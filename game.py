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
scr=pygame.display.set_mode((750,200),DOUBLEBUF)
scr.fill((255,255,255))
k=0
initialpos=600
k=random.randint(0,200)
cactii=[]
for t in range(2):
	a=random.randint(1,3)
	l=[0 for i in range(3)]
	for k in (len(l)):
		j=random.randint(0,1):
		if(j==1):
			l[k]=1
	cactii+=[l]
def env():
	while(1):
		for t in range(2):
			
