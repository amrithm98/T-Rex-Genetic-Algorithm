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
trw=runl.get_width()
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
class main ():
	def __init__(self):
		self.l=0
		self.h=0
		self.landx=0
		self.landy=750
		self.xshift=land1.get_width()-750-4
		self.k=0
		self.speed=20
	def run(self):
		if(self.landx>(750-land1.get_width())):
			print ("First Phase")
			pygame.draw.rect(scr,(255,255,255),(self.landx+50,200,land1.get_width(),land1.get_height()))
			scr.blit(land1,(self.landx,200))
			self.landx-=self.speed
		elif(self.landx<=-(land1.get_width()-100)):
			scr.blit(land1,(0,200))
			print ("Third phase")
			self.landx=0
		elif(self.landx<=(750-land1.get_width())):
			pygame.draw.rect(scr,(255,255,255),(self.landx+50,200,land1.get_width(),land1.get_height()))
			pygame.draw.rect(scr,(255,255,255),(self.landx+50+land1.get_width(),20,land1.get_width(),land1.get_height()))
			scr.blit(land1,(self.landx,200))
			scr.blit(land1,(self.landx+land1.get_width()-10,200))
			print("Second Phase")
			self.landx-=self.speed
		if(self.l==0):
			scr.blit(runl,(55,170))
			self.l=1
		else:
			scr.blit(runr,(55,170))
			self.l=0
		clock.tick(10)
		pygame.display.flip()
preprocess()
def game():
	test=main()
	while (1):
		test.run()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
game()
