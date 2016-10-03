#/usr/bin/python2.7


import dot3k.joystick as j


class Scroller():
	
	def __init__(self):
		self.scrollnum = 0
		return

	@j.on(j.RIGHT)
	def handle_right(self, pin):
		self.scrollnum += 1

	@j.on(j.LEFT)
	def handle_left(self, pin):
		self.scrollnum -= 1


