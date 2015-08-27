'''
Created on 2015-08-26

@author: James

blank_tesT_ch7
'''
from sre_parse import Pattern

#Example7.1
s_1='100 NORTH MAIN ROAD'
print s_1.replace('ROAD', 'RD.')
print
s_2 ='100 NORTH BROAD ROAD'
print s_2.replace('ROAD', 'RD.')
print s_2[:-4]+s_2[-4:].replace('ROAD', 'RD.')
print
import re
print re.sub('ROAD$', 'RD.', s_2)

#Example7.2
print
s_3='100 BROAD'
print re.sub('ROAD$', 'RD.', s_3)
print re.sub('\\bROAD$', 'RD', s_3)
print re.sub('\bROAD$', 'RD', s_3)
print
s_4='100 BROAD ROAD APT.3'
print re.sub(r'\bROAD$', 'RD', s_4)
print re.sub(r'\bROAD\b', 'RD', s_4)
print 'test'
print ('\b')
print (r'\b')
print (r'\t')

#Example7.9
pattern="""
^            # beginning of string
M{0,3}        # thousands - 0-3 M
(CM|CD|D?C{0,3})    # hundreds - 900|400|
(XC|XL|L?X{0,3})    # tens - 90|40|
(IX|IV|V?I{0,3})    # ones - 9|4|
$            # end of string
"""

phone_pattern=re.compile(r'''
    # no need to match beginning of string
(\d{3})     # area code is 3 digits
\D*        # optional operator can be anything or nothing
(\d{3])    # next 3 digits
\D*        # optional operator
(\d[4])    # rest part of phone number
\D*        # operator
(\d*)        # optional extension
''', re.VERBOSE)
