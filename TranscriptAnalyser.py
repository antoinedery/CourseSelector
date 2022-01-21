from operator import indexOf
import time
import PyPDF2
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageScraper import createCoursesDictionary
from EmailSender import sendEmailTranscriptAnalyser

def runTranscriptAnalyser(username, password, dob, email, courses):
    createCoursesDictionary()
    while(len(courses) > 0):
        print("Program is running...")
        openBrowser()
        logIntoStudentAccount(username, password, dob)
        downloadPDF(email, courses)
        time.sleep(30)


def openBrowser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    prefs = {"plugins.always_open_pdf_externally": True,
             "download.default_directory": dir_path}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    openBrowser.driver = webdriver.Chrome(options=chrome_options)
    url = 'https://dossieretudiant.polymtl.ca/WebEtudiant7/poly.html'
    openBrowser.driver.get(url)


def logIntoStudentAccount(username, password, dob):
    openBrowser.driver.find_element(By.ID, "code").send_keys(username)
    openBrowser.driver.find_element(By.ID, "nip").send_keys(password)
    openBrowser.driver.find_element(By.ID, "naissance").send_keys(dob)
    openBrowser.driver.find_element(
        By.XPATH, "//input[@type='submit' and @value='Connexion']").click()


def downloadPDF(email, courses):
    openBrowser.driver.find_element(By.NAME, "btnBulCumul").click()
    time.sleep(5)
    parsePDF(email, courses)

def parsePDF(email, courses):
    fileName = [filename for filename in os.listdir(
        '.') if filename.startswith("bulletin_cumulatif-")]
    pdfFile = open(fileName[0], 'rb')
    pdfReaderObj = PyPDF2.PdfFileReader(pdfFile)
    content = ''
    for page in range(0, pdfReaderObj.numPages):
        content += (pdfReaderObj.getPage(page).extractText())

    contentList = content.split()
    for course in courses:
        if(course not in createCoursesDictionary.courses):
            print("The course " + course + " does not exist.")
            return
        index = 0
        index = contentList.index(course)
        while(contentList[index] != str(createCoursesDictionary.courses[course])):
            index += 1

        possibleGrades = {'A*', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D'}
        if(contentList[index+1] in possibleGrades):
            courses.remove(course)
            print(courses)
            print('A grade was found for ' + course + '! Your grade is : ' + contentList[index+1] + '.')
            sendEmailTranscriptAnalyser(email, course)
        else:
            print("No grade for " + course + '.')

