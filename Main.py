import pwinput
import time
from CourseAdder import addCourse, logIntoStudentAccount, openBrowser

username = input("Enter your username : ")
password = pwinput.pwinput(prompt="Enter your password : ")
dob = pwinput.pwinput(prompt="Enter your date of birth (YYYYMMDD or YYMMDD) : ")
courseNumber = input("Enter the course name : ")
thGroup = input("Enter the theoretical group number : ")
labGroup = input("Enter the lab group number : ")

isCourseAdded = False
while not(isCourseAdded):
    print("Program is running...")
    openBrowser()
    logIntoStudentAccount(username, password, dob)
    addCourse(courseNumber, thGroup, labGroup)
    time.sleep(60)
