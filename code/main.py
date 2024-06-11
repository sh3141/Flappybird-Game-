import pygame,sys
from defs import *
from button import Button
from pipe import PipeGroup
from bird import Bird
from birdai import BirdGeneration
from neuralnet import Nnet 
import numpy as np
import random, time

pygame.init()
screen= pygame.display.set_mode((DISPLAY_WIDTH ,DISPLAY_HEIGHT)) 
surface = pygame.Surface((DISPLAY_WIDTH,DISPLAY_HEIGHT),pygame.SRCALPHA)
#quit_screen = pygame.display.set_mode((QUIT_DISPLAY_WIDTH,QUIT_DISPLAY_HEIGHT))
background_img =  pygame.image.load(BG_IMAGE_FILEPATH)
clock = pygame.time.Clock()
with open(TUTORIAL_TEXT_FILEPATH,'r') as tutorial_file:
	tutorial_lines = tutorial_file.readlines()
tutorial_lines = [lines.strip() for lines in tutorial_lines]


def draw_text(text, font, text_col, x,y):
	text_img=font.render(text,True,text_col)
	screen.blit(text_img,(x,y))
	text_rect = text_img.get_rect()
	return text_rect.width

def update_label(game_time,score,coins):
	font = pygame.font.SysFont("cambria",20)
	pos = 25
	label_width = draw_text("Game Time: ",font,"black",pos,25)
	pos +=label_width + 5
	label_width = draw_text(str(game_time/1000),font,"black",pos,25)
	pos +=label_width 
	draw_text(" s",font,"black",pos,25)
	draw_text("Score: ",font,"black",25,50)
	draw_text(str(score),font,"black",85,50)
	draw_text("Coins: ",font,"black",25,75)
	draw_text(str(coins),font,"black",85,75)

def update_labelai(respects_paid,generation,num_alive,highest_score):
	font=pygame.font.SysFont("cambria",20)
	draw_text("respects paid: ",font,"black",25,100)
	draw_text(str(respects_paid),font,"black",150,100)
	draw_text("Gen: ",font,"black",25,125)
	draw_text(str(generation),font,"black",85,125)
	draw_text("Alive: ",font,"black",25,150)
	draw_text(str(num_alive),font,"black",85,150)
	draw_text("high score: ",font,"black",25,175)
	draw_text(str(highest_score/1000),font,"black",150,175)

def run_main_menu():
	
	pygame.display.set_caption('Flappy Bird - Main menu')
	
	run = True
	screen_no=0
	status =1
	font=pygame.font.SysFont(MAIN_MENU_FONT_TYPE,MAIN_MENU_FONT_SIZE)
	font = pygame.font.SysFont("cambria",50)
	manual_button = Button("Manual",480,150,font)
	ai_button =Button("AI",480,250,font)
	tutorial_button = Button("Tutorial",480,350,font)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_t:
					tutorial_button.changeColor([tutorial_button.rect.centerx,tutorial_button.rect.centery])
					tutorial_button.update(screen)
					status = run_tutorial()
				elif event.key ==pygame.K_a:
					ai_button.changeColor([ai_button.rect.centerx,ai_button.rect.centery])
					ai_button.update(screen)
					status = run_ai()
				elif event.key == pygame.K_m:
					manual_button.changeColor([manual_button.rect.centerx,manual_button.rect.centery])
					manual_button.update(screen)
					status = run_manual()
				else:
					run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if manual_button.isPressed(pygame.mouse.get_pos()) == True:
					status = run_manual()
				elif ai_button.isPressed(pygame.mouse.get_pos()) == True:
					status = run_ai()
				elif tutorial_button.isPressed(pygame.mouse.get_pos()) == True:
					status = run_tutorial()
		if status == QUIT :
			run = False
		screen.blit(background_img, (0, 0))
		draw_text("Flappy Bird 101!!",font,MAIN_MENU_FONT_COLOUR,275,50)
		for button in [manual_button,ai_button,tutorial_button]:
			button.changeColor(pygame.mouse.get_pos())
			button.update(screen)
		pygame.display.update()

def draw_pause_screen(game_time,score,coins_collected,pause_reason):

	game_stats = [game_time/1000,score,coins_collected]
	game_stats_labels = ["Game Time: ","Score: ","Coins: "]
	font = pygame.font.SysFont("cambria",50)
	font_button = pygame.font.SysFont("cambria",25)
	return_button = Button("Return to main menu",480,150,font_button)
	restart_button = Button("Restart",480,200,font_button)
	quit_button = Button("Quit",480,250,font_button)
	continue_button = Button("Continue",480,300,font_button)
	if pause_reason == PAUSE:
		draw_text("Game paused",font,(0,250,250),330,50)
	else:
		draw_text("lol you lost !! how embarrasing",font,(0,250,250),200,50)
	pygame.draw.rect(surface, (100,100,100,10),[0,0,DISPLAY_WIDTH,DISPLAY_HEIGHT])
	screen.blit(surface,(0,0))
	index = 0
	for button in [restart_button,return_button,quit_button,continue_button]:
		if index ==3 and pause_reason == LOST :
			break
		button.changeColor(pygame.mouse.get_pos())
		button.update(screen)
		index +=1
	font_stats = pygame.font.SysFont("cambria",30)
	stat_label_x = 200
	if pause_reason == PAUSE:
		stat_label_y = 340
	else:
		stat_label_y = 290
	for i in range(0,3):
		label_witdth = draw_text(game_stats_labels[i],font_stats,(0,200,200),stat_label_x,stat_label_y)
		stat_label_x += label_witdth+LABEL_DATA_OFFSET
		label_witdth = draw_text(str(game_stats[i]),font_stats,"black",stat_label_x,stat_label_y)
		stat_label_x +=LABEL_OFFSET +label_witdth
	if pause_reason == PAUSE:
		return restart_button,return_button,quit_button,continue_button
	else:
		return restart_button,return_button,quit_button


def run_tutorial():
	pygame.display.set_caption('tutorial')
	screen.fill("black")
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return QUIT
			elif event.type == pygame.KEYDOWN:
				pygame.display.set_caption('Flappy Bird - Main menu')
				return RETURN_TO_MAIN_MENU		
		font = pygame.font.SysFont("arial",25)
		start_pos_y = 25
		for i in range(0,len(tutorial_lines)):
			draw_text(tutorial_lines[i], font, "white",25,start_pos_y)
			start_pos_y += 27
		pygame.display.update()
	pygame.display.set_caption('Flappy Bird - Main menu')
	return RETURN_TO_MAIN_MENU

def run_manual():
	game_time=0
	pygame.display.set_caption('Manual')
	run = True
	pause = False
	lost = False
	first_tick = True #flag to ignore the first tick
	return_pause_status = RESUME
	pipe_collection = PipeGroup(screen)
	pipe_collection.create_new_set()
	birdie_boi = Bird(screen)
	clock = pygame.time.Clock()
	dt=0
	while run:
		return_pause_status = RESUME
		dt = clock.tick(FPS)
		if first_tick:
			dt = 0
			first_tick = False 
			
		if not pause and not lost:
			game_time +=dt
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return QUIT
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not pause and not lost:
					birdie_boi.jump(dt)
				elif event.key == pygame.K_ESCAPE and not lost:
					if pause :
						pygame.display.set_caption('Manual')
					else :
						pygame.display.set_caption('Manual - paused')
					pause = not pause
			elif event.type == pygame.MOUSEBUTTONDOWN and (pause or lost):
				if return_button.isPressed(pygame.mouse.get_pos()) == True:
					pygame.display.set_caption('Flappy Bird - Main menu')
					return RETURN_TO_MAIN_MENU
				elif restart_button.isPressed(pygame.mouse.get_pos()) == True:
					pygame.display.set_caption('Manual')
					return_pause_status = RESTART
					pause = False
					lost = False
				elif quit_button.isPressed(pygame.mouse.get_pos()) == True:
					pygame.display.set_caption('Flappy Bird - Main menu')
					return QUIT
				elif continue_button.isPressed(pygame.mouse.get_pos()) == True:
					pygame.display.set_caption('Manual')
					return_pause_status = RESUME
					pause = False

		if not pause and not lost:
			screen.blit(background_img,(0,0))
			pipe_collection.update(dt)
			birdie_boi.update(dt,pipe_collection.pipes)

			if return_pause_status == RESTART:
				birdie_boi.reset()
				pipe_collection = PipeGroup(screen)
				pipe_collection.create_new_set()
				game_time =0

			if birdie_boi.state == DEAD:
				lost = True 
			update_label(game_time,birdie_boi.score,birdie_boi.coins)
		elif pause:
			restart_button,return_button,quit_button,continue_button = draw_pause_screen(game_time,birdie_boi.score,birdie_boi.coins,PAUSE)
		else:
			restart_button,return_button,quit_button = draw_pause_screen(game_time,birdie_boi.score,birdie_boi.coins,LOST)

		pygame.display.update()
	pygame.display.set_caption('Flappy Bird - Main menu')
	return RETURN_TO_MAIN_MENU

def run_ai():
	pygame.display.set_caption('ai')
	pipe_collection = PipeGroup(screen)
	pipe_collection.create_new_set()
	game_time =0
	coins = 0
	score = 0
	respects_paid = 0
	generation = 1
	highest_score = 0
	first_tick = True #flag to ignore the first tick
	run = True
	birds = BirdGeneration(screen)
	clock = pygame.time.Clock()
	dt=0
	while run:
		dt = clock.tick(FPS)
		"""
		if first_tick:
			dt = 0
			first_tick = False 
			"""
		game_time +=dt
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return QUIT
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					respects_paid += 1
				else:
					pygame.display.set_caption('Flappy Bird - Main menu')
					return RETURN_TO_MAIN_MENU
		screen.blit(background_img,(0,0))
		pipe_collection.update(dt)
		score,coins = birds.update(dt,pipe_collection.pipes)
		
		if birds.num_alive == 0:
			
			pipe_collection.create_new_set()
			birds.evolve_generation(generation)
			generation +=1
			if game_time > highest_score:
				highest_score = game_time
			game_time = 0
			coins = 0
			score = 0
		update_label(game_time,score,coins)
		update_labelai(respects_paid,generation,birds.num_alive,highest_score)
		
		
		pygame.display.update()
	pygame.display.set_caption('Flappy Bird - Main menu')
	return RETURN_TO_MAIN_MENU


if __name__ == "__main__" :
	run_main_menu()
