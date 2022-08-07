import pygame
from python_card_object import *
from pygame_solitaire_manager import *
import numpy as np

class Solitaire:
	def __init__(self):
		self.board = np.full((21,7), "",dtype=Card)
		self.deck = []
		self.stored = ["","","",""]
		cards = Deck()
		self.ordered_deck = [x for x in cards.get_cards()]
		cards.shuffle_deck()
		shuffled = cards.get_cards()
		index = 0
		for stack in range(0,7):
			for card in range(stack):
				shuffled[index].toggle_hide()
				self.board[card, stack] = shuffled[index]
				index += 1
			self.board[stack, stack] = shuffled[index]
			index += 1
		self.deck = shuffled[index:]

	def game_over(self):
		for x in self.stored:
			if x == '':
				return False
			else:
				if x.get_rank() != 'K': 
					return False
		return True

	def get_storage(self):
		storage = []
		for suit in self.stored:
			if type(suit) == Card:
				storage.append(suit)
			else:
				storage.append("EMPTY")
		return storage

	def get_deck_cards(self):
		if len(self.deck) > 1:
			return [self.deck[0], self.deck[1]]
		elif len(self.deck) > 0:
			return [self.deck[0], "EMPTY"]
		else:
			return ["EMPTY", "EMPTY"]

	def get_board(self):
		return self.board

	def print_board(self, screen):

		print('{:^3}'.format(" "),end=" ")
		for x in range(len(self.board[0])):
			print('{:^3}'.format(x),end="|")
		print()
		for x in range(len(self.board)):
			print('{:^3}'.format(x),end="|")
			found = False
			for y in range(len(self.board[x])):
				if self.board[x,y] != '':
					if self.board[x,y].is_hidden():
						print('{:^3}'.format('H'),end="|")
					else:
						print('{:^3}'.format(self.board[x,y].show_card()),end="|")
					found = True
				else:
					print('{:^3}'.format(" "),end="|")
			print()
			if found == False:
				break

		if len(self.deck) > 0:
			print("Deck:",self.deck[0].show_card())
		else:
			print("Deck: EMPTY")

		return

	def draw_deck(self):
		if len(self.deck) > 0:
			temp = self.deck.pop(0)
			self.deck.append(temp)
		return

	def check_move(self, card, column):
		new_row = 0
		if type(card) != Card:
			return False
		if card.is_hidden():
			return False
		if self.board[new_row, column] == '':
			if card.get_rank() == 'K':
				return True
			else:
				return False
		while self.board[new_row+1, column] != '':
			new_row += 1
		suit = card.get_suit()
		to_check = self.board[new_row, column]
		if suit == '♥' or suit == '♦':
			if to_check.get_suit() == '♥' or to_check.get_suit() == '♦':
				return False
		if suit == '♣' or suit == '♠':
			if to_check.get_suit() == '♣' or to_check.get_suit() == '♠':
				return False
		ordered_index = self.ordered_deck.index(card)
		valid_rank = self.ordered_deck[ordered_index+1].get_rank()
		if valid_rank == 11:
			valid_rank = 'J'
		elif valid_rank == 12:
			valid_rank = 'Q'
		elif valid_rank == 13:
			valid_rank = 'K'
		if to_check.get_rank() != valid_rank:
			print(to_check.get_rank(), valid_rank)
			return False
		return True

	def move_from_deck(self, new_column):
		if not Solitaire.check_move(self, self.deck[0], new_column):
			print("Bad Move")
			return
		new_row = 0
		while self.board[new_row, new_column] != '':
			new_row += 1
		self.board[new_row, new_column] = self.deck[0]
		self.deck.pop(0)
		return

	def move_from_store(self, store_column, new_column):
		if store_column > len(self.stored) or new_column > len(self.board[0]):
			return
		if not Solitaire.check_move(self, self.stored[store_column], new_column):
			print("Bad Move")
			return
		new_row = 0
		while self.board[new_row, new_column] != '':
			new_row += 1
		self.board[new_row, new_column] = self.stored[store_column]
		ordered_index = self.ordered_deck.index(self.stored[store_column])
		self.stored[store_column] = self.ordered_deck[ordered_index-1]
		return

	def make_move(self, old_column, old_row, new_column):
		if not Solitaire.check_move(self, self.board[old_row, old_column], new_column):
			print("Bad Move")
			return
		if old_row > 0:
			if self.board[old_row-1, old_column].is_hidden():
				self.board[old_row-1, old_column].toggle_hide()
		new_row = 0
		while self.board[new_row, new_column] != '':
			new_row += 1
		while self.board[old_row, old_column] != '':
			self.board[new_row, new_column] = self.board[old_row, old_column]
			self.board[old_row, old_column] = ''
			old_row += 1
			new_row += 1
		return

	def store_card(self, column):
		if column < 0 or column > len(self.board[0]):
			return
		row = 0
		while self.board[row, column] != '':
			row += 1
		row -= 1
		card = self.board[row, column]
		if card.get_suit() == '♥':
			if card.get_rank() == 'A':
				self.stored[0] = card
			elif self.stored[0]:
				ordered_index = self.ordered_deck.index(self.stored[0])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[0] = card
				else:
					return
			else:
				return
		if card.get_suit() == '♦':
			if card.get_rank() == 'A':
				self.stored[1] = card
			elif self.stored[1]:
				ordered_index = self.ordered_deck.index(self.stored[1])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[1] = card
				else:
					return
			else:
				return
		if card.get_suit() == '♣':
			if card.get_rank() == 'A':
				self.stored[2] = card
			elif self.stored[2]:
				ordered_index = self.ordered_deck.index(self.stored[2])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[2] = card
				else:
					return
			else:
				return
		if card.get_suit() == '♠':
			if card.get_rank() == 'A':
				self.stored[3] = card
			elif self.stored[3]:
				ordered_index = self.ordered_deck.index(self.stored[3])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[3] = card
				else:
					return
			else:
				return
		self.board[row, column] = ""
		if row > 0:
			if self.board[row-1, column].is_hidden():
				self.board[row-1, column].toggle_hide()

	def store_from_deck(self):
		if len(self.deck) == 0:
			return
		card = self.deck[0]
		if card.get_suit() == '♥':
			if card.get_rank() == 'A':
				self.stored[0] = card
			elif self.stored[0]:
				ordered_index = self.ordered_deck.index(self.stored[0])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[0] = card
				else:
					return
			else:
				return
		if card.get_suit() == '♦':
			if card.get_rank() == 'A':
				self.stored[1] = card
			elif self.stored[1]:
				ordered_index = self.ordered_deck.index(self.stored[1])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[1] = card
				else:
					return
			else:
				return
		if card.get_suit() == '♣':
			if card.get_rank() == 'A':
				self.stored[2] = card
			elif self.stored[2]:
				ordered_index = self.ordered_deck.index(self.stored[2])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[2] = card
				else:
					return
			else:
				return
		if card.get_suit() == '♠':
			if card.get_rank() == 'A':
				self.stored[3] = card
			elif self.stored[3]:
				ordered_index = self.ordered_deck.index(self.stored[3])
				to_check = self.ordered_deck[ordered_index+1]
				if card.get_rank() == to_check.get_rank():
					self.stored[3] = card
				else:
					return
			else:
				return
		self.deck.pop(0)

game = Solitaire()

# while(True):
# 	game.print_board()
# 	print("1: Draw from deck.")
# 	print("2: Store a card from board.")
# 	print("3: Store a card from deck.")
# 	print("4: Move a card on the board.")
# 	print("5: Move a card from the deck.")
# 	print("6: Move a card from the store.")
# 	choice = input("What would you like to do: ")
# 	if choice == '1':
# 		game.draw_deck()
# 	elif choice == '2':
# 		try:
# 			print("You are storing a card. Please select card to store.")
# 			column = int(input("COLUMN: "))
# 			game.store_card(column)
# 		except:
# 			print("INVALID INPUT")
# 	elif choice == '3':
# 		game.store_from_deck()
# 	elif choice == '4':
# 		print("You are moving a card. Please select card to move.")
# 		try:
# 			column = int(input("COLUMN: "))
# 			row = int(input("ROW: "))
# 			print("Which column would you like to move it to?")
# 			new_column = int(input("COLUMN: "))
# 			game.make_move(column, row, new_column)
# 		except:
# 			print("INVALID INPUT")
# 	elif choice == '5':
# 		try:
# 			print("You are moving a card from the deck. Please select column to move this card.")
# 			column = int(input("COLUMN: "))
# 			game.move_from_deck(column)
# 		except:
# 			print("INVALID INPUT")
# 	elif choice == '6':
# 		try:
# 			print("You are moving a card from the store. Please select the column of the card in store.")
# 			stored_card = int(input("STORE COLUMN: "))
# 			column = int(input("COLUMN ON BOARD: "))
# 			game.move_from_store(stored_card,column)
# 		except:
# 			print("INVALID INPUT")
# 	else:
# 		print("INVALID")
# 	if game.game_over():
# 		print("---------- YOU HAVE WON THE GAME ----------")
# 		break

pygame.init()
width = 800
height = 800
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python Solitaire")

game_manager = Pygame_Solitaire_Manager(screen)
carryOn = True
clock = pygame.time.Clock()
while carryOn:
	# print("1: Draw from deck.")
	# print("2: Store a card from board.")
	# print("3: Store a card from deck.")
	# print("4: Move a card on the board.")
	# print("5: Move a card from the deck.")
	# print("6: Move a card from the store.")
	# choice = input("What would you like to do: ")
	# if choice == '1':
	# 	game.draw_deck()
	# elif choice == '2':
	# 	try:
	# 		print("You are storing a card. Please select card to store.")
	# 		column = int(input("COLUMN: "))
	# 		game.store_card(column)
	# 	except:
	# 		print("INVALID INPUT")
	# elif choice == '3':
	# 	game.store_from_deck()
	# elif choice == '4':
	# 	print("You are moving a card. Please select card to move.")
	# 	try:
	# 		column = int(input("COLUMN: "))
	# 		row = int(input("ROW: "))
	# 		print("Which column would you like to move it to?")
	# 		new_column = int(input("COLUMN: "))
	# 		game.make_move(column, row, new_column)
	# 	except:
	# 		print("INVALID INPUT")
	# elif choice == '5':
	# 	try:
	# 		print("You are moving a card from the deck. Please select column to move this card.")
	# 		column = int(input("COLUMN: "))
	# 		game.move_from_deck(column)
	# 	except:
	# 		print("INVALID INPUT")
	# elif choice == '6':
	# 	try:
	# 		print("You are moving a card from the store. Please select the column of the card in store.")
	# 		stored_card = int(input("STORE COLUMN: "))
	# 		column = int(input("COLUMN ON BOARD: "))
	# 		game.move_from_store(stored_card,column)
	# 	except:
	# 		print("INVALID INPUT")
	# else:
	# 	print("INVALID")
	# if game.game_over():
	# 	print("---------- YOU HAVE WON THE GAME ----------")
	# 	break
	game_manager.update_screen(game)
	dragging = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				game_manager.deck_card(game, event)
				game_manager.drag_cards(game, event, clock)
				game_manager.drag_deck(game, event, clock)
				game_manager.drag_storage(game,event, clock)

	
	clock.tick(60)
	pygame.display.flip()

pygame.quit()
