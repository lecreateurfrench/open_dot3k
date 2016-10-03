#/usr/bin/python2.7

import dot3k.backlight as backlight

class Backlight():

	def __init__(self):
		self.maxtemp = 50.0
		self.mintemp = 0.0
		self.step = 255.0 / (self.maxtemp - self.mintemp)/2

	def color(self, temp):
		increment = int(temp) * int(self.step)
		try: 
			if temp <= 25:
				green = 0 + increment
				blue = 255 - increment
				red = 0
				backlight.rgb(red, green, blue)
			elif temp > 25:
				green = 255 - increment
				red = 0 + increment
				blue = 0
				backlight(red, green, blue)
		except:
			backlight(255, 255, 255)

