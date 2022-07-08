import pygame
from python_card_object import *

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

#deck = Deck()
#deck.show_deck()
#deck.shuffle_deck()
#deck.show_deck()
#cards = deck.get_cards()
pygame.init()

width = 800
height = 800
size = (width,height)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 12)
buffer = 10
card_width = (width / 7) - (2*buffer)
card_height = card_width * (5/4)
print(card_width, card_height)
pygame.display.set_caption("Python Solitaire")

carryOn = True
clock = pygame.time.Clock()

while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False

	screen.fill(BLACK)

	vert_slice0 = pygame.Rect(0*(width/7), 0, width/7, height)
	vert_slice1 = pygame.Rect(1*(width/7), 0, width/7, height)
	vert_slice2 = pygame.Rect(2*(width/7), 0, width/7, height)
	vert_slice3 = pygame.Rect(3*(width/7), 0, width/7, height)
	vert_slice4 = pygame.Rect(4*(width/7), 0, width/7, height)
	vert_slice5 = pygame.Rect(5*(width/7), 0, width/7, height)
	vert_slice6 = pygame.Rect(6*(width/7), 0, width/7, height)
	
	card0 = pygame.Rect(vert_slice0.x + buffer, vert_slice0.y + buffer, card_width, card_height)
	card1 = pygame.Rect(vert_slice1.x + buffer, vert_slice1.y + buffer, card_width, card_height)
	card2 = pygame.Rect(vert_slice2.x + buffer, vert_slice2.y + buffer, card_width, card_height)
	card3 = pygame.Rect(vert_slice3.x + buffer, vert_slice3.y + buffer, card_width, card_height)
	card4 = pygame.Rect(vert_slice4.x + buffer, vert_slice4.y + buffer, card_width, card_height)
	card5 = pygame.Rect(vert_slice5.x + buffer, vert_slice5.y + buffer, card_width, card_height)
	card6 = pygame.Rect(vert_slice6.x + buffer, vert_slice6.y + buffer, card_width, card_height)

	pygame.draw.rect(screen, WHITE, card0)
	pygame.draw.rect(screen, WHITE, card1)
	pygame.draw.rect(screen, WHITE, card2)
	pygame.draw.rect(screen, WHITE, card3)
	pygame.draw.rect(screen, WHITE, card4)
	pygame.draw.rect(screen, WHITE, card5)
	pygame.draw.rect(screen, WHITE, card6)
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
