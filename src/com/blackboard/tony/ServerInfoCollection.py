'''
Created on Oct 29, 2015

@author: tfeng
'''
import time
from ServerInfoRecorder import recordServerInfo
from ReportGenerator import generateServerInfoReport
from EmailSender import sendEmail

#serverURLList = ['https://ultra-qa1.int.bbpd.io','https://saas-stg.int.bbpd.io','https://qa-ultra-std-clienttest.int.bbpd.io','https://qa-ultra-std-ga.int.bbpd.io']
serverURLList = ['https://ultra-qa1.int.bbpd.io','https://saas-stg.int.bbpd.io','https://qa-ultra-std-ga.int.bbpd.io']

# Record server information into DB
for i in range(len(serverURLList)):
    recordServerInfo(serverURLList[i])

now = time.strftime('%Y-%m-%d %H:%M:%S %Z',time.localtime(time.time()))
subject = 'Server Info Report: ' + str(now)
messageBody = generateServerInfoReport()
#receiver = 'tony.feng@blackboard.com,bob.liu@blackboard.com'
receiver = 'CCoELearnQA@blackboard.com'

sendEmail(receiver, subject, messageBody)

if __name__ == '__main__':
    pass