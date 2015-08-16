'''
Created on 2015-08-15

@author: James

ditionary_example
'''

dic_1={"server":"mpilgrim", "database":"master"}
print dic_1
print dic_1["server"]
print dic_1["database"]

print "\n"
dic_1["database"]="pubs"
print dic_1

print "\n"
dic_1["uid"]="sa"
print dic_1

print "\n"
dic_2={}
dic_2["key"]="value"
dic_2["key"]="other_value"
print dic_2

print "\n"
dic_2["KEY"]="VALUE"
print dic_2

print 
dic_1["retrycount"]=3
print dic_1

print
dic_1[43]="douglas"
print dic_1
del dic_1[43]
print dic_1

print
dic_1.clear()
print dic_1