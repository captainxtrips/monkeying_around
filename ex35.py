#from sys import exit, argv
from random import randint

#WELCOME TO MONKEYING AROUND

#script, userfile = argv

testBool = False

def final_room():
	print """Congratulations, dick- I mean, %s. Few make it this far.\n
	You are now faced with an impossible decision:\n
	You, poor soul, must choose between saving your family\n 
	from certain death, and owning a brand new pair of\n 
	Yeezies by Kanye West in the style and color of your\n
	choosing. Go now, and destroy your life, one way or another. \n \n
	""" % username
	
	while True:

		ultAns = raw_input(""""
			\tPress the '1' key to save your family \n\tOR \n 
			\tPress the '0' key to choose the Yeezies \n \n >>
			""")

		if "1" in ultAns:
			print """
			You have been noble, and your family will \n
			be spared, but at what cost? The Yeezies \n
			are now forever out of reach. They will \n
			haunt you until the day you die. \n \n
			"""
			testBool1 = True
			

		elif "0" in ultAns:
			print """
			You have done the unthinkable, %s. Your family is dead. \n
			The precious Yeezies by Kanye West are now yours, in the style 
			and color of your choosing. Know in your heart that you have \n
			made the right choice.
			""" % username
			testBool2 = True
			

		else:
			rip_in_piece ("""You had two choices, dipshit. Now your family is getting \n
			killed, AND you have no Yeezies to show for it. \n
			You stupid asshole...
			""")

def chimp_room():
	print """
	You find yourself in a room full of sleeping chimpanzees. \n
	They are not yet alerted to your presence among them. You see \n
	two possible routes to reach an unlocked door on the other side of \n
	the room. \n \n
	\tThe first route is across creaky, unstable wood. You might be able \n
	\tmake it across if you go tread slowly and are careful not to make \n
	too much noise. \n \n
	\tThe second route is loose dirt, riddled with puddles of what appears \n
	\tbe water. How do you proceed, asshole? \n \n
	"""

	chimpAns = raw_input("""
		\t\tPress the '1' key to walk across the wood.\n
		\t\tPress the '2' to walk in the mud. \n\n >>
		""")

	print "\n\n"

	if "2" in chimpAns:
		print "You made it through the dirt, but now your shoes are all muddy."
		testBool1 = True
		final_room()

	elif "1" in chimpAns:
		print """
		You made it about 3 steps toward the door before being brutally \n
		ripped apart and eaten alive by the hoard of primates.
		"""
		testBool2 = True
		rip_in_piece()

	else:
		rip_in_piece("""
			Good going, moron. You managed to fuck up while answering a\n
			binary question.
			""")

def gorilla_room():
	print "You enter to find a single, large silverback gorilla \n",
	"sleeping in the center of the room. There's a gun off to the \n",
	"side with six bullets in it. You're a terrible shot, so each \n",
	"bullet only has a 10%% chance of hitting the target. In order to \n",
	"kill the gorilla, your shots must connect at least six times. The first \n",
	"shot will awaken the beast, so if you don't kill him, he'll kill you.\n\n",


	ready = raw_input("\tPRESS ENTER TO EMPTY YOUR MAGAZINE INTO THIS BIG UGLY FUCK")
	
	gorillaChance = randint(0,9)
	gorillaChanceList = [0, 2, 3, 4, 5, 6]
	shotHit = 0

	for i in gorillaChanceList:
		if gorillaChance > 5:
			print "HIT \n"
			shotHit += 1

		elif gorillaChance < 6:
			print "MISS \n"

		else:
			print "BROKEN CODE"
			exit()
	if shotHit >= 6:
		print "You killed the gorilla, and may pass safely into the next room"
		testbool = True
		final_room()
		
	elif shotHit < 6:
		print "You fucked up, you blind idiot. You're now a dead man."
		testbool = True
		rip_in_piece("You couldn't fucking shoot a giant gorilla at point",
			" blank range.")

	else:
		print "BROKEN CODE"
		exit()

def rip_in_piece(reason):
	print "Well, you've done it. You went and killed yourself, %s" % username
	print "It looks like you've succumb to %s" % reason
	print "\nWould you like to play again?"

	playAgain = raw_input ("Press the 'Enter' key to play again,",
		" or press exit the terminal to quit")

	start()

def start():
	print "You find yourself in an unfamiliar room.",
	"You see two doors in front of you. One says 'G'",
	"and the other says 'C'\n"

	print "You must choose which door you will open, %s." % username

	startAns = raw_input ("""
		\n\t\tEnter the 'G' key for the first door
		or end the 'C' key for the second door
		"""
		)

	if 'G' in startAns:
		print "You go inside the door marked 'G'"
		print """
		.........
		.........
		.........
		.........
		"""
		gorilla_room()

	elif 'C' in startAns:
		print "You go inside the door marked 'C'"
		print """
		.........
		.........
		.........
		.........
		"""
		chimp_room()
	
	else:
		print "BROKEN CODE"

username = raw_input("What do I call you?\n>>")

start()
