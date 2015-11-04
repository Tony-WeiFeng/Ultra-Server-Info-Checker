'''
Created on Oct 27, 2015

@author: tfeng
'''
import sqlite3
import os

# Preparation: Create DB folder under execution path if it's not existed.
currentPath = os.path.abspath('.')
DBPath = os.path.abspath(currentPath + '/DB/')
if not os.path.exists(DBPath):
    os.mkdir(DBPath)

# def __DBCreator(sqliteDBName):
#     
#     # Sqlite Database name
#     #DBName = "ServerInfo.db"
#     '''
#     Description: Create a DB to store server information.
#     '''
#     
#     try:
#         # Connect Database. It will be created if it's not existed.
#         DBConnection = sqlite3.connect(os.path.join(DBPath, sqliteDBName))
#         DBConnection.commit()
#     
#     except sqlite3.Error,e:
#         print "Failed to connect sqlite3 database!", "\n", e.args[0]
#         return
#     
#     DBConnection.close();

def tableCreator(DBName, tableCreateString):
    # Create DB Connection
    DBConnection = sqlite3.connect(os.path.join(DBPath, DBName))
    
    #Create a cursor for Database operation
    cur = DBConnection.cursor()                                                                   
    try:
        cur.execute(tableCreateString)
        # For sqlite3 DB, after every execution, need call the function of the connection.  
        DBConnection.commit()
    except sqlite3.Error,e:
        print "Failed to create table!", "\n", e.args[0]
        return
    DBConnection.close()

def executeSQL(DBName, SQLString):
    # Create DB Connection
    try:
        # Connect Database. It will be created if it's not existed.
        DBConnection = sqlite3.connect(os.path.join(DBPath, DBName))
        DBConnection.commit()
    
    except sqlite3.Error,e:
        print "Failed to connect sqlite3 database!", "\n", e.args[0]
        return
    
    # Create a cursor for Database operation
    cur = DBConnection.cursor()
    
    # Create table if it's not exist.
    try:
        cur.execute(SQLString)
        DBConnection.commit()
        return cur.fetchall()
    except sqlite3.Error,e:
        print "Failed to execute the SQL:" + SQLString, "\n", e.args[0]
        return
    
    DBConnection.close()


if __name__ == '__main__':    
    pass