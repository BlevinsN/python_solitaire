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
			self.rank = "Ace"
		elif self.rank == 11:
			self.rank = "Jack"
		elif self.rank == 12:
			self.rank = "Queen"
		elif self.rank == 13:
			self.rank = "King"
		print("{} of {}".format(self.rank, self.suit))
		return

class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in ["spades", "clubs", "diamonds", "hearts"]:
			for rank in range(1,14):
				self.cards.append(Card(rank, suit))

	def show_deck(self):
		for card in self.cards:
			card.show_card()

	def shuffle_deck(self):
		for index in range(len(self.cards)-1,0,-1):
			r = random.randint(0,index)
			self.cards[index], self.cards[r] = self.cards[r], self.cards[index]

