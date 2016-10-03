#/usr/bin/python2.7

import dot3k.joystick as j
import time
import sys
import os
import screen, backlight, ledbar, temperature, joystick

MESSAGE = screen.Screen()
TEMP =  temperature.Temperature()
LED = ledbar.LedBar)
SCROLLER = joystick.Scroller()
LIGHT =  backlight.Backlight()
INDEX = 0

@j.on(j.UP)
def handle_up(pin):
	MESSAGE.clearScreen()
	main()
	
@j.on(j.RIGHT)
def handle_right(pin):
	MESSAGE.clearScreen()
	INDEX = SCROLLER.rightSignal(INDEX)
	main()


@j.on(j.LEFT)
def handle_left(pin):
	MESSAGE.clearScreen()
	INDEX = SCROLLER.leftSignal(INDEX)
	main()

@j.on(j.DOWN)
def handle_left(pin):
	MESSAGE.clearScreen()
	LIGHT.power_off()
	os.kill()
def main():
	TEMP.readTemp()
	if INDEX >= len(TEMP.temperatures):
		INDEX = 0
	if INDEX < 0:
		INDEX = len(TEMP.temperatures) - 1
	MESSAGE.writeTemp(TEMP.temperatures[INDEX])
	LIGHT.color(float(TEMP.temperatures[INDEX]))
	LED.set_size(float(TEMP.temperatures[INDEX]))
	return

signal.pause()

if __name__ == '__main__':
	sys.ex

def main():
	TEMP.readTemp()
	if INDEX >= len(TEMP.temperatures):
		INDEX = 0
	if INDEX < 0:
		INDEX = len(TEMP.temperatures) - 1
	MESSAGE.writeTemp(TEMP.temperatures[INDEX])
	LIGHT.color(float(TEMP.temperatures[INDEX]))
	LED.set_size(float(TEMP.temperatures[INDEX]))
	return

signal.pause()

if __name__ == '__main__':
	sys.exit(main())
