import pwinput
import time
from CourseAdder import addCourse, logIntoStudentAccount, openBrowser
from EmailSender import sendEmail

username = input("Enter your username : ")
password = pwinput.pwinput(prompt="Enter your password : ")
dob = pwinput.pwinput(prompt="Enter your date of birth (YYYYMMDD or YYMMDD) : ")
courseNumber = input("Enter the course name : ")
thGroup = input("Enter the theoretical group number : ")
labGroup = input("Enter the lab group number : ")
email = input("Enter your email address : ")

isCourseAdded = False
while not(isCourseAdded):
    print("Program is running...")
    openBrowser()
    logIntoStudentAccount(username, password, dob)
    isCourseAdded = addCourse(courseNumber, thGroup, labGroup)
    if not (isCourseAdded) : time.sleep(60)

sendEmail(courseNumber, email)
