'''
Created on Oct 29, 2015

@author: tfeng
'''
import smtplib  
from email.mime.text import MIMEText

def sendEmail(to, subject, message):
    smtpserver = '10.75.106.10:25'
    fro = 'printer.shanghai@blackboard.com'
    
    msg = MIMEText(message, "html", "utf-8")
    msg['From'] = fro
    msg['Subject'] = subject
    msg['To'] = to

    smtp = smtplib.SMTP(smtpserver)
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()
    
if __name__ == '__main__':

    pass