import math
import numpy as np

class vector:
	def __init__(self,_x=0,_y=0):
		self.x = _x
		self.y = _y
		self.mag = math.sqrt(self.x**2+self.y**2)

		if self.y > 0 and self.x > 0:
			self.ang = math.atan(self.y/self.x)
		elif self.y > 0 and self.x < 0:
			self.ang = math.pi/2+math.atan(self.y/self.x)
		elif self.y < 0 and self.x < 0:
			self.ang = math.pi+math.atan(self.y/self.x)
		elif self.y < 0 and self.x > 0:
			self.ang = 3*math.pi/2 + math.atan(self.y/self.x)

	def __add__(self,vec):
		return vector(self.x+vec.x,self.y+vec.y)

	def __sub__(self,vec):
		return vector(self.x-vec.x,self.y-vec.y)

	def mul(self,other):
		return vector(self.x*other,self.y*other)
	def __mul__(self,vec):
		return vector(self.x*vec,self.y*vec)
	def __truediv__(self,vec):
		return vector(self.x/vec,self.y/vec)