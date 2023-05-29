import pygame
import matplotlib.pyplot as plt

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

dt = 1/30

WHITE = (255,255,255)
RED = (255,0,0)


def draw_win():
	WIN.fill(WHITE)
	pygame.display.update()

def accel(_x,_v):
	return -10*(_x-450)-1*(_v)

def get_next_v(_x,_v):
	f1 = accel(_x,_v)
	f2 = accel(_x+(dt*f1)/2,_v)
	f3 = accel(_x+(dt*f2)/2,_v)
	f4 = accel(_x+(dt*f3)/2,_v)
	return (dt*(f1+2*f2+2*f3+f4))/6

def main():
	global x,y,v,t
	global xa,va
	xa, va = [],[]
	x ,y,v= 750,250,0
	clock = pygame.time.Clock()
	run = True
	t=0

	while run:
		clock.tick(1/dt)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_win()
		v += get_next_v(x,v)
		x += v*dt
		t+=dt
		va.append(x)
		xa.append(t)
		pygame.draw.rect(WIN,RED, pygame.Rect(x,y,50,50))
		pygame.display.flip()



if __name__ == "__main__":
	main()
	plt.plot(xa,va)
	plt.show()