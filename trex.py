import pygame
import math
import sys
import random
from pygame.locals import *

zero=pygame.image.load("0.png")
one=pygame.image.load("1.png")
two=pygame.image.load("2.png")
three=pygame.image.load("3.png")
four=pygame.image.load("4.png")
five=pygame.image.load("5.png")
six=pygame.image.load("6.png")
seven=pygame.image.load("7.png")
eight=pygame.image.load("8.png")
nine=pygame.image.load("9.png")
cactbig=pygame.image.load("cact1.png")
cactsmall=pygame.image.load("cact2.png")
cloud=pygame.image.load("cloud.png")
go=pygame.image.load("game_over.png")
land1=pygame.image.load("land.png")
land2=pygame.image.load("landx.png")
gorex=pygame.image.load("over.png")
start=pygame.image.load("start.png")
jump1=pygame.image.load("trex-jump.png")
jump2=pygame.image.load("trex-jump2.png")
runl=pygame.image.load("trex-run1.png")
runr=pygame.image.load("trex-run2.png")
pygame.init()
pygame.display.init()
scr=pygame.display.set_mode((750,240),DOUBLEBUF)
clock=pygame.time.Clock()
scr.fill((255,255,255))
score=0
speed = 5
def preprocess():
	scr.blit(land1,(0,200))
	scr.blit(runl,(55,167))
	i=random.randint(1,4)
	t=[]
	s=500
	for j in range(i):
		k=random.randint(0,1)
		if k==0:
			scr.blit(cactsmall,(s,200-(cactsmall.get_rect().size[1])+15))
			s+=cactsmall.get_rect().size[0]-2
		else:
			scr.blit(cactbig,(s,200-(cactbig.get_rect().size[1])+15))
			s+=cactbig.get_rect().size[0]-2
def gameloop():
	l=0
	while (1):
		run(l)
		if (l==0):
			l=1
		else:
			l=0
		pygame.display.update()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
def run(l):
	if(l==0):
		scr.blit(runl,(55,167))
	else:
		scr.blit(runr,(55,167))
print (runl.get_rect().size[0])
print (land1.get_rect().size[0])
print (land2.get_rect().size[0])
preprocess()
gameloop()


