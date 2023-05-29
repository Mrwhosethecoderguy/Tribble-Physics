class Spring:
	def __init__(k,l,damp,x=0)
		self.k = k
		self.l = l
		self.x = x
		self.damp = damp
	def get_force(self,v):
		return -k*x-damp*v 
