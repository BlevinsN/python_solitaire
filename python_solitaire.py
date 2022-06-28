import pygame
from python_card_object import *

# BLACK = ( 0, 0, 0)
# WHITE = ( 255, 255, 255)
# GREEN = ( 0, 255, 0)
# RED = ( 255, 0, 0)

# pygame.init()
# size = (800,800)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Python Solitaire")

# carryOn = True
# clock = pygame.time.Clock()

# while carryOn:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			carryOn = False

# 	screen.fill(GREEN)

# 	pygame.display.flip()
# 	clock.tick(60)

# pygame.quit()
deck = Deck()
deck.show_deck()
deck.shuffle_deck()
deck.show_deck()
