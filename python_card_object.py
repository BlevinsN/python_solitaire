import random

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def get_rank(self):
		return self.rank

	def get_suit(self):
		return self.suit

	def show_card(self):
		if self.rank == 1:
			self.rank = "A"
		elif self.rank == 11:
			self.rank = "J"
		elif self.rank == 12:
			self.rank = "Q"
		elif self.rank == 13:
			self.rank = "K"
		return str(("{}{}".format(self.suit,self.rank)))


class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in ["♥","♦","♣","♠"]:
			for rank in range(1,14):
				self.cards.append(Card(rank, suit))
				
	def get_cards(self):
		return self.cards

	def show_deck(self):
		for card in self.cards:
			card.show_card()

	def shuffle_deck(self):
		for index in range(len(self.cards)-1,0,-1):
			r = random.randint(0,index)
			self.cards[index], self.cards[r] = self.cards[r], self.cards[index]

class Card_object:
	def __init__(self, card, position):
		self.card = card
		self.position = position
	
	def card_rank():
		return card.get_rank()

	def card_suit():
		return card.get_suit()

