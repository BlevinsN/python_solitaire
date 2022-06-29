import pygame
from python_card_object import *

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

deck = Deck()
deck.show_deck()
deck.shuffle_deck()
deck.show_deck()
cards = deck.get_cards()
pygame.init()

width = 800
height = 800
size = (width,height)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 12)
pygame.display.set_caption("Python Solitaire")

carryOn = True
clock = pygame.time.Clock()

while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False

	screen.fill(BLACK)

	pygame.draw.rect(screen, WHITE, pygame.Rect(30,30,60,60))
	text = cards[0].get_rank()
	screen.blit(text, card_one)
	pygame.draw.rect(screen, WHITE, pygame.Rect(100,30,60,60))
	pygame.draw.rect(screen, WHITE, pygame.Rect(170,30,60,60))
	pygame.draw.rect(screen, WHITE, pygame.Rect(240,30,60,60))
	pygame.draw.rect(screen, WHITE, pygame.Rect(310,30,60,60))
	pygame.draw.rect(screen, WHITE, pygame.Rect(380,30,60,60))
	pygame.draw.rect(screen, WHITE, pygame.Rect(450,30,60,60))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
