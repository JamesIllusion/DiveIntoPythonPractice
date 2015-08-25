'''
Created on 2015-08-19

@author: James

filter_list_example
'''

list_1=['a', 'mpilgrim', 'foo', 'b', 'c', 'd', 'e', 'd']
print [elem for elem in list_1 if len(elem)>1]
print [elem for elem in list_1 if elem!='b']
print [elem for elem in list_1 if list_1.count(elem)!=1]