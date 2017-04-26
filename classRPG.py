from hero import Hero
from goblin import Goblin
from vampire import Vampire
from ogre import Ogre





startup = True
while startup == True:
	new_game = raw_input("Start a new game? Y/N \n")
	if new_game == "Y":
		print "Splendid! I wish thee well on thy quest.\n"
		startup = False
	elif new_game == "N":
		print "What a shame. Perhaps one day thou wilst become a hero.\n"
		
	else:
		print "That is not a valid input.\n"

hero_name = raw_input("What is thy name, bold adventurer? \n")
the_hero = Hero(hero_name)
hero_home = raw_input("Whence dost thou hail, brave %s? \n") % the_hero.name

print "Well, %s of %s, I hope you are prepared. \n" % (the_hero.name, the_hero.home)


monsters = []
monsters.append(Goblin())
monsters.append(Vampire())
monsters.append(Ogre())


for monster in monsters:
#	 print "1. 1 enemy"
#	 print "2. 2 enemies"
#	 print "3. 3 enemies"
#	 enemies_num = raw_input("How many enemies do you want to fight? ")
#	 if enemies_num == "1":
#	 	monsters[0]

	print "\n"
	print "Mighty hero %s, you have encountered a %s. \n" % (the_hero.name, monster.name)
	if monster == Ogre:
		monster.ogre_cry()
	while monster.health > 0 and the_hero.is_alive():
	 		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	 		print "The %s has %d health and %d power.\n" % (monster.name, monster.health, monster.power)
	 		print "What do you want to do?" 
	 		print "1. fight %s" % (monster.name)
	 		print "2. do nothing"
	 		print "3. flee"
	 		print "4. drink potion of life"
	 		print "> ",
	 		print "\n"
	 		user_input = raw_input()

	 		if user_input == "1":
	 			# the_goblin.health -= the_hero.power

	 			the_hero.attack(monster)

	 			print "You did %d damage.\n" % (the_hero.power)
	 			if monster.health <= 0:
	 				print "You killed the %s!\n" % monster.name
	 				the_hero.xp += monster.xp_value
	 				the_hero.check_level
	 		elif user_input == "2":
	 			print "You do nothing." 

			elif user_input == "3":
				print "Goodbye, coward."
				break
			elif user_input == "4":
				the_hero.health_potion()
				print "You healed yourself"
			else: 
				print "Invalid input %s." % user_input

			if monster.health > 0:
				# hero has attacked and goblin is still alive
				the_hero.health -= monster.power
				print "The %s hits you for %d damage" % (monster.name, monster.power) + "."
				if the_hero.health <= 0:
					print "You are dead."
					break 
			if the_hero.health > 0 and the_hero.health < 5:
				print "You have gone into a rage. Your power has increased!"
				the_hero.power += 5