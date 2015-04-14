from sys import argv

script, filename = argv

print "We are going to erase %r" %filename
print "If you dont want that, hit CTRL-C (^C)"
print "If you want that, hit RETURN"

raw_input("??")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Bye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line_1, ")
line2 = raw_input("Line_2, ")
line3 = raw_input("Line_3, ")

print "I'm going to write these the file."

target.write(line1)
target.write(line2)
target.write(line3)

print "And finally, we close it."
target.close()
