import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from EmailSender import sendEmailCourseAdder


def runCourseAdder(username, password, dob, email, courseNumber, thGroup, labGroup):
    isCourseAdded = False
    while not(isCourseAdded):
        print("Program is running...")
        openBrowser()
        logIntoStudentAccount(username, password, dob)
        isCourseAdded = addCourse(courseNumber, thGroup, labGroup)
        if not (isCourseAdded) : time.sleep(120)
    sendEmailCourseAdder(courseNumber, thGroup, labGroup, email)

def openBrowser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    openBrowser.driver = webdriver.Chrome(options=chrome_options)
    url = 'https://dossieretudiant.polymtl.ca/WebEtudiant7/poly.html'
    openBrowser.driver.get(url)

def logIntoStudentAccount(username, password, dob):
    openBrowser.driver.find_element(By.ID, "code").send_keys(username)
    openBrowser.driver.find_element(By.ID, "nip").send_keys(password)
    openBrowser.driver.find_element(By.ID, "naissance").send_keys(dob)
    openBrowser.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Connexion']").click()

def verifyIsCourseFull():
    WebDriverWait(openBrowser.driver, 1).until(EC.alert_is_present())
    if(openBrowser.driver.switch_to.alert.text.startswith("Il n'y a plus de places")):
        openBrowser.driver.switch_to.alert.accept()
        return True # Course is already full
    openBrowser.driver.switch_to.alert.accept()
    return False

def addCourse(courseNumber, thGroup, labGroup):
    openBrowser.driver.find_element(By.NAME, "btnModif").click()
    for index in range(1, 11):
        course = openBrowser.driver.find_element(By.NAME, "sigle"+str(index))
        if(course.get_attribute("value") == courseNumber):
            openBrowser.driver.find_element(By.NAME, "grtheo"+str(index)).send_keys(Keys.CONTROL, "a")
            openBrowser.driver.find_element(By.NAME, "grtheo"+str(index)).send_keys(thGroup)
            openBrowser.driver.find_element(By.NAME, "grlab"+str(index)).click()
            try:
                if(verifyIsCourseFull()):   # Alert : thGroup and labGroup has to be the same
                    openBrowser.driver.close()
                    print("Error : group is full")
                    return False
            except TimeoutException:
                continue

            try:
                if(verifyIsCourseFull()):   # Alert : conflicts in schedule
                    openBrowser.driver.close()
                    print("Error : group is full")
                    return False
            except TimeoutException:
                continue 
            openBrowser.driver.find_element(By.NAME, "grlab"+str(index)).send_keys(Keys.CONTROL, "a")
            openBrowser.driver.find_element(By.NAME, "grlab"+str(index)).send_keys(labGroup)
            break

        elif(course.get_attribute("value") == ''):
            course.send_keys(courseNumber)
            openBrowser.driver.find_element(By.NAME, "grtheo"+str(index)).send_keys(thGroup)
            openBrowser.driver.find_element(By.NAME, "grlab"+str(index)).click()

            try:
                if(verifyIsCourseFull()):   # Alert : thGroup and labGroup has to be the same
                    openBrowser.driver.close()
                    print("Error : group is full")
                    return False
            except TimeoutException:
                continue

            try:
                if(verifyIsCourseFull()):   # Alert : conflicts in schedule
                    openBrowser.driver.close()
                    print("Error : group is full")
                    return False
            except TimeoutException:
                continue 

            openBrowser.driver.find_element(By.NAME, "grlab"+str(index)).send_keys(labGroup)
            break
    openBrowser.driver.find_element(By.XPATH, "//input[@type='button' and @value='Enregistrer']").click()
    try:
        verifyIsCourseFull()    # Alert : conflicts in schedule again
    except TimeoutException:
        pass
    print(courseNumber + " was added to your schedule !")
    return True