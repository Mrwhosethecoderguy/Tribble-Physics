from vector import *
from spring import *

class circle:
	def __init__(self,pos,mass,r,dt,ang_mom=vector(0,0),mom=vector(0,0),**kwargs):
		self.pos = pos
		self.ang_mom = ang_mom
		self.mom = mom
		self.mass = mass
		self.r = r
		self.attach = None
		self.dt = dt
		self.v = vector(mom.x/mass,mom.y/mass)
		for i in range(len(kwargs)):
			try:
				self.attach = kwargs['a']
			except:
				try:
					self.attach = kwargs["attach"]
				except:
					pass
	def get_next_v(self,spr):
		f1 = spr.get_force(self.pos,self.v)/self.mass
		f2 = spr.get_force(self.pos+(f1.mul(self.dt))/2,self.v)/self.mass
		f3 = spr.get_force(self.pos+(f2.mul(self.dt))/2,self.v)/self.mass
		f4 = spr.get_force(self.pos+(f3.mul(self.dt))/2,self.v)/self.mass
		return ((f1+f2.mul(2)+f3.mul(2)+f4).mul(self.dt))/6

	def update(self):
		if self.attach != None:
			for i in range(len(self.attach)):
				self.v += self.get_next_v(self.attach[i])
				self.pos += self.v.mul(self.dt)






