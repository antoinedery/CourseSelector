# import PyPDF2
 
# # creating a pdf file object
# pdfFileObj = open('Bulletin.pdf', 'rb')
 
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# # printing number of pages in pdf file
# print(pdfReader.numPages)
 
# # creating a page object
# pageObj = pdfReader.getPage(0)
 
# # extracting text from page
# print(pageObj.extractText())
 
# # closing the pdf file object
# pdfFileObj.close()

import time
import autoit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def openBrowser():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    openBrowser.driver = webdriver.Chrome(options=chrome_options)
    url = 'https://dossieretudiant.polymtl.ca/WebEtudiant7/poly.html'
    openBrowser.driver.get(url)

def logIntoStudentAccount(username, password, dob):
    openBrowser.driver.find_element(By.ID, "code").send_keys(username)
    openBrowser.driver.find_element(By.ID, "nip").send_keys(password)
    openBrowser.driver.find_element(By.ID, "naissance").send_keys(dob)
    openBrowser.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Connexion']").click()

def openPDF():
    openBrowser.driver.find_element(By.NAME, "btnBulCumul").click()
    time.sleep(2)

    Pdf

    ##autoit.send("^p")
    ##time.sleep(2)
    ##openBrowser.driver.find_element_by_class_name("md-select").click()
    # select.select_by_value("Save as PDF/local/")


