import pygame
from python_card_object import *
import numpy as np

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

class Pygame_Solitaire_Manager:
	def __init__(self, screen):
		self.screen = screen
		self.screen.fill(BLACK)
		self.font = pygame.font.SysFont("None", 20)
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
		self.storage = [self.heart_stored, self.diamond_stored, self.spade_stored, self.club_stored]

		self.deck_hidden = pygame.Rect(self.vert_slice0.x, self.horz_slice6.y, self.card_width, self.card_height)
		self.deck_showing = pygame.Rect(self.vert_slice1.x, self.horz_slice6.y, self.card_width, self.card_height)

	def update_screen(self, game, omit=None):
		self.screen.fill(BLACK)
		game_storage = game.get_storage()

		for suit in range(len(game_storage)):
			pygame.draw.rect(self.screen, WHITE, self.storage[suit])
			if type(game_storage[suit]) == Card:
				text = self.font.render(game_storage[suit].show_card(), True, BLACK, WHITE)
			else:
				text = self.font.render(game_storage[suit], True, BLACK, WHITE)
			self.screen.blit(text, self.storage[suit])

		top_deck_cards = game.get_deck_cards()
		if top_deck_cards[0] != "EMPTY":
			pygame.draw.rect(self.screen, WHITE, self.deck_showing)
			text = self.font.render( str(top_deck_cards[0]), True, BLACK, WHITE)
			self.screen.blit(text, self.deck_showing)
		if top_deck_cards[1] != "EMPTY":
			pygame.draw.rect(self.screen, WHITE, self.deck_hidden)

		game_board = game.get_board()
		for stack in range(len(game_board)):
			for card in range(len(game_board[stack])):
				rect = pygame.Rect(self.x_pos[card].x, self.horz_slice1.y + (stack*self.buffer)+30, self.card_width, self.card_height)
				if type(game_board[stack][card]) == Card:
					if game_board[stack][card] != omit:
						pygame.draw.rect(self.screen, WHITE, rect)
						if game_board[stack][card].is_hidden():
							text = self.font.render( '', True, BLACK, WHITE)
						else:
							text = self.font.render( str(game_board[stack][card].show_card()), True, BLACK, WHITE)
						self.screen.blit(text, rect)
		return

	def drag_cards(self, game, mouse_event,clock):
		def look_in_stack(game, mouse_event):
			game_board = game.get_board()
			for stack in range(len(game_board)):
				for card in range(len(game_board[stack])):
					rect = pygame.Rect(self.x_pos[card].x, self.horz_slice1.y + (stack*self.buffer)+30, self.card_width, self.card_height)
					if type(game_board[stack][card]) == Card:
						if not game_board[stack][card].is_hidden():
							if rect.collidepoint(mouse_event.pos):
								return [rect, game_board[stack][card]]
			return
		def look_in_storage(game, mouse_event):
			for rect in range(len(self.storage)):
				if self.storage[rect].collidepoint(mouse_event.pos):
					return self.storage[rect]
			return
		to_move = look_in_stack(game, mouse_event)
		if to_move:
			dragging = True
			mouse_x, mouse_y = mouse_event.pos
			offset_x = to_move[0].x - mouse_x
			offset_y = to_move[0].y - mouse_y
			while dragging:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONUP:
						if event.button == 1:
							new_location = look_in_stack(game,event)
							if new_location:
								old_x, old_y = np.where(game.get_board() == to_move[1])
								new_x, new_y = np.where(game.get_board() == new_location[1])
								game.make_move(old_x[0],old_y[0],new_x[0])
								self.update_screen(game)
								return
							else:
								new_location = look_in_storage(game, event)
								if new_location:
									old_x, old_y = np.where(game.get_board() == to_move[1])
									game.store_card(old_x[0])
									self.update_screen(game)
									return

							dragging = False
					elif event.type == pygame.MOUSEMOTION:
						mouse_x, mouse_y = event.pos
						to_move[0].x = mouse_x + offset_x
						to_move[0].y = mouse_y + offset_y
				self.update_screen(game, to_move[1])
				pygame.draw.rect(self.screen, WHITE, to_move[0])
				text = self.font.render( to_move[1].show_card(), True, BLACK, WHITE)
				self.screen.blit(text, to_move[0])
				pygame.display.flip()
				clock.tick(60)
			return

	def deck_card(self, game, mouse_event,clock):
		if self.deck_hidden.collidepoint(mouse_event.pos):
			dragging = True
			while dragging:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONUP:
						if self.deck_hidden.collidepoint(event.pos):
							game.draw_deck()
							return True
						else:
							return False











