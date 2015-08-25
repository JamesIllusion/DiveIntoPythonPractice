'''
Created on 2015-08-16

@author: James

blank_test
'''

from apihelper import  info
import odbchelper

list_test=[]
info(list_test)

print
info(odbchelper)

print
print odbchelper.buildConnectionString
print getattr(odbchelper, "buildConnectionString")

print
object=odbchelper
method="buildConnectionString"
print getattr(object, method)

print
print type(getattr(object, method))

print
import types
print type(getattr(object, method))==types.FunctionType

print
print callable(getattr(object, method))

print
import statsout
def output(data, format='text'):
    output_function=getattr(statsout, "output_%s" %format)
    print output_function(data)
    return output_function(data)

