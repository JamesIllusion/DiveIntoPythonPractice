'''
Created on 2015-08-27

@author: James

urllib_example
'''

import urllib, urllister
sock=urllib.urlopen('http://diveintopython.org')
htmlSource=sock.read()
sock.close()
print htmlSource

from sgmllib import SGMLParser
class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls=[]
        
    def start_a(self,attrs):
        href=[v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)
        
#Example 8.7            
print ("Below is for example 8.7")   
usock=urllib.urlopen("http://diveintopython.org/")
parser=urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls: print url