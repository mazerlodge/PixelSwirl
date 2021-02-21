#!/bin/python3 

# imports 

# globals 


# class 
class Qed:

	# member vars 
	isitlocal = 0
	cpPixelsCount = 10
	cpPixels = [] 

	def __init__(self, parms): 
		# do something 
		self.isitlocal = parms
		self.showLocal()
		self.initPixelsArray()
		self.showPixelsArray()
		
	def initPixelsArray(self):
		for i in range(self.cpPixelsCount): 	
			self.cpPixels.append((0,0,0))
			
	def showPixelsArray(self): 
		for i in range(self.cpPixelsCount): 	
			print(self.cpPixels[i])

	def wheel(self, pos):
		# Input a value 0 to 255 to get a color value.
		# The colors are a transition r - g - b - back to r.
		
		# This doesn't happen, just a safety valve.
		if (pos < 0) or (pos > 255):
			return (0, 0, 0)
			
		if pos < 85:
			return (int(pos * 3), int(255 - (pos * 3)), 0)

		if pos < 170:
			pos -= 85
			return (int(255 - pos * 3), 0, int(pos * 3))

		pos -= 170

		return (0, int(pos * 3), int(255 - pos * 3))
	
	
	def rainbowCycle(self, wait):
		for j in range(255):
			for i in range(self.cpPixelsCount):
				idx = int((i * 256 / len(self.cpPixels)) + j)
				print("av = %d yields %s" % ((idx & 255), self.wheel(idx & 255)))
				self.cpPixels[i] = self.wheel(idx & 255)
				
	def showLocal(self): 
		print("isitlocal = %d" % self.isitlocal) 


# entry point 
qe = Qed(42) 
qe.showLocal()
qe.rainbowCycle(42)
qe.showPixelsArray()
