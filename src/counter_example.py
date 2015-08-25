'''
Created on 2015-08-23

@author: James

counter_example
'''

class counter:
    count = 0
    def __init__(self):
        self.__class__.count+=1
        
print counter.count

print
c=counter()
print c.count