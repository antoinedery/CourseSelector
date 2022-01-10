import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "PolyScheduleModifier@gmail.com"
userEmailAddress = "antoinedery12@hotmail.fr"
password = input("Type your password and press enter: ")

def sendEmail(courseNumber, userEmailAddress) : 
    message = """\
    Subject: PolyScheduleModifier - Your course was added
    This message is to inform you that the course {courseNumber} was added to your schedule"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, userEmailAddress, message)