from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass and implement enter()."
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()

class Death(Scene):
	quips = [ "You died. Game is over."]
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]

class CentralCorridor(Scene):
	def enter(self):
		print "The Gothons of planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapon Armory,"
		print "put it in the bridge, and below the ship after getting into an escape pod."
		print "\n"
		print "You are running down the central corrior to the Weapon Armory when "
		print "a Gothon jumps out, read scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled boty. He is blocking the door to the "
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("Please act >>")

		if action == "shoot":
			print "you are dead. He eats you."
			return 'death'

		elif action == "dodge":
			print "you are dead. The Gothon eats you."
			return 'death'

		elif action == 'tell a joke':
			print 'while he is laughing, you shoot him down'
			return 'laser_weapon_armory'

		else:
			print "DOES NOT ACCEPT"
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print "You do a drive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding."
		print "It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container.  There's a keypad lock on the box"
		print "and you need the code to get the bomb out.  If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb.  The code is 3 digits."
		
		code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]>")
		guesses = 0

		while guess != code and guesses<10:
			print "Biiiiiii!"
			guesses+=1
			guess = raw_input("[keypad]>")

		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'

		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
		
class TheBridge(Scene):
	def enter(self):
		print "You burst onto the Bridge with the netron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship.  Each of them has an even uglier"
		print "clown costume than the last.  They haven't pulled their"



class EscapePod(Scene):
	def enter(self):
		pass

class Map(object):
	def __init__(self, start_scene):
		pass
	def next_scene(self, scene_name):
		pass
	def opening_scene(self):
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
	
