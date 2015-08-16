'''
Created on 2015-08-15

@author: James

list_example
'''

list_1=["a", "b", "google", "zach", "steph"]
print list_1
print list_1[0]
print list_1[4]

print
print list_1
print list_1[-1].upper()
print list_1[-4]

print
print list_1
print list_1[1:3]
print list_1[1:-1]
print list_1[0:3]

print
print list_1
print list_1[:3]
print list_1[3:]
print list_1[:]

print
print list_1
list_1.append("klay")
print list_1
list_1.insert(2, "andre")
print list_1
list_1.extend(["two","elements"])
print list_1

print
print list_1
print list_1.index("zach", )
print list_1.index("steph")

print
print list_1
list_1.remove("two")
print list_1
print list_1.pop()
print list_1

print
list_2=['a', 'b', 'data', 'warriors']
list_2=list_2+['golden', 'state']
print list_2
list_2+=['champion']
print list_2

print
list_3=['5', '32']
list_3=list_3*3
print list_3