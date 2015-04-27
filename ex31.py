print "You enter a dark room with two doors, which door do you choose?"

door = raw_input(">")

if door == "1":
	print "There is a giant bear eating a cheese cake. what do you do?"
	print "1. Take the cake"
	print "2. sceam at the bear."

	bear = raw_input(">")

	if bear == "1":
		print "The bear eats your face off. Game over"
	elif bear == '2':
		print "The bear eats your legs off. Game over"
	else:
		print "Sorry, there is not choice. LoL"

elif door =="2":
	print "You stare into the endless abyss."
	print "1. blurberries"
	print "2. yellow jacket clothespins"
	print "3. understaning revolvers yelling melodies"

	insanity = raw_input(">")

	if instanity == "1" or instanity == "2":
		print "Your body survives, good job"
	else:
		print "The insanity rots your eyes, good job"

else:
	print "You stubble around then fall on a knife and die"
