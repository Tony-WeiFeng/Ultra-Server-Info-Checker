'''
Created on Oct 28, 2015

@author: tfeng
'''
import re
import ServerInfoChecker
import DataStore

#currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
dbName = 'DB_UltraServerInfo'

def recordServerInfo(serverURL):
    sic = ServerInfoChecker.ServerInfoChecker(serverURL)
    commitID = sic.getCommitID()
    buildID = sic.getBuildID()
    serverName = re.findall('https://([^.]+).int.', serverURL)[0]
    executeTime = 'DATETIME(\'NOW\')'
    
    # Create table if the table for storing the server info is not exist.
    tableCreateString = ''' CREATE TABLE IF NOT EXISTS SERVER_INFO ( ID INTEGER PRIMARY KEY,
                                                                SERVER_NAME VARCHAR(50),
                                                                SERVER_URL VARCHAR(200),
                                                                BUILD_ID VARCHAR(100),
                                                                BUILD_ID_PUDATED INTEGER,
                                                                BUILD_ID_LAST_UPDATE_TIME DATETIME,
                                                                COMMIT_ID VARCHAR(200),
                                                                COMMIT_ID_UPDATED INTEGER,
                                                                COMMIT_ID_LAST_UPDATE_TIME DATETIME,
                                                                EXECUTE_TIME DATETIME
                                                                );'''
    DataStore.tableCreator(dbName, tableCreateString)
    
    sqlStringQueryLastCommitID = 'SELECT COMMIT_ID,COMMIT_ID_LAST_UPDATE_TIME,BUILD_ID,BUILD_ID_LAST_UPDATE_TIME FROM SERVER_INFO WHERE SERVER_URL = \'' + serverURL + '\' ORDER BY EXECUTE_TIME DESC LIMIT 1;'
    qResults = DataStore.executeSQL(dbName, sqlStringQueryLastCommitID)

    if len(qResults) > 0:
        queryResult = qResults[0]
        lastCommitID = str(queryResult[0])
        commitIDLastUpdateTime = str(queryResult[1])
        lastBuildID = str(queryResult[2])
        buildIDLastUpdateTime = str(queryResult[3])
        
        if commitID == lastCommitID:
            commitIDUpdated = 0
            #commitIDLastUpdateTime = 'DATATIME(' + commitIDLastUpdateTime + ')'
            commitIDLastUpdateTime = '\'' + commitIDLastUpdateTime + '\''
        else:
            commitIDUpdated = 1
            #commitIDLastUpdateTime = 'DATETIME(\'NOW\')'        
            commitIDLastUpdateTime = executeTime
                    
        if buildID == lastBuildID:
            buildIDUpdated = 0
            buildIDLastUpdateTime = '\'' + buildIDLastUpdateTime + '\''
        else:
            buildIDUpdated = 1
            #buildIDLastUpdateTime = 'DATETIME(\'NOW\')' 
            buildIDLastUpdateTime = executeTime
    else:
        commitIDUpdated = 1
        #commitIDLastUpdateTime = 'DATETIME(\'NOW\')'
        commitIDLastUpdateTime = executeTime
        buildIDUpdated = 1
        #buildIDLastUpdateTime = 'DATETIME(\'NOW\')'
        buildIDLastUpdateTime = executeTime
        
    #print(lastCommitID)
    
    #sqlStringQueryLastBuildID = 
    
    sqlStringInsertServerInfo = 'INSERT INTO SERVER_INFO VALUES(null, \'' + serverName + '\', \'' + serverURL + '\', \'' + buildID + '\','  + str(buildIDUpdated) + ', ' + buildIDLastUpdateTime + ', \'' + commitID + '\',' + str(commitIDUpdated) +', ' + commitIDLastUpdateTime + ', ' + executeTime + ');'

    DataStore.executeSQL(dbName, sqlStringInsertServerInfo)
    #print(serverName)

if __name__ == '__main__':    
    pass



