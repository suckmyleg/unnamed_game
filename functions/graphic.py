import pygame

class Graphic:
	def __init__(self):
		self.width = 500
		self.height = 500

	def start(self):
		pygame.init()
		pygame.display.set_mode((self.width,self.height))

	def display_frame(self):
		pygame.display.update()