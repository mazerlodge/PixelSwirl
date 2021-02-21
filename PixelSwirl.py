# Orignal file details follow
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example lights up the NeoPixels with a rainbow swirl.
Modified to turn lights off between color changes causing 'spin' effect
"""
import time
from adafruit_circuitplayground import cp


def wheel(pos):
	# Input a value 0 to 255 to get a color value.
	# The colours are a transition r - g - b - back to r.
	if (pos < 0) or (pos > 255):
		return (0, 0, 0)
	if pos < 85:
		return (int(pos * 3), int(255 - (pos * 3)), 0)
	if pos < 170:
		pos -= 85
		return (int(255 - pos * 3), 0, int(pos * 3))
	pos -= 170
	return (0, int(pos * 3), int(255 - pos * 3))


def rainbow_cycle(wait):
	for j in range(255):
		for i in range(cp.pixels.n):
			idx = int((i * 256 / len(cp.pixels)) + j)
			cp.pixels[i] = wheel(idx & 255)

			if (i == 1):
				print(cp.pixels[i])
			cp.pixels.show()
			time.sleep(wait)

		for i in range(cp.pixels.n):
			cp.pixels[i] = (0,0,0)
			cp.pixels.show()
			time.sleep(wait)
			
	print("rainbow done")


def qtest():
	for i in range(10):
		cp.pixels[i] = (255,0,0)
		cp.pixels.show()	
		time.sleep(0.25)
		cp.pixels[i] = (0,0,0)	
		cp.pixels.show()	
	print("qtest done")

# Main entry point
cp.pixels.auto_write = False
cp.pixels.brightness = 0.1

while True:
	qtest()
	rainbow_cycle(0.1)	
