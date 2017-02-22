import pygame
import math
import sys
import random
from pygame.locals import *
import time

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
scr.fill((255,255,255))
clock=pygame.time.Clock()
def land(x,y):
	scr.blit(land1,(x,200))
	scr.blit(land1,(y,200))
def cactus(cac):
	for t in range(len(cac)):
		a=cac[t][0]
		b=cac[t][1]
		start=a
		for i in b:
			if(i==1):
				scr.blit(cactbig,(start,200-cactbig.get_height()+20))
				start+=cactbig.get_width()-5
			else:
				scr.blit(cactsmall,(start,200-cactsmall.get_height()+20))
				start+=cactsmall.get_width()-5
def collision(x,y,cac):
	if(cac[0][0]<5):
		a=cac[1][0]
		b=cac[1][1]
	else:
		a=cac[0][0]
		b=cac[0][0]
class trex():
	def __init__(self):
		self.l=0
		self.x=0
		self.y=land1.get_width()-10
		self.posx=85
		self.t=0
		self.posy=200-runl.get_height()+25
		p=random.randint(1,3)
		s=[0 for i in range (p)]
		for j in range(len(s)):
			y=random.randint(0,1)
			if(y==1):
				s[j]=1
		self.cactii=[[600,s]]
		r=random.randint(0,225)
		p=random.randint(1,3)
		s=[0 for i in range(p)]
		for j in range(len(s)):
			y=random.randint(0,1)
			if(y==1):
				s[j]=1
		u=len(self.cactii)
		self.cactii+=[[(self.cactii[u-1][0]+225+r),(s)]]
	def jump(self):
		while(1):	
			scr.fill((255,255,255))
			land(self.x,self.y)
			self.x-=20
			self.y-=20
			print (self.posy)
			if(self.x>self.y):
				if(self.y<=-(land1.get_width())):
					self.y=self.x+land1.get_width()-15
			else:
				if(self.x<=-(land1.get_width())):
					self.x=self.y+land1.get_width()-15
			cactus(self.cactii)
			for j in range(len(self.cactii)):
				self.cactii[j][0]-=20
			if(self.cactii[0][0]<-50):
				del self.cactii[0]
			if(self.cactii[-1][0]<740):
				r=random.randint(0,225)
				p=random.randint(1,3)
				s=[0 for i in range(p)]
				for u in range(len(s)):
					y=random.randint(0,1)
					if(y==1):
						s[u]=1
				n=len(self.cactii)
				self.cactii+=[[(self.cactii[n-1][0]+225+r),s]]
			if(self.l==0):
				scr.blit(runl,(self.posx,self.posy))
				self.l=1
			else:
				scr.blit(runr,(self.posx,self.posy))
				self.l=0
			#clock.tick(10000)
#			pygame.display.flip()
#			pygame.display.flip()
			if(self.posy<=(200-cactbig.get_height()+20-15)/1.25) or (self.t==1):
				self.posy+=10
				self.t=1
				print ("Incrementing posy")
			else:
				self.posy-=10
				print("Decrementing posy")
			if(self.posy>=(200-runl.get_height()+25)):
				self.posy=200-runl.get_height()+25
				print ("Breaking out of the loop")
				self.t=0
				break
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					quit()
			collision(self.x,self.y,self.cactii)
			clock.tick(22)
			pygame.display.update()
	def run(self):
		scr.fill((255,255,255))
		land(self.x,self.y)
		self.x-=20
		self.y-=20
		if(self.x>self.y):
			if(self.y<=-(land1.get_width())):
				self.y=self.x+land1.get_width()-15
		else:
			if(self.x<=-(land1.get_width())):
				self.x=self.y+land1.get_width()-15
		if(self.l==0):
			scr.blit(runl,(self.posx,self.posy))
			self.l=1
		else:
			scr.blit(runr,(self.posx,self.posy))
			self.l=0
		cactus(self.cactii)
		for j in range(len(self.cactii)):
			self.cactii[j][0]-=20
		if(self.cactii[0][0]<-50):
			del self.cactii[0]
		if(self.cactii[-1][0]<740):
			r=random.randint(0,225)
			p=random.randint(1,3)
			s=[0 for i in range(p)]
			for u in range(len(s)):
				y=random.randint(0,1)
				if(y==1):
					s[u]=1
			n=len(self.cactii)
			self.cactii+=[[(self.cactii[n-1][0]+225+r),s]]
		collision(self.x,self.y,self.cactii)
		clock.tick(20)
		pygame.display.flip()
def startgame():
	t=trex()
	z=0
	while (1):
		for event in pygame.event.get():
			if event.type==KEYDOWN:
				print ("event occured")
				if event.key==K_SPACE or event.key==K_UP: 
					print ("space entered")
					t.jump()
			elif event.type==pygame.QUIT:
				pygame.quit()
				quit()
		t.run()
startgame()