#/usr/bin/python2.7


import dot3k.joystick as j


class Scroller():
	
	def __init__(self):
		return

	def rightSignal(self, index):
		index += 1
		return index

	def leftSignal(self, index):
		index -= 1
		return index


