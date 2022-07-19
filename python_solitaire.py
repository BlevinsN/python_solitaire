import pygame
from python_card_object import *
import numpy as np

class Solitaire:
	def __init__(self, cards):
		self.board = np.full((21,7), "  ",dtype=np.dtype('U100'))
		self.deck = []
		self.stored = ["","","",""]
		self.order = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		index = 0
		for stack in range(0,7):
			for card in range(stack):
				self.board[card, stack] = '*' + cards[index].show_card()
				index += 1
			self.board[stack, stack] = cards[index].show_card()
			index += 1
		self.deck = [ card.show_card() for card in cards[index+1:]]

		print(self.board)
		print(self.deck)
		print(self.stored)

	def print_board(self):
		print('{:^3}'.format(" "),end=" ")
		for x in range(len(self.board[0])):
			print('{:^3}'.format(x),end="|")
		print()
		for x in range(len(self.board)):
			print('{:^3}'.format(x),end="|")
			found = False
			for y in range(len(self.board[x])):
				if self.board[x,y][0] == "*":
					print('{:^3}'.format('H'),end="|")
					found = True
				else:
					if self.board[x,y] != '  ':
						print('{:^3}'.format(self.board[x,y]),end="|")
						found = True
					else:
						print('{:^3}'.format(self.board[x,y]),end="|")
			print()
			if found == False:
				break
		if len(self.deck) > 0:
			print("Deck:",self.deck[0])
		else:
			print("Deck: EMPTY")
		print("Storage:", self.stored)
		return

	def draw_deck(self):
		temp = self.deck.pop(0)
		self.deck.append(temp)
		return

	def check_move(self, card, column):
		new_row = 0
		if card[0] == '*':
			return False
		if self.board[new_row, column] == '  ':
			if card[1:] == 'K':
				return True
			else:
				return False
		while self.board[new_row+1, column] != '  ':
			new_row += 1
		if card[0] == '♥' or card[0] == '♦':
			if self.board[new_row, column][0] == '♥' or self.board[new_row, column][0] == '♦':
				return False
		if card[0] == '♣' or card[0] == '♠':
			if self.board[new_row, column][0] == '♣' or self.board[new_row, column][0] == '♠':
				return False
		valid_card = self.order[self.order.index(self.board[new_row, column][1:]) - 1]
		if card[1:] != valid_card:
			return False
		return True

	def move_from_deck(self, new_column):
		if not Solitaire.check_move(self, self.deck[0], new_column):
			print("Bad Move")
			return
		new_row = 0
		while self.board[new_row, new_column] != '  ':
			new_row += 1
		self.board[new_row, new_column] = self.deck[0]
		self.deck.pop(0)
		return

	def move_from_store(self, store_column, new_column):
		if not Solitaire.check_move(self, self.stored[store_column], new_column):
			print("Bad Move")
			return
		new_row = 0
		while self.board[new_row, new_column] != '  ':
			new_row += 1
		self.board[new_row, new_column] = self.stored[store_column]
		self.stored[store_column] = self.stored[store_column][0] + self.order[self.order.index(self.stored[store_column][1:])-1]
		return

	def make_move(self, old_column, old_row, new_column):
		if not Solitaire.check_move(self, self.board[old_row, old_column], new_column):
			print("Bad Move")
			return
		if old_row > 0:
			if self.board[old_row-1, old_column][0] == "*":
				self.board[old_row-1, old_column] = self.board[old_row-1, old_column][1:]
		new_row = 0
		while self.board[new_row, new_column] != '  ':
			new_row += 1
		while self.board[old_row, old_column] != '  ':
			self.board[new_row, new_column] = self.board[old_row, old_column]
			self.board[old_row, old_column] = '  '
			old_row += 1
			new_row += 1
		return

	def store_card(self, column):
		row = 0
		while self.board[row, column] != '  ':
			row += 1
		row -= 1
		card = self.board[row, column]
		if card[0] == '♥':
			if card[1] == 'A':
				self.stored[0] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[0][1:]) + 1]:
					self.stored[0] = card
		if card[0] == '♦':
			if card[1] == 'A':
				self.stored[1] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[1][1:]) + 1]:
					self.stored[1] = card
		if card[0] == '♣':
			if card[1] == 'A':
				self.stored[2] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[2][1:]) + 1]:
					self.stored[2] = card
		if card[0] == '♠':
			if card[1] == 'A':
				self.stored[3] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[3][1:]) + 1]:
					self.stored[3] = card
		self.board[row, column] = "  "
		if row > 0:
			if self.board[row-1, column][0] == "*":
				self.board[row-1, column] = self.board[row-1, column][1:]

	def store_from_deck(self):
		card = self.deck[0]
		if card[0] == '♥':
			if card[1] == 'A':
				self.stored[0] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[0][1:]) + 1]:
					self.stored[0] = card
		if card[0] == '♦':
			if card[1] == 'A':
				self.stored[1] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[1][1:]) + 1]:
					self.stored[1] = card
		if card[0] == '♣':
			if card[1] == 'A':
				self.stored[2] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[2][1:]) + 1]:
					self.stored[2] = card
		if card[0] == '♠':
			if card[1] == 'A':
				self.stored[3] = card
			else:
				if card[1:] == self.order[self.order.index(self.stored[3][1:]) + 1]:
					self.stored[3] = card
		self.deck.pop(0)

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

deck = Deck()
#deck.show_deck()
deck.shuffle_deck()
#deck.show_deck()
cards = deck.get_cards()

game = Solitaire(cards)

while(True):
	game.print_board()
	print("1: Draw from deck.")
	print("2: Store a card from board.")
	print("3: Store a card from deck.")
	print("4: Move a card on the board.")
	print("5: Move a card from the deck.")
	print("6: Move a card from the store.")
	choice = input("What would you like to do: ")
	if choice == '1':
		game.draw_deck()
	elif choice == '2':
		print("You are storing a card. Please select card to store.")
		column = int(input("COLUMN: "))
		game.store_card(column)
	elif choice == '3':
		game.store_from_deck()
	elif choice == '4':
		print("You are moving a card. Please select card to move.")
		column = int(input("COLUMN: "))
		row = int(input("ROW: "))
		print("Which column would you like to move it to?")
		new_column = int(input("COLUMN: "))
		game.make_move(column, row, new_column)
	elif choice == '5':
		print("You are moving a card from the deck. Please select column to move this card.")
		column = int(input("COLUMN: "))
		game.move_from_deck(column)
	elif choice == '6':
		print("You are moving a card from the store. Please select the column of the card in store.")
		stored_card = int(input("STORE COLUMN: "))
		column = int(input("COLUMN ON BOARD: "))
		game.move_from_store(stored_card,column)
	else:
		print("INVALID")


#pygame.init()

# width = 800
# height = 800
# size = (width,height)
# screen = pygame.display.set_mode(size)
# font = pygame.font.Font(None, 12)
# buffer = 10
# row_width = (width / 7) - (2*buffer)
# card_width = row_width - (2*buffer)
# row_height = card_width * (5/4)
# card_height = row_height - buffer
# pygame.display.set_caption("Python Solitaire")

# carryOn = True
# clock = pygame.time.Clock()

# vert_slice0 = pygame.Rect(0*(width/7)+buffer, 0, row_width, height)
# vert_slice1 = pygame.Rect(1*(width/7)+buffer, 0, row_width, height)
# vert_slice2 = pygame.Rect(2*(width/7)+buffer, 0, row_width, height)
# vert_slice3 = pygame.Rect(3*(width/7)+buffer, 0, row_width, height)
# vert_slice4 = pygame.Rect(4*(width/7)+buffer, 0, row_width, height)
# vert_slice5 = pygame.Rect(5*(width/7)+buffer, 0, row_width, height)
# vert_slice6 = pygame.Rect(6*(width/7)+buffer, 0, row_width, height)

# horz_slice0 = pygame.Rect(0, (0*row_height)+buffer, width, row_height)
# horz_slice1 = pygame.Rect(0, (1*row_height)+buffer, width, row_height)
# horz_slice2 = pygame.Rect(0, (2*row_height)+buffer, width, row_height)
# horz_slice3 = pygame.Rect(0, (3*row_height)+buffer, width, row_height)
# horz_slice4 = pygame.Rect(0, (4*row_height)+buffer, width, row_height)
# horz_slice5 = pygame.Rect(0, (5*row_height)+buffer, width, row_height)
# horz_slice6 = pygame.Rect(0, (6*row_height)+buffer, width, row_height)

# x_pos = [vert_slice0, vert_slice1, vert_slice2, vert_slice3, vert_slice4, vert_slice5, vert_slice6]
# y_pos = [horz_slice0, horz_slice1, horz_slice2, horz_slice3, horz_slice4, horz_slice5, horz_slice6]

# while carryOn:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			carryOn = False

# 	screen.fill(BLACK)
	
# 	suit1 = pygame.Rect(vert_slice3.x, horz_slice0.y, card_width, card_height)
# 	suit2 = pygame.Rect(vert_slice4.x, horz_slice0.y, card_width, card_height)
# 	suit3 = pygame.Rect(vert_slice5.x, horz_slice0.y, card_width, card_height)
# 	suit4 = pygame.Rect(vert_slice6.x, horz_slice0.y, card_width, card_height)

# 	deck_hidden = pygame.Rect(vert_slice0.x, horz_slice6.y, card_width, card_height)
# 	deck_showing = pygame.Rect(vert_slice1.x, horz_slice6.y, card_width, card_height)

# 	# card1 = pygame.Rect(vert_slice0.x, horz_slice1.y, card_width, card_height)
# 	# card2 = pygame.Rect(vert_slice1.x, horz_slice1.y, card_width, card_height)
# 	# card3 = pygame.Rect(vert_slice2.x, horz_slice1.y, card_width, card_height)
# 	# card4 = pygame.Rect(vert_slice3.x, horz_slice1.y, card_width, card_height)
# 	# card5 = pygame.Rect(vert_slice4.x, horz_slice1.y, card_width, card_height)
# 	# card6 = pygame.Rect(vert_slice5.x, horz_slice1.y, card_width, card_height)
# 	# card7 = pygame.Rect(vert_slice6.x, horz_slice1.y, card_width, card_height)

# 	for stack in range(0,7):
# 		for card in range(stack+1):
# 			rect = pygame.Rect(x_pos[stack].x, horz_slice1.y + (card*buffer), card_width, card_height)
# 			if card % 2 == 0:
# 				pygame.draw.rect(screen, WHITE, rect)
# 			else:
# 				pygame.draw.rect(screen, RED, rect)

# 	pygame.draw.rect(screen, WHITE, suit1)
# 	pygame.draw.rect(screen, WHITE, suit2)
# 	pygame.draw.rect(screen, WHITE, suit3)
# 	pygame.draw.rect(screen, WHITE, suit4)

# 	# pygame.draw.rect(screen, WHITE, card1)
# 	# pygame.draw.rect(screen, WHITE, card2)
# 	# pygame.draw.rect(screen, WHITE, card3)
# 	# pygame.draw.rect(screen, WHITE, card4)
# 	# pygame.draw.rect(screen, WHITE, card5)
# 	# pygame.draw.rect(screen, WHITE, card6)
# 	# pygame.draw.rect(screen, WHITE, card7)
	
# 	pygame.draw.rect(screen, WHITE, deck_hidden)
# 	pygame.draw.rect(screen, WHITE, deck_showing)

# 	pygame.display.flip()
# 	clock.tick(60)

# pygame.quit()
