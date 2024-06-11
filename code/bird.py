import pygame
from defs import *
bird_img =  pygame.image.load(BIRD_IMAGE_FILEPATH)
class Bird:
	def __init__(self,screen):
		self.screen = screen 
		self.img = bird_img
		self.rect = bird_img.get_rect()
		self.rect.centerx=BIRD_INIT_POS_X
		self.rect.centery=BIRD_INIT_POS_Y
		self.state =ALIVE
		self.speed_y = 0
		self.score = 0
		self.time_lived = 0
		self.coins = 0
		self.within_pipe_gap = False
		self.candidate_pipe = 0 #pipe the bird is about to pass through

	def move(self,dt):
		bird_y_displacement = self.speed_y*dt+0.5*g*dt*dt
		self.speed_y += g*dt
		self.rect.centery += bird_y_displacement
		if self.rect.top < 0 :
			self.rect.top = 0 
			self.speed_y = 0


	def update(self,dt,pipes):
		if self.state == ALIVE :
			self.time_lived += dt
			self.check_passing(pipes)
			self.move(dt)
			self.screen.blit(bird_img,self.rect)
			self.check_status(pipes)
			self.check_coin()
			self.update_score()
		

	def jump(self,dt):
		self.speed_y = BIRD_SPEED_Y 

	def reset(self):
		self.state = ALIVE
		self.rect.centerx=BIRD_INIT_POS_Y
		self.rect.centery=BIRD_INIT_POS_X
		self.speed_y = 0
		self.score = 0
		self.coins = 0
		self.time_lived = 0
		self.candidate_pipe = 0
		self.within_pipe_gap = False

	def check_collision(self,pipes):
		for p in pipes :
			if p.rect.colliderect(self.rect):
				self.state = DEAD
			

	def check_status(self,pipes):
		if self.rect.bottom > DISPLAY_HEIGHT:
			self.state = DEAD
		else :
			self.check_collision(pipes)

	def check_passing(self,pipes):

		if self.within_pipe_gap  == False:
			for p in pipes:
				if self.rect.right in range(p.rect.left,p.rect.right):
					self.candidate_pipe = p
					self.within_pipe_gap  = True 
					return p
			self.candidate_pipe = 0
			return 0
		return 0

	def check_coin(self):
		if self.within_pipe_gap == True and self.candidate_pipe.has_coin == True:
			if self.rect.colliderect(self.candidate_pipe.coin.rect):
				self.coins +=1
				self.candidate_pipe.coin.chosen = True

	def update_score(self):
		if self.within_pipe_gap == True and self.rect.left > self.candidate_pipe.rect.right:
			self.score +=1
			self.within_pipe_gap = False

				
