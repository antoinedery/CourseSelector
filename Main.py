import pwinput

username = input("Enter your username : ")
password = pwinput.pwinput(prompt="Enter your password : ")
dob =  pwinput.pwinput(prompt="Enter your date of birth (YYYYMMDD or YYMMDD) : ")
courseNumber = input("Enter the course name : ")
thGroup = input("Enter the theoretical group number : ")
labGroup = input("Enter the lab group number : ")

from CourseAdder import addCourse, logIntoStudentAccount
logIntoStudentAccount(username, password, dob)
print(addCourse(courseNumber, thGroup, labGroup))