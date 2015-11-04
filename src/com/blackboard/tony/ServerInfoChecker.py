'''
Created on Oct 27, 2015

@author: tfeng
'''
import urllib2
import re

class ServerInfoChecker(object):
    '''
    classdocs
    '''    

    def __init__(self, URL):
        '''
        Constructor
        '''
        self.serverURL = URL
        
    def getCommitID(self):
        serverURL = self.serverURL
        # Open the ultra page, then the source page of ultra will contain uiv info.
        urllib2.urlopen(serverURL + '/ultra/')
        
        for i in range(10):
            pageSource = urllib2.urlopen(serverURL + '/ultra/').read()
            if len(re.findall('<base href="([^"]+)">', pageSource)) > 0:
                basehref = re.findall('<base href="([^"]+)">', pageSource)[0]
                uiv = re.findall('/ultra/([^/]+)/', basehref)[0]
                break
            else:
                i += 1
        commitIDURL = serverURL + '/ultra/' + uiv + '/build-info.json'
        commitInfo = urllib2.urlopen(commitIDURL).read()
        commitID = re.findall('"commit": "([^"]+)",', commitInfo)[0]
        
        return commitID
    
    def getBuildID(self):
        serverURL = self.serverURL
        
        for i in range (10):
            buildInfo = str(urllib2.urlopen(serverURL).info())
            if len(re.findall('X-Blackboard-product: Blackboard Learn &#8482; ([\S]+)',buildInfo)) > 0:
                buildID = re.findall('X-Blackboard-product: Blackboard Learn &#8482; ([\S]+)',buildInfo)[0]
            else:
                i += 1
        return buildID
    
if __name__ == '__main__':
#     ma = ServerInfoChecker('https://ultra-qa1.int.bbpd.io')
#     ma.getBuildID()
    pass