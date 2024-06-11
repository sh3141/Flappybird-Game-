import pygame
from defs import *
coin1_img =  pygame.image.load(COIN_GOLD1_IMG_FILEPATH)
coin2_img =  pygame.image.load(COIN_GOLD2_IMG_FILEPATH)
coin3_img =  pygame.image.load(COIN_GOLD3_IMG_FILEPATH)
coin4_img =  pygame.image.load(COIN_GOLD4_IMG_FILEPATH)
coin5_img =  pygame.image.load(COIN_GOLD5_IMG_FILEPATH)
coin6_img =  pygame.image.load(COIN_GOLD6_IMG_FILEPATH)

coins =[coin1_img,coin2_img,coin3_img,coin4_img,coin5_img,coin6_img]
class Coin:
	def __init__(self,x,y,screen):
		self.x=x
		self.y=y
		self.screen = screen
		self.index =0
		self.image = coins[self.index]
		self.rect = self.image.get_rect()
		self.rect.centerx=self.x
		self.rect.centery=y
		self.chosen = False
		self.moved = False

	def update(self):
		self.index +=1
		if self.index ==6:
			self.index =0
		self.image = coins[self.index]
		self.rect = self.image.get_rect()
		self.rect.centerx=self.x
		self.rect.centery=self.y

	def move(self,dx):
		self.x+=dx
		self.rect.centerx = self.x
