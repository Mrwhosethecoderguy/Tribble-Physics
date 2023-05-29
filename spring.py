from vector import *
import math

class Spring:
	def __init__(self,k,pos,damp):
		self.k = k
		self.pos = pos
		self.damp = damp
	def get_force(self,pos,v):
		return vector(-self.k*(pos.x-self.pos.x)-self.damp*v.x,-self.k*(pos.y-self.pos.y)-self.damp*v.y) 

