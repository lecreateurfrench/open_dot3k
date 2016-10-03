#/usr/bin/python2.7

import time
import screen, backlight, ledbar, temperature, joystick

def main():
	temp = temperature.Temperature()
	message = screen.Screen()
	led = ledbar.LedBar()
	scroller = joystick.Scroller()
	light = backlight.Backlight
	while True:
		temp.readTemp()
		message.writeTemp(temp.temperatures[0])
		light.color(temp.temperatures[0])
		led.set_size(temp.temperatures[0])
		time.sleep(30)
	return

if __name__ == '__main__':
	sys.exit(main())
