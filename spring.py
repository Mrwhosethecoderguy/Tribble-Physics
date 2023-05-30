from vector import *
import math

class Spring:
	def __init__(self,k,l,pos,damp):
		self.k = k
		self.l = l
		self.pos = pos
		self.damp = damp
	def get_force(self,pos,v):
		v_eff = None
		if v.ang >= math.pi:
			v_eff = -v.mag
		else:
			v_eff = v.mag
		f_mag = -self.k*(self.get_dist(pos))-self.damp*v_eff
		ang = None
		try:
			ang = math.atan((pos.y-self.pos.y)/(pos.x-self.pos.x))
		except:
			ang = math.pi/2
		f = vector(f_mag*math.cos(ang),f_mag*math.sin(ang))
		return f

	def get_dist(self,pos):
		dist = math.sqrt((pos.x-self.pos.x)**2+(pos.y-self.pos.y)**2)
		if pos.x < self.pos.x:
			return -dist
		elif pos.y < self.pos.y:
			return -dist
		else:
			return dist
