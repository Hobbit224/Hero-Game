class Hero(object):
	def __init__(self, name):
		self.name = name
		self.health = 10
		self.power = 5
		self.max_health = 10
		self.xp = 0
		self.level = 1

	def cheer_hero(self):
		print "Fight hard, %s" % self.name


	# This class method returns a boolean. True if alive, false if dead
	def is_alive(self):
		return self.health > 0

	def attack(self, who_to_attack):
		who_to_attack.health -= self.power

	def health_potion(self):
		self.health += 10
		if self.health > self.max_health:
			self.health = self.max_health

	def check_level(self):
		if self.xp > 3:
			self.level = 2
			self.level_up()

	def level_up(self):
		self.max_health += 10
		self.health = self.max_health
		slef.power += 5
		print "Thou hast leveled up %s! Thy hp is now %d and they power is now %d!" % (self.name, self.max_health, self.power)

