import pygame
import sys
from defs import *

class Button:
	def __init__(self,text,x,y,font):
		self.text = text
		self.x = x
		self.y=y
		self.font = font
		self.text_img=self.font.render(self.text,True,"black",(0,200,200))
		self.rect = self.text_img.get_rect(center=(self.x,self.y))

	def update(self,screen):
		screen.blit(self.text_img,self.rect)

	def changeColor(self,pos):
		if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom) :
			self.text_img=self.font.render(self.text,True,"yellow",(0,200,200))
		else:
			self.text_img=self.font.render(self.text,True,"black",(0,200,200))

	def isPressed(self,pos):
		if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom) :
			return True
		else:
			return False 


