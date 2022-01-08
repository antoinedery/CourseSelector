from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
url = 'https://dossieretudiant.polymtl.ca/WebEtudiant7/poly.html'
driver.get(url)

def logIntoStudentAccount(username, password, dob):
    driver.find_element(By.ID, "code").send_keys(username)
    driver.find_element(By.ID, "nip").send_keys(password)
    driver.find_element(By.ID, "naissance").send_keys(dob)
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Connexion']").click()

def verifyIsCourseFull():
    WebDriverWait(driver, 1).until(EC.alert_is_present())
    if(driver.switch_to.alert.text.startswith("Il n'y a plus de places")):
        driver.switch_to.alert.accept()
        return True # Course is already full
    driver.switch_to.alert.accept()
    return False

def addCourse(courseNumber, thGroup, labGroup):
    driver.find_element(By.NAME, "btnModif").click()
    for index in range(1, 11):
        course = driver.find_element(By.NAME, "sigle"+str(index))
        if(course.get_attribute("value") == courseNumber):
            driver.find_element(By.NAME, "grtheo"+str(index)).send_keys(Keys.CONTROL, "a")
            driver.find_element(By.NAME, "grtheo"+str(index)).send_keys(thGroup)
            driver.find_element(By.NAME, "grlab"+str(index)).click()
            try:
                if(verifyIsCourseFull()):   # Alert : thGroup and labGroup has to be the same
                    driver.close()
                    return False
            except TimeoutException:
                continue

            try:
                if(verifyIsCourseFull()):   # Alert : conflicts in schedule
                    driver.close()
                    return False
            except TimeoutException:
                continue 
            driver.find_element(By.NAME, "grlab"+str(index)).send_keys(Keys.CONTROL, "a")
            driver.find_element(By.NAME, "grlab"+str(index)).send_keys(labGroup)
            break

        elif(course.get_attribute("value") == ''):
            course.send_keys(courseNumber)
            driver.find_element(By.NAME, "grtheo"+str(index)).send_keys(thGroup)
            driver.find_element(By.NAME, "grlab"+str(index)).click()

            try:
                if(verifyIsCourseFull()):   # Alert : thGroup and labGroup has to be the same
                    driver.close()
                    return False
            except TimeoutException:
                continue

            try:
                if(verifyIsCourseFull()):   # Alert : conflicts in schedule
                    driver.close()
                    return False
            except TimeoutException:
                continue 

            driver.find_element(By.NAME, "grlab"+str(index)).send_keys(labGroup)
            break
    driver.find_element(By.XPATH, "//input[@type='button' and @value='Enregistrer']").click()
    try:
        verifyIsCourseFull()    # Alert : conflicts in schedule again
    except TimeoutException:
        pass
    return True

