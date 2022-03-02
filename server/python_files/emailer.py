import smtplib
from email.message import EmailMessage

port = 587
smtpServer = "smtp.gmail.com"
senderEmail = "PolyScheduleModifier@gmail.com"
appPassword = "niryziqrdghvzggc"

server = smtplib.SMTP(smtpServer, port)
server.starttls()
server.login(senderEmail, appPassword)

def sendEmailTranscriptAnalyser(userEmailAddress, foundGrades):
    msg = EmailMessage()

    foundGradesString = "\n\n"

    for k,v in foundGrades.items():
        foundGradesString += str(k) + " : " + str(v) + '\n'

    message = "Bonjour,\n\nCe message est pour vous informer qu'une note a été ajoutée à votre bulletin pour le(s) cours suivant(s) :" + foundGradesString + "\nSe connecter au dossier étudiant : www.dossieretudiant.polymtl.ca/WebEtudiant7/poly.html\n\nMerci d'avoir utilisé PolyStudentTools!"
    # messageHTML = MIMEText(message,'html')
    msg.set_content(message)
    msg['Subject'] =  "PolyStudentTools - " + "Nouvelle note sur votre bulletin"
    msg['From'] = senderEmail
    msg['To'] = userEmailAddress
    server.send_message(msg)

# def sendEmailCourseAdder(courseNumber, thGroup, labGroup, userEmailAddress):
#     msg = EmailMessage()

#     message = """\
#     This message is to inform you that the course """ + courseNumber + """ was added to your schedule in the following groups: 
#     Theoretical group: """ + thGroup + """
#     Laboratory group: """ + labGroup + """

#     Thank you for using this tool!
#     """
#     msg.set_content(message)
#     msg['Subject'] =  "PolyScheduleModifier - " + courseNumber + " was added to your schedule"
#     msg['From'] = senderEmail
#     msg['To'] = userEmailAddress
#     server.send_message(msg)
