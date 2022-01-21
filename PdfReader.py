import time
import PyPDF2
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def openBrowser():
    chrome_options= webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    prefs = {"plugins.always_open_pdf_externally": True, "download.default_directory" : dir_path}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option(
          'excludeSwitches', ['enable-logging'])
    openBrowser.driver=webdriver.Chrome(options = chrome_options)
    url='https://dossieretudiant.polymtl.ca/WebEtudiant7/poly.html'
    openBrowser.driver.get(url)

def logIntoStudentAccount(username, password, dob):
    openBrowser.driver.find_element(By.ID, "code").send_keys(username)
    openBrowser.driver.find_element(By.ID, "nip").send_keys(password)
    openBrowser.driver.find_element(By.ID, "naissance").send_keys(dob)
    openBrowser.driver.find_element(
        By.XPATH, "//input[@type='submit' and @value='Connexion']").click()

def downloadPDF(id):
    openBrowser.driver.find_element(By.NAME, "btnBulCumul").click()
    # time.sleep(5)
    parsePDF(id)

def parsePDF(id):
    # creating a pdf file object
    pdfFileObj = open('bulletin_cumulatif-'+id+'.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    # print(pdfReader.numPages)
    for page in range(0, pdfReader.numPages):
        print(pdfReader.getPage(page).extractText())
    # print(pdfReader.getPage(1).extractText())   

    # closing the pdf file object
    pdfFileObj.close()
