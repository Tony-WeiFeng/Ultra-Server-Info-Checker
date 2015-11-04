'''
Created on Oct 29, 2015

@author: tfeng
'''
import datetime
from DataStore import executeSQL

dbName = 'DB_UltraServerInfo'

def generateServerInfoReport():
    sqlStringQueryServersInfo = 'SELECT * FROM SERVER_INFO GROUP BY SERVER_URL;'
    
    resuts = executeSQL(dbName, sqlStringQueryServersInfo)
    
    tableString = '''<h4>Server Information:</h4>
                <table border="1">
                    <tr>
                        <th>Server Name</th>
                        <th>Server URL</th>
                        <th>Build ID</th>
                        <th>Commit ID</th>
                    </tr>'''
    envString = ''
    isolationString = '''<br>*Isolation Detail:*<br>
                        ||server||environment||result||<br>
                    '''
    
    for i in range(len(resuts)):
        serverName = resuts[i][1]
        serverURL = resuts[i][2]
        buildID = resuts[i][3]
        buildIDUpdated = resuts[i][4]
        buildIDLastUpdateTime = resuts[i][5]
    
        commitID = resuts[i][6]
        commitIDUpdated = resuts[i][7]
        commitIDLastUpdateTime = resuts[i][8]
        
        executeTime = resuts[i][9]
        
        bLastUpdateTime = datetime.datetime.strptime(buildIDLastUpdateTime, '%Y-%m-%d %H:%M:%S')
        cLastUpdateTime = datetime.datetime.strptime(commitIDLastUpdateTime, '%Y-%m-%d %H:%M:%S')
        eTime = datetime.datetime.strptime(executeTime, '%Y-%m-%d %H:%M:%S')
        
        
        buildDateOffset = (eTime - bLastUpdateTime).days
        commitDateOffset = (eTime - cLastUpdateTime).days
        
        oriBuildID = buildID
        oriCommitID = commitID
        
        if buildIDUpdated == 0 and buildDateOffset >= 1:
            buildID = '<div>' + buildID + '</div><div style="color:red">Build ID had not been updated for ' + str(buildDateOffset) + ' day(s)</div>'
            
        if commitIDUpdated == 0 and commitDateOffset >= 1:
            commitID = '<div>' + commitID + '</div><div style="color:red">Commit ID had not been updated for ' + str(commitDateOffset) + ' day(s)</div>'    
        
        rowString = '''
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>                    
                    </tr>'''%(serverName, serverURL, buildID, commitID)
        
        tableString += rowString
        
        serverInfoString = '''Server: %s <br>
                            Build ID: %s <br>
                            Commit ID: %s'''%(serverURL, oriBuildID, oriCommitID)
        
        envString += '*Environment:*<br>'
        envString += serverInfoString + '<br><br>'
        
        isolationString += '|%s|%s|test result|<br>'%(serverName,serverInfoString)
    tableString += '</table><br><br><br>'
    
    messageBody = tableString + envString + isolationString + '<br><br><br>Thanks,<br>Learn Shanghai QA Team'
    
    return messageBody
    
if __name__ == '__main__':
    pass