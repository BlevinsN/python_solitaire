import pygame
from python_card_object import *

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

class Pygame_Solitaire_Manager:
	def __init__(self, screen):
		self.screen = screen
		self.screen.fill(BLACK)
		self.font = pygame.font.Font(None, 24)
		area = self.screen.get_rect()
		width = area.width
		height = area.height
		self.buffer = 10
		self.row_width = (width / 7) - (2*self.buffer)
		self.card_width = self.row_width - (2*self.buffer)
		self.row_height = self.card_width * (5/4)
		self.card_height = self.row_height - self.buffer

		self.vert_slice0 = pygame.Rect(0*(width/7)+self.buffer, 0, self.row_width, height)
		self.vert_slice1 = pygame.Rect(1*(width/7)+self.buffer, 0, self.row_width, height)
		self.vert_slice2 = pygame.Rect(2*(width/7)+self.buffer, 0, self.row_width, height)
		self.vert_slice3 = pygame.Rect(3*(width/7)+self.buffer, 0, self.row_width, height)
		self.vert_slice4 = pygame.Rect(4*(width/7)+self.buffer, 0, self.row_width, height)
		self.vert_slice5 = pygame.Rect(5*(width/7)+self.buffer, 0, self.row_width, height)
		self.vert_slice6 = pygame.Rect(6*(width/7)+self.buffer, 0, self.row_width, height)

		self.horz_slice0 = pygame.Rect(0, (0*self.row_height)+self.buffer, width, self.row_height)
		self.horz_slice1 = pygame.Rect(0, (1*self.row_height)+self.buffer, width, self.row_height)
		self.horz_slice2 = pygame.Rect(0, (2*self.row_height)+self.buffer, width, self.row_height)
		self.horz_slice3 = pygame.Rect(0, (3*self.row_height)+self.buffer, width, self.row_height)
		self.horz_slice4 = pygame.Rect(0, (4*self.row_height)+self.buffer, width, self.row_height)
		self.horz_slice5 = pygame.Rect(0, (5*self.row_height)+self.buffer, width, self.row_height)
		self.horz_slice6 = pygame.Rect(0, (6*self.row_height)+self.buffer, width, self.row_height)

		self.x_pos = [self.vert_slice0, self.vert_slice1, self.vert_slice2, self.vert_slice3, self.vert_slice4, self.vert_slice5, self.vert_slice6]
		self.y_pos = [self.horz_slice0, self.horz_slice1, self.horz_slice2, self.horz_slice3, self.horz_slice4, self.horz_slice5, self.horz_slice6]

		self.heart_stored = pygame.Rect(self.vert_slice3.x, self.horz_slice0.y, self.card_width, self.card_height)
		self.diamond_stored = pygame.Rect(self.vert_slice4.x, self.horz_slice0.y, self.card_width, self.card_height)
		self.spade_stored = pygame.Rect(self.vert_slice5.x, self.horz_slice0.y, self.card_width, self.card_height)
		self.club_stored = pygame.Rect(self.vert_slice6.x, self.horz_slice0.y, self.card_width, self.card_height)

		self.deck_hidden = pygame.Rect(self.vert_slice0.x, self.horz_slice6.y, self.card_width, self.card_height)
		self.deck_showing = pygame.Rect(self.vert_slice1.x, self.horz_slice6.y, self.card_width, self.card_height)

	def update_screen(self, game):
		self.screen.fill(BLACK)
		storage = [self.heart_stored, self.diamond_stored, self.spade_stored, self.club_stored]
		game_storage = game.get_storage()

		for suit in range(len(game_storage)):
			pygame.draw.rect(self.screen, WHITE, storage[suit])
			text = self.font.render(game_storage[suit], True, BLACK, WHITE)
			self.screen.blit(text, storage[suit])

		top_deck_cards = game.get_deck_cards()
		if top_deck_cards[0] != "EMPTY":
			pygame.draw.rect(self.screen, WHITE, self.deck_showing)
			text = self.font.render( top_deck_cards[0], True, BLACK, WHITE)
			self.screen.blit(text, self.deck_showing)
		if top_deck_cards[1] != "EMPTY":
			pygame.draw.rect(self.screen, WHITE, self.deck_hidden)

		game_board = game.get_board()
		for stack in range(len(game_board)):
			for card in range(len(game_board[stack])):
				rect = pygame.Rect(self.x_pos[card].x, self.horz_slice1.y + (stack*self.buffer), self.card_width, self.card_height)
				if type(game_board[stack][card]) == Card:
					pygame.draw.rect(self.screen, WHITE, rect)
					text = self.font.render( game_board[stack][card].show_card(), True, BLACK, WHITE)
					self.screen.blit(text, rect)
		return