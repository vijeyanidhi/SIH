frontend

Azad kumar

Backend and security
Vijeyanidhi
Mayank

OCR
Nishee
Vikas Yadav
Amit Kumar Jena

## Details for the OCR part:
Python libraries required:
1. OpenCV
2. Pytesseract
3. Pandas
4. Gensim
5. Numpy

Clone the CliNER repository and install it as written here: https://github.com/text-machine-lab/CliNER
CliNER is required to do analysis and extract information of problems, tests and treatments listed in the medical report. 

Extract the Lab Reports.zip file. It contains some sample reports as well as required .csv files which contains the list of keywords to be searched in the report by RegEx.

The 'Information extraction' python file and notebook perform the same operation. We are able to extract following details:
1. dict_basic: python dictionary which stores Basic Details like Name, Date, Age etc.
2. dict_blood (in case of Blood reports): python dictionary which stores Values of the Parameters as written in the Blood reports
3. dict_urine (in case of Urine reports): python dictionary which stores Values of the Parameters as present in the Urine reports
4. Comments_Report: Comments written in the report, followed by the keyword 'Comments' (if available)
5. Summary: summary of the comments (if available)
6. list_problem: list of terms/phrases in the report which are categorised as 'Problem' by CliNER
7. list_treatment: list of terms/phrases in the report which are categorised as 'Treatment' by CliNER
8. list_tests: list of terms/phrases in the report which are categorised as 'Test' by CliNER
