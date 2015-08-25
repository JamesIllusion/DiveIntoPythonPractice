'''
Created on 2015-08-16

@author: James

getattr_example
'''

li=['larry', 'bird']
li.pop()
print getattr(li, "pop")
print getattr(li, "append")("magic")
print li

print
print getattr({}, "clear")
#print getattr((), "pop")