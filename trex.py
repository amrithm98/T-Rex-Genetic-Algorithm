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
#	scr.blit(land1,(0,200))
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
	def run(self):
		if(self.l==0):
			scr.blit(runl,(55,167))
			self.l=1
		else:
			scr.blit(runr,(55,167))
			self.l=0
		'''
		position=land1.get_rect().move(self.k,200)
		scr.blit(land1,position)
		self.k+=land1.get_width()
		print (self.k)
		'''
		'''
				#printing land
		scr.blit(land1, (-self.landx, 200))

		#checking if land1 has shifted enough to introduce land2
		if(self.landx>=self.xshift):
			scr.blit(land1, (-self.land2x, 200))
			self.land2x+=50

		#Replacing land by land2 after checking if land has completely gone out of screen
		if(self.landx>land1.get_width()):
			self.landx=self.land2x
			self.land2x=-750
		#New land position
		self.landx+=50
		'''

		'''
		if (self.h==0):
			scr.blit(land1,(self.landx,200))
			scr.blit(land2,(self.landy,200))
			self.h=1
			self.landx-=50
			self.landy-=50
		else:
			position1=land1.get_rect().move(self.landx,200)
			position2=land2.get_rect().move(self.landy,200)
			self.landx-=50
			self.landy-=50
			scr.blit(land1,position1)
			scr.blit(land2,position2)
			if(self.landx<=(0-land1.get_width())):
				self.landx=self.landy+land2.get_width()
			elif(self.landy<=(0-land2.get_width())):
				self.landy=self.landx+land1.get_width()
		'''
		'''
		if (self.landx>=(750-land1.get_width())):
			scr.blit(land1,(self.landx,200))
			self.landx-=50
		if(self.k==0):
			scr.blit(runl,(100,100))
			self.k=1
		else:
			scr.blit(runl,(550,100))
			self.k=0
		if(self.landx>=(750-land1.get_width())):
#			pygame.draw.rect(scr,(255,255,255),(self.landx+50,200,land1.get_width(),land1.get_height()))

			scr.blit(land1,(self.landx,200))
			self.landx-=50
		elif(self.landx<=-(land1.get_width())):
			scr.blit(land1,(0,200))
			self.landx=0
		elif(self.landx<=(750-land1.get_width())):
			pygame.draw.rect(scr,(255,255,255),(self.landx+50,200,land1.get_width(),land1.get_height()))
			pygame.draw.rect(scr,(255,255,255),(self.landx+50+land1.get_width(),20,land1.get_width(),land1.get_height()))
			scr.blit(land1,(self.landx,200))
			scr.blit(land1,(self.landx+land1.get_width(),200))
			self.landx-=50
		if (self.landx<=-(750-land1.get_rect().size[0])):
			self.landx=0
		
		scr.blit(land1,(self.landx,200))
		scr.blit(land2,(self.landy,200))
		self.landx-=50
		self.landy-=50
		if self.landx==-(land1.get_rect().size[0]):
			self.landx=self.landy+land2.get_rect().size[0]
		elif self.landy==-(land2.get_rect().size[0]):
			self.landy=self.landx+land1.get_rect().size[0]
		'''
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

