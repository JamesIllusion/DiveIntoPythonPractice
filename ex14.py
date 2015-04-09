from sys import argv

script, user_name = argv
prompt = '>'

print "HI %s, I'm %s script." %(user_name, script)
print "I have questions for you."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print "You said %r about liking me. And you are living in %r, with a %r computer" %(likes, lives, computer)
