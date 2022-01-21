import pwinput
import time
# from CourseAdder import addCourse, logIntoStudentAccount, openBrowser
# from EmailSender import sendEmail
from PdfReader import downloadPDF, logIntoStudentAccount, openBrowser

username = input("Enter your Poly username : ")
password = pwinput.pwinput(prompt="Enter your Poly password : ")
dob = input("Enter your date of birth (YYYYMMDD or YYMMDD) : ")
# courseNumber = input("Enter the course name : ")
# thGroup = input("Enter the theoretical group number : ")
# labGroup = input("Enter the lab group number : ")
# email = input("Enter your email address : ")

openBrowser()
logIntoStudentAccount(username, password, dob)
downloadPDF()

# isCourseAdded = False
# while not(isCourseAdded):
#     print("Program is running...")
#     openBrowser()
#     logIntoStudentAccount(username, password, dob)
#     isCourseAdded = addCourse(courseNumber, thGroup, labGroup)
#     if not (isCourseAdded) : time.sleep(60)

# sendEmail(courseNumber, thGroup, labGroup, email)
