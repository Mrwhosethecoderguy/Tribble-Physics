from tribble import *
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

def main():
	clock = pygame.time.Clock()
	clock.tick(1/dt)
	run = True
	t=0
	x = []
	tm = []
	pos = vector(450,250)
	spr1p = vector(450,150)
	spr2p = vector(150,250)
	spr1 = Spring(1e2,spr1p,0)
	spr2 = Spring(1e2,spr2p,0)
	circ = circle(pos,1,20,dt,s=[spr1,spr2])

	while run:
		clock.tick(1/dt)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_win()

		pygame.draw.circle(WIN,RED, (circ.pos.x,circ.pos.y), circ.r)
		pygame.draw.rect(WIN,(0,255,0),pygame.Rect(spr1p.x,spr1p.y,20,20))
		pygame.draw.rect(WIN,(0,255,0),pygame.Rect(spr2p.x,spr2p.y,20,20))
		pygame.display.flip()
		circ.update()
		x.append(circ.pos.y)
		t += dt
		tm.append(circ.pos.x)
	plt.plot(tm,x)
	plt.show()


main()
