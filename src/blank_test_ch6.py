'''
Created on 2015-08-25

@author: James

blank_test_ch6
'''
#Example 6.2
from getpass import win_getpass, unix_getpass
#Bind the name getpass to the appropriate function

try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
             from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
            print "default"
        else:
            getpass = AskPassword
            print "Mac"
    else:
        getpass = win_getpass
        print "Windows"
else:
    getpass = unix_getpass
    print "Unix"
    

#Example 6.3 / 6.4 / 6.5 / 6.6 / 6.7
tmp_file=open('blank_test_ch6.txt', 'rb')
print tmp_file
print tmp_file.mode
print tmp_file.name
print
print tmp_file.tell()
print tmp_file.seek(0)
print
print tmp_file.closed
tmp_file.close()
print tmp_file
print tmp_file.closed
#print tmp_file.seek(0)
print
tmp_file=open('blank_test_ch6.txt', 'w')
tmp_file.write('Hello there, this is written using Python, file open function, in write mode')
tmp_file.close()
print file('blank_test_ch6.txt').read()
print '--------THIS IS THE GAP BETWEEN WRITE MODE AND APPEND MODE--------'
tmp_file=open('blank_test_ch6.txt', 'a')
tmp_file.write('\nHi again, this time, we are using append mode')
tmp_file.close()
print file('blank_test_ch6.txt').read()

#Example 6.12
print
import sys
print '\t'.join(sys.modules.keys())