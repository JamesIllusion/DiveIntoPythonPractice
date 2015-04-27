def add(a,b):
	print "ADD %d + %d" %(a,b)
	return a+b

def minus(a,b):
	print "%d MINUS - %d" %(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLY %d * %d" %(a,b)
	return a*b

def divide(a,b):
	print "DIVIDE %d / %d" %(a,b)
	return a/b

print "Let's do some math"

age = add(20,7)
height = minus(200, 10)
weight = multiply(9,10)
IQ = divide(200,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, IQ)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, minus(height, multiply(weight, divide(IQ, 2))))

print "That becomes: ", what, "Can you do it by hand?"
