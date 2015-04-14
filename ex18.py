def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r,\n arg2: %r,\n" %(arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_one(arg1):
	print "arg1: %r" %arg1

def print_none():
	print "I got nothing"

print_two("root", "shaw")
print_two_again("john", "harold")
print_one("POI")
print_none()
