import pygame
from bird import Bird
from neuralnet import Nnet
import numpy as np
import random
from defs import *

class AiBird(Bird):

	def __init__(self, screen):
		super().__init__(screen)
		self.fitness = 0
		self.found_coin = False
		self.nnet = Nnet(nnet_input, nnet_hidden, nnet_output)
		

	def reset(self):
		super().reset()
		self.fitness = 0
		self.found_coin = False

	def assign_collison_fitness(self, p):
		self.fitness = -(abs(self.rect.centery - p.avg_gap_y))
		if p.has_coin ==True : 
			self.fitness -= COIN_WEIGHT*abs(self.rect.centery - p.coin.rect.centery)


	def check_hits(self, pipes):
		for p in pipes:
			if p.rect.colliderect(self.rect):
				self.state = DEAD
				self.assign_collison_fitness(p)
				break

	def update(self, dt, pipes):
		if self.state == ALIVE:
			self.time_lived += dt
			self.check_passing(pipes)
			self.move(dt)
			self.screen.blit(self.img,self.rect)
			self.check_status(pipes)
			self.check_coin()
			self.remove_coin()
			self.update_score()
		

	def get_inputs(self, pipes):
		closest = DISPLAY_WIDTH * 2
		bottom_y = 0
		coin_distance = 0
		norm_vertical_dis = 0
		coin_bird_dis = 0
		norm_coin_dis = 0
		choose_coin = False
		for p in pipes :
			if p.type == PIPE_UPPER and p.rect.right < closest and p.rect.right > self.rect.left:
				closest = p.rect.right
				dis_y = p.avg_gap_y
				if p.has_coin == True or self.found_coin:
					coin_distance = p.coin.rect.centery
					choose_coin = True
				else :
					choose_coin = False 

		horozontial_distance = closest - self.rect.centerx
		vertical_distance =  self.rect.centery - (dis_y)
		norm_vertical_dis = (((vertical_distance + Y_SHIFT) / Y_NORMALISER) * 0.99) + 0.01
		norm_coin_dis = norm_vertical_dis
		if choose_coin == True:
			coin_bird_dis =  self.rect.centery - coin_distance
			norm_coin_dis = (((vertical_distance + COIN_SHIFT ) / COIN_NORMALISER) * 0.99) + 0.01

		inputs = [
		((horozontial_distance / DISPLAY_WIDTH) * 0.99) + 0.01, norm_vertical_dis , norm_coin_dis

		]

		return inputs

	def remove_coin(self):
		if self.found_coin == True:
			if self.candidate_pipe.has_coin:
				if self.rect.left > self.candidate_pipe.coin.rect.right :
					self.candidate_pipe.coin.chosen = True


class BirdGeneration():
	def __init__(self,screen):
		self.screen = screen
		self.birds_gen = []
		self.create_new_gen()

	def create_new_gen(self):
		self.birds_gen = []
		for i in range(0,GENERATION_SIZE):
			b = AiBird(self.screen)
			self.birds_gen.append(b)
	def update(self,dt,pipes):
		num = 0
		max_score = 0
		max_coins = 0
		for b in self.birds_gen:
			if b.nnet.get_output(b.get_inputs(pipes)) > DO_JUMP:
				b.jump(dt)
			b.update(dt,pipes)
			if b.score > max_score :
				max_score = b.score 
			if b.coins > max_coins:
				max_coins = b.coins
			if b.state == ALIVE:
				num +=1
		self.num_alive = num
		return max_score,max_coins 
		#self.remove_coin()
	def get_max_score(self):
		score = 0
		for b in self.birds_gen:
			if b.score > score:
				score = b.score 
		return score 
					
		

	def get_max_score_coins(self):
		score = 0
		coins = 0
		for b in self.birds_gen:
			if b.score > score:
				score = b.score 
			if b.coins >coins :
				coins = b.coins 
		return score,coins

	def evolve_generation(self,iteration):
		for b in self.birds_gen:
			b.fitness += (b.time_lived*(-PIPE_VELOCITY) + b.coins*COINS_FACTOR)
		self.birds_gen.sort(key = lambda x:x.fitness , reverse = True)
		"""
		print('fitness for iteration #',iteration)
		for b in self.birds_gen:
			print('fitness: ', b.fitness)
			"""
		good_num = int(len(self.birds_gen)*GOOD_PERCENTAGE)
		good_birds = self.birds_gen[0:good_num]
		bad_birds = self.birds_gen[good_num:]
		bad_num = int(BAD_BUT_KEEP*len(bad_birds))

		for b in bad_birds:
			b.nnet.mutate_weights()

		taken_bad_index = np.random.choice(np.arange(len(bad_birds)),bad_num,replace = False )
		new_birdies = []

		for index in taken_bad_index:
			new_birdies.append(bad_birds[index])
		new_birdies.extend(good_birds)

		while  GENERATION_SIZE > len(new_birdies):
			parents_to_breed = np.random.choice(np.arange(len(good_birds)),2,replace = False )
			parent1 = good_birds[parents_to_breed[0]]
			parent2 = good_birds[parents_to_breed[1]]
			if parents_to_breed[0] != parents_to_breed[1]:
				child = BirdGeneration.produce_offspring(parent1,parent2,self.screen)
				new_birdies.append(child)

		for b in new_birdies:
			b.reset()
		self.birds = new_birdies



	def produce_offspring(bird1,bird2,screen):
		child = AiBird(screen)
		child.nnet.mix_weights(bird1.nnet,bird2.nnet)
		if random.random() < MUTATION_CHANCE:
			child.nnet.mutate_weights()
		return child

