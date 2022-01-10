import smtplib
import ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "PolyScheduleModifier@gmail.com"
password = input("Type your password and press enter: ")

def sendEmail(courseNumber, thGroup, labGroup, userEmailAddress):
    message = """\
    Subject:""" + courseNumber + """ was added to your schedule - PolyScheduleModifier

    This message is to inform you that the course """ + courseNumber + """ was added to your schedule in the following groups: 
    Theoretical group: """ + thGroup + """
    Laboratory group: """ + labGroup + """

    Thank you for using PolyScheduleModifier!

    Antoine
    """
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, userEmailAddress, message)