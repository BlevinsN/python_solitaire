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
row_width = (width / 7) - (2*buffer)
card_width = row_width - (2*buffer)
row_height = card_width * (5/4)
card_height = row_height - buffer
print(card_width, card_height)
pygame.display.set_caption("Python Solitaire")

carryOn = True
clock = pygame.time.Clock()

vert_slice0 = pygame.Rect(0*(width/7)+buffer, 0, row_width, height)
vert_slice1 = pygame.Rect(1*(width/7)+buffer, 0, row_width, height)
vert_slice2 = pygame.Rect(2*(width/7)+buffer, 0, row_width, height)
vert_slice3 = pygame.Rect(3*(width/7)+buffer, 0, row_width, height)
vert_slice4 = pygame.Rect(4*(width/7)+buffer, 0, row_width, height)
vert_slice5 = pygame.Rect(5*(width/7)+buffer, 0, row_width, height)
vert_slice6 = pygame.Rect(6*(width/7)+buffer, 0, row_width, height)

horz_slice0 = pygame.Rect(0, (0*row_height)+buffer, width, row_height)
horz_slice1 = pygame.Rect(0, (1*row_height)+buffer, width, row_height)
horz_slice2 = pygame.Rect(0, (2*row_height)+buffer, width, row_height)
horz_slice3 = pygame.Rect(0, (3*row_height)+buffer, width, row_height)
horz_slice4 = pygame.Rect(0, (4*row_height)+buffer, width, row_height)
horz_slice5 = pygame.Rect(0, (5*row_height)+buffer, width, row_height)
horz_slice6 = pygame.Rect(0, (6*row_height)+buffer, width, row_height)

x_pos = [vert_slice0, vert_slice1, vert_slice2, vert_slice3, vert_slice4, vert_slice5, vert_slice6]
y_pos = [horz_slice0, horz_slice1, horz_slice2, horz_slice3, horz_slice4, horz_slice5, horz_slice6]

while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False

	screen.fill(BLACK)
	
	suit1 = pygame.Rect(vert_slice3.x, horz_slice0.y, card_width, card_height)
	suit2 = pygame.Rect(vert_slice4.x, horz_slice0.y, card_width, card_height)
	suit3 = pygame.Rect(vert_slice5.x, horz_slice0.y, card_width, card_height)
	suit4 = pygame.Rect(vert_slice6.x, horz_slice0.y, card_width, card_height)

	deck_hidden = pygame.Rect(vert_slice0.x, horz_slice6.y, card_width, card_height)
	deck_showing = pygame.Rect(vert_slice1.x, horz_slice6.y, card_width, card_height)

	# card1 = pygame.Rect(vert_slice0.x, horz_slice1.y, card_width, card_height)
	# card2 = pygame.Rect(vert_slice1.x, horz_slice1.y, card_width, card_height)
	# card3 = pygame.Rect(vert_slice2.x, horz_slice1.y, card_width, card_height)
	# card4 = pygame.Rect(vert_slice3.x, horz_slice1.y, card_width, card_height)
	# card5 = pygame.Rect(vert_slice4.x, horz_slice1.y, card_width, card_height)
	# card6 = pygame.Rect(vert_slice5.x, horz_slice1.y, card_width, card_height)
	# card7 = pygame.Rect(vert_slice6.x, horz_slice1.y, card_width, card_height)

	for stack in range(0,7):
		for card in range(stack+1):
			rect = pygame.Rect(x_pos[stack].x, horz_slice1.y + (card*buffer), card_width, card_height)
			if card % 2 == 0:
				pygame.draw.rect(screen, WHITE, rect)
			else:
				pygame.draw.rect(screen, RED, rect)

	pygame.draw.rect(screen, WHITE, suit1)
	pygame.draw.rect(screen, WHITE, suit2)
	pygame.draw.rect(screen, WHITE, suit3)
	pygame.draw.rect(screen, WHITE, suit4)

	# pygame.draw.rect(screen, WHITE, card1)
	# pygame.draw.rect(screen, WHITE, card2)
	# pygame.draw.rect(screen, WHITE, card3)
	# pygame.draw.rect(screen, WHITE, card4)
	# pygame.draw.rect(screen, WHITE, card5)
	# pygame.draw.rect(screen, WHITE, card6)
	# pygame.draw.rect(screen, WHITE, card7)
	
	pygame.draw.rect(screen, WHITE, deck_hidden)
	pygame.draw.rect(screen, WHITE, deck_showing)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
