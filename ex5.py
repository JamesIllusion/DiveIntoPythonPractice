my_name = "Luting (aka. James) Xu"
my_age = 27 #year
my_height = 75 # inches
my_weight = 200 # pounds
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s." %my_name
print "He is %d inches tall." %my_height
print "He's %d pounds weight." %my_weight
print "He has %s hair and %s eyes." %my_hair, %my_eyes
print "And his teeth are in %s." %my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
