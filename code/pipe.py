import pygame
import random
from defs import *
from coin import Coin
pipe_img = pygame.image.load(PIPE_IMAGE_FILEPATH)

class Pipe:
	def __init__(self,x,y,screen,pipe_type):
		self.screen=screen
		self.rect = pipe_img.get_rect()
		self.state = PIPE_MOVING 
		self.type = pipe_type
		if pipe_type== PIPE_UPPER:
			y=y-self.rect.height 
		self.rect.left=x
		self.rect.top = y
		self.has_coin = False
		self.coin =0 
		self.avg_gap_y = 0 #average vertical displacement between pipes


	def update(self,dt):
		if self.state == PIPE_MOVING :
			self.move(PIPE_VELOCITY*dt)
			self.screen.blit(pipe_img, self.rect)
			self.remove_coin()
			if self.has_coin == True and self.type == PIPE_UPPER:
				self.coin.x = self.rect.centerx
				self.coin.screen.blit(self.coin.image,self.coin.rect)
				self.coin.update()
			self.update_status()

	def move(self,dx):
		self.rect.centerx += dx

	def update_status(self):
		if self.rect.right < 0:
			self.state = PIPE_OUT 

	def remove_coin(self):
		if self.has_coin == True:
			if self.coin.chosen == True:
				self.has_coin = False 
				self.coin = 0

class PipeGroup:
	def __init__(self,screen):
		self.screen = screen
		self.pipes =[]
		self.coins_collection = []

	def add_pipe_pair(self,x):
		upper_y = random.randint(PIPE_MIN_Y, PIPE_MAX_Y)
		lower_y = upper_y + random.randint(PIPE_GAP_MIN, PIPE_GAP_MAX)
		#lower_y = upper_y + PIPE_GAP
		p1=Pipe(x,upper_y,self.screen,PIPE_UPPER)
		p2=Pipe(x,lower_y,self.screen,PIPE_LOWER)
		if int(round(random.random()-SKEW,0)) ==1:
			coin_displacement = random.randint(upper_y + COIN_CLEARANCE,lower_y - COIN_CLEARANCE)
			c1=Coin(p1.rect.centerx,coin_displacement,self.screen)
			p1.has_coin = True
			p1.coin = c1
			p2.has_coin = True
			p2.coin = c1
		p1.avg_gap_y = int((upper_y+lower_y)/2)
		p2.avg_gap_y = int((upper_y+lower_y)/2)

		self.pipes.append(p1)
		self.pipes.append(p2)

	def create_new_set(self):
		self.pipes = []
		current_pipe_pos_x= INITAL_PIPE_POS_X
		self.add_pipe_pair(current_pipe_pos_x)
		while current_pipe_pos_x < DISPLAY_WIDTH :
			current_pipe_pos_x += PIPE_SPACING_X
			self.add_pipe_pair(current_pipe_pos_x)

	def update(self,dt):
		right_most =0
		for p in self.pipes:
			p.update(dt)
			if p.type == PIPE_UPPER:
				right_most = p.rect.left

		if right_most < (DISPLAY_WIDTH - PIPE_SPACING_X):
			self.add_pipe_pair(DISPLAY_WIDTH)
		self.pipes = [p for p in self.pipes if p.state == PIPE_MOVING]



	



