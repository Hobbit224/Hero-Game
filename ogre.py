class Ogre(object):
	def __init__(self):
		self.health = 8
		self.power = 3
		self.name = "Ogre"
		self.xp_value = 7
		
	def is_alive(self):
		return self.health > 0
	def take_damage(self, damage):
		self.health -= damage