import pygame
from python_card_object import *
import numpy as np

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

class Pygame_Solitaire_Manager:
	def __init__(self, screen, game):
		self.game = game
		self.screen = screen
		self.screen.fill(GREEN)
		self.font = pygame.font.SysFont("None", 18)
		area = self.screen.get_rect()
		width = area.width
		height = area.height
		self.buffer = 12
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

	def draw_card(self, card, rect):
		card_rank = card.get_rank()
		card_suit = card.get_suit()
		if not card.is_hidden():
			rank_text = self.font.render(str(card_rank), True, BLACK, WHITE)
			if card_suit == "\u2660":
				image = pygame.image.load('spade.jpg')
			elif card_suit == "\u2663":
				image = pygame.image.load('club.jpg')
			elif card_suit == "\u2666":
				image = pygame.image.load('diamond.png')
			elif card_suit == "\u2665":
				image = pygame.image.load('heart.png')
			center_image = pygame.transform.scale(image, (self.card_height/2, self.card_width/2))
			top_image = pygame.transform.scale(image, (self.card_height/6, self.card_width/6))
			self.screen.blit(center_image, (rect.centerx-(self.card_width/4),rect.centery-(self.card_height/4)))
			self.screen.blit(top_image, (rect.topright[0]-(self.card_width/6),rect.topright[1]))
			self.screen.blit(rank_text, rect)
		return 


	def update_screen(self, game, omit=None):
		self.screen.fill(GREEN)
		game_storage = self.game.stored

		for suit in range(len(game_storage)):
			outer_rect = self.storage[suit]
			rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
			pygame.draw.rect(self.screen, BLACK, outer_rect)
			pygame.draw.rect(self.screen, WHITE, rect)
			if type(game_storage[suit]) == Card:
				if game_storage[suit] != omit:
					self.draw_card(game_storage[suit], rect)
			else:
				text = self.font.render(game_storage[suit], True, BLACK, WHITE)
				self.screen.blit(text, rect)

		top_deck_cards = game.get_deck_cards()
		if top_deck_cards[0] != "EMPTY":
			if top_deck_cards[0] != omit:
				outer_rect = self.deck_showing
				rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
				pygame.draw.rect(self.screen, BLACK, outer_rect)
				pygame.draw.rect(self.screen, WHITE, rect)
				self.draw_card(top_deck_cards[0], rect)
		if top_deck_cards[1] != "EMPTY":
			outer_rect = self.deck_hidden
			rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
			pygame.draw.rect(self.screen, BLACK, outer_rect)
			pygame.draw.rect(self.screen, WHITE, rect)

		game_board = game.get_board()
		omit_col = -1
		for x in range(len(self.game.board)):
			for y in range(len(self.game.board[x])):
				outer_rect = pygame.Rect(self.x_pos[y].x, self.horz_slice1.y + (x*self.buffer)+30, self.card_width, self.card_height)
				rect = pygame.Rect(self.x_pos[y].x+2, self.horz_slice1.y + (x*self.buffer)+32, self.card_width-4, self.card_height-4)
				if type(game_board[x][y]) == Card:
					if game_board[x][y] != omit:
						if omit_col != y:
							pygame.draw.rect(self.screen, BLACK, outer_rect,2,2)
							pygame.draw.rect(self.screen, WHITE, rect)
							self.draw_card(game_board[x][y], rect)
					else:
						omit_col = y
		return


	def drag_cards(self, game, mouse_event,clock):
		def look_in_stack(game, mouse_event):
			for x in range(len(self.game.board)-1,-1,-1):
				for y in range(len(self.game.board[x])-1,-1,-1):
					rect = pygame.Rect(self.x_pos[y].x, self.horz_slice1.y + (x*self.buffer)+30, self.card_width, self.card_height)
					if type(self.game.board[x][y]) == Card:
						if not self.game.board[x][y].is_hidden():
							if rect.collidepoint(mouse_event.pos):
								return [rect, self.game.board[x][y]]
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
			old_x, old_y = np.where(self.game.board == to_move[1])
			while dragging:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONUP:
						if event.button == 1:
							new_location = look_in_stack(game,event)
							if new_location:
								game.print_board(self.screen)
								new_x, new_y = np.where(self.game.board == new_location[1])
								game.make_move(old_y[0],old_x[0],new_y[0])
								self.update_screen(game)
								return
							new_location = look_in_storage(game, event)
							if new_location:
								game.store_card(old_y[0])
								self.update_screen(game)
								return
							if to_move[1].get_rank() == 'K':
								for rect in self.x_pos:
									if rect.collidepoint(event.pos):
										game.make_move(old_y[0],old_x[0], self.x_pos.index(rect))
										self.update_screen(game)
										return
							dragging = False
					elif event.type == pygame.MOUSEMOTION:
						mouse_x, mouse_y = event.pos
						to_move[0].x = mouse_x + offset_x
						to_move[0].y = mouse_y + offset_y
				self.update_screen(game, to_move[1])
				outer_rect = to_move[0]
				rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
				pygame.draw.rect(self.screen, BLACK, outer_rect,2,2)
				pygame.draw.rect(self.screen, WHITE, rect)
				self.draw_card(to_move[1],rect)
				x = old_x[0]+1
				while type(self.game.board[x][old_y[0]]) == Card:
					index = x - (old_x[0])
					outer_rect = pygame.Rect(to_move[0].x, to_move[0].y + (index*10), self.card_width, self.card_height)
					rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
					pygame.draw.rect(self.screen, BLACK, outer_rect,2,2)
					pygame.draw.rect(self.screen, WHITE, rect)
					self.draw_card(self.game.board[x][old_y[0]],rect)
					x+=1
				pygame.display.flip()
				clock.tick(60)
			return

	def deck_card(self, game, mouse_event):
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

	def drag_deck(self, game, mouse_event,clock):
		def look_in_stack(game, mouse_event):
			for x in range(len(self.game.board)-1,-1,-1):
				for y in range(len(self.game.board[x])-1,-1,-1):
					rect = pygame.Rect(self.x_pos[y].x, self.horz_slice1.y + (x*self.buffer)+30, self.card_width, self.card_height)
					if type(self.game.board[x][y]) == Card:
						if not self.game.board[x][y].is_hidden():
							if rect.collidepoint(mouse_event.pos):
								return [rect, self.game.board[x][y]]
			return
		def look_in_storage(game, mouse_event):
			for rect in range(len(self.storage)):
				if self.storage[rect].collidepoint(mouse_event.pos):
					return self.storage[rect]
			return
		def look_in_deck(game, mouse_event):
			if self.deck_showing.collidepoint(mouse_event.pos):
				return [self.deck_showing, game.get_deck_cards()[0]]
		to_move = look_in_deck(game, mouse_event)
		if to_move:
			dragging = True
			mouse_x, mouse_y = mouse_event.pos
			offset_x = to_move[0].x - mouse_x
			offset_y = to_move[0].y - mouse_y
			while dragging:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONUP:
						if event.button == 1:
							game.print_board(self.screen)
							new_location = look_in_stack(game,event)
							if new_location:
								new_x, new_y = np.where(game.get_board() == new_location[1])
								game.move_from_deck(new_y[0])
							new_location = look_in_storage(game, event)
							if new_location:
								game.store_from_deck()
							if to_move[1].get_rank() == 'K':
								for rect in self.x_pos:
									if rect.collidepoint(event.pos):
										game.move_from_deck(self.x_pos.index(rect))
							self.deck_showing = pygame.Rect(self.vert_slice1.x, self.horz_slice6.y, self.card_width, self.card_height)
							self.update_screen(game)
							dragging = False
					elif event.type == pygame.MOUSEMOTION:
						mouse_x, mouse_y = event.pos
						to_move[0].x = mouse_x + offset_x
						to_move[0].y = mouse_y + offset_y
				self.update_screen(game, to_move[1])
				outer_rect = pygame.Rect(to_move[0].x, to_move[0].y, self.card_width, self.card_height)
				rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
				pygame.draw.rect(self.screen, BLACK, outer_rect,2,2)
				pygame.draw.rect(self.screen, WHITE, rect)
				self.draw_card(to_move[1],rect)
				pygame.display.flip()
				clock.tick(60)
			return

	def drag_storage(self, game, mouse_event,clock):
		def look_in_stack(game, mouse_event):
			for x in range(len(self.game.board)-1,-1,-1):
				for y in range(len(self.game.board[x])-1,-1,-1):
					rect = pygame.Rect(self.x_pos[y].x, self.horz_slice1.y + (x*self.buffer)+30, self.card_width, self.card_height)
					if type(self.game.board[x][y]) == Card:
						if not self.game.board[x][y].is_hidden():
							if rect.collidepoint(mouse_event.pos):
								return [rect, self.game.board[x][y]]
			return
		def look_in_storage(game, mouse_event):
			hearts = pygame.Rect(self.vert_slice3.x, self.horz_slice0.y, self.card_width, self.card_height)
			diamonds = pygame.Rect(self.vert_slice4.x, self.horz_slice0.y, self.card_width, self.card_height)
			spades = pygame.Rect(self.vert_slice5.x, self.horz_slice0.y, self.card_width, self.card_height)
			clubs = pygame.Rect(self.vert_slice6.x, self.horz_slice0.y, self.card_width, self.card_height)
			storage_pos = [hearts, diamonds, spades, clubs]
			for rect in range(len(storage_pos)):
				if storage_pos[rect].collidepoint(mouse_event.pos):
					game_storage = game.get_storage()
					return [storage_pos[rect], game_storage[rect], rect]
			return
		to_move = look_in_storage(game, mouse_event)
		if to_move:
			if type(to_move[1]) != Card:
				return
			to_return = to_move[0]
			dragging = True
			mouse_x, mouse_y = mouse_event.pos
			offset_x = to_move[0].x - mouse_x
			offset_y = to_move[0].y - mouse_y
			while dragging:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONUP:
						if event.button == 1:
							game.print_board(self.screen)
							new_location = look_in_stack(game,event)
							if new_location:
								new_x, new_y = np.where(game.get_board() == new_location[1])
								game.move_from_store(to_move[2], new_y[0])
							self.update_screen(game)
							dragging = False
					elif event.type == pygame.MOUSEMOTION:
						mouse_x, mouse_y = event.pos
						to_move[0].x = mouse_x + offset_x
						to_move[0].y = mouse_y + offset_y
						self.update_screen(game,to_move[1])
						outer_rect = pygame.Rect(to_move[0].x, to_move[0].y, self.card_width, self.card_height)
						rect = pygame.Rect(outer_rect.x+2, outer_rect.y+2, self.card_width-4, self.card_height-4)
						pygame.draw.rect(self.screen, BLACK, outer_rect,2,2)
						pygame.draw.rect(self.screen, WHITE, rect)
						self.draw_card(to_move[1],rect)
						pygame.display.flip()
						clock.tick(60)
			return










