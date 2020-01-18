import cv2 
import pytesseract
import numpy as np
import re
import pandas as pd
from gensim.summarization.summarizer import summarize
import os

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)[1]

#dilation
def dilate(image):
    kernel = np.ones((2,2),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((2,2),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((2,2),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if(angle < -45):
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

#Function to extract Basic information related to Patient
def Basic_details(text):
    dict_basic =  []
    df_basic = pd.read_csv('Basic_details.csv')

    pattern1=re.compile(r'(Name|NAME)[\s]?[:]?[\s]?(MR|MRS|MS|Mr|Ms|Mrs|PATIENT|Patient)?([\.]?[\s]?[a-zA-Z]+)')
    matches=pattern1.finditer(text)
    for match in matches:
        name = match.group(3)
        dict_basic.append(['Name:', name])
        break
    for i in range(len(df_basic)):
        match = re.search(df_basic['Fields'][i]+'(\S+\s+)', text)
        if match:
            weather = match.group(1)
            dict_basic.append([df_basic['Fields'][i], weather])

        match = re.search(df_basic['Fields'][i]+' (\S+\s+)', text)
        if match:
            weather = match.group(1)
            dict_basic.append([df_basic['Fields'][i], weather]) 
    
    dict_basic = pd.DataFrame(dict_basic, columns=['Basic details', 'Values'])
    return dict_basic        

#Function to extract information related to Blood tests
def Blood_Test_Details(text):
    dict_blood =  []
    df = pd.read_csv('lab report parameters  - Sheet1.csv')
    for i in range(len(df)):
        param = df['Parameter_Name'][i]
        match = re.search(df['Parameter_Name'][i]+' (\S+)', text)
        if match:
            weather = match.group(1)
            dict_blood.append([param, weather])

    dict_blood = pd.DataFrame(dict_blood, columns=['Sections', 'Values Obtained'])  
    return dict_blood


#Function to extract information related to Urine tests
def Urine_Test_Details(text):
    dict_urine =  []
    df = pd.read_csv('URINE_TEST - Sheet1.csv')
    for i in range(len(df)):
        param = df['Fields'][i]
        match = re.search(param+' (\S+)', text)
        if match:
            weather = match.group(1)
            dict_urine.append([param, weather])

    dict_urine = pd.DataFrame(dict_urine, columns=['Sections', 'Values Obtained'])
    return dict_urine


#Extracting comments from report
def comment_extract(text):
    mystring =  text
    keyword = 'Comments'
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    return after_keyword

def report_summary(text):
    return summarize(text)

def process_img(fp):
#Image pre-processing before feeding it to OCR algorithm
    factor = 2
    img = cv2.imread(fp)
    img = cv2.resize(img, (factor*img.shape[1],factor*img.shape[0]), interpolation = cv2.INTER_CUBIC)
    img = get_grayscale(img)
    img = deskew(img)
#img = thresholding(img)

#Text extraction by OCR (line by line)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    file1 = open("raw_text.txt","w") 
    file1.write(text)  
    file1.close()
    
    dict_basic = Basic_details(text)    
    dict_blood = Blood_Test_Details(text)
    dict_urine = Urine_Test_Details(text)
    Comments_Report = comment_extract(text)
    Summary = report_summary(Comments_Report)

#Problem, tests and treatment extraction from reports
    arg1 = 'raw_text.txt'
    os.system("CliNER/cliner predict --txt " + arg1 + " --out CliNER/data/predictions --model CliNER/models/silver.crf.1 --format i2b2")
    file1 = open("/home/amit/CliNER/data/predictions/raw_text.con","r+")
    data = file1.readlines()
    list_problem = []
    list_treatment = []
    list_tests = []
    for i in range(len(data)):
        description = data[i].split('"')[1]
        inference = data[i].split('"')[3]
        if inference=='problem':
            list_problem.append(description)
        elif inference=='treatment':
            list_treatment.append(description)
        else:
            list_tests.append(description)
    
    return list_problem,list_treatment,list_tests,dict_basic,dict_blood,dict_urine,Comments_Report,Summary
