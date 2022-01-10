import smtplib
from email.message import EmailMessage

port = 587
smtpServer = "smtp.gmail.com"
senderEmail = "PolyScheduleModifier@gmail.com"
appPassword = "niryziqrdghvzggc"

def sendEmail(courseNumber, thGroup, labGroup, userEmailAddress):
    server = smtplib.SMTP(smtpServer, port)
    server.starttls()
    server.login(senderEmail, appPassword)

    msg = EmailMessage()

    message = """\
    This message is to inform you that the course """ + courseNumber + """ was added to your schedule in the following groups: 
    Theoretical group: """ + thGroup + """
    Laboratory group: """ + labGroup + """

    Thank you for using PolyScheduleModifier!
    """
    msg.set_content(message)
    msg['Subject'] =  "PolyScheduleModifier - " + courseNumber + " was added to your schedule"
    msg['From'] = senderEmail
    msg['To'] = userEmailAddress
    server.send_message(msg)