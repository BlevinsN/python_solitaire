import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

class Pygame_Solitaire_Manager:
	def __init__(self, screen):
		self.screen = screen
		self.screen.fill(BLACK)
		self.font = pygame.font.Font(None, 24)
		area = self.screen.get_rect()
		width = area.width
		height = area.height
		buffer = 10
		row_width = (width / 7) - (2*buffer)
		card_width = row_width - (2*buffer)
		row_height = card_width * (5/4)
		card_height = row_height - buffer

		self.vert_slice0 = pygame.Rect(0*(width/7)+buffer, 0, row_width, height)
		self.vert_slice1 = pygame.Rect(1*(width/7)+buffer, 0, row_width, height)
		self.vert_slice2 = pygame.Rect(2*(width/7)+buffer, 0, row_width, height)
		self.vert_slice3 = pygame.Rect(3*(width/7)+buffer, 0, row_width, height)
		self.vert_slice4 = pygame.Rect(4*(width/7)+buffer, 0, row_width, height)
		self.vert_slice5 = pygame.Rect(5*(width/7)+buffer, 0, row_width, height)
		self.vert_slice6 = pygame.Rect(6*(width/7)+buffer, 0, row_width, height)

		self.horz_slice0 = pygame.Rect(0, (0*row_height)+buffer, width, row_height)
		self.horz_slice1 = pygame.Rect(0, (1*row_height)+buffer, width, row_height)
		self.horz_slice2 = pygame.Rect(0, (2*row_height)+buffer, width, row_height)
		self.horz_slice3 = pygame.Rect(0, (3*row_height)+buffer, width, row_height)
		self.horz_slice4 = pygame.Rect(0, (4*row_height)+buffer, width, row_height)
		self.horz_slice5 = pygame.Rect(0, (5*row_height)+buffer, width, row_height)
		self.horz_slice6 = pygame.Rect(0, (6*row_height)+buffer, width, row_height)

		self.x_pos = [self.vert_slice0, self.vert_slice1, self.vert_slice2, self.vert_slice3, self.vert_slice4, self.vert_slice5, self.vert_slice6]
		self.y_pos = [self.horz_slice0, self.horz_slice1, self.horz_slice2, self.horz_slice3, self.horz_slice4, self.horz_slice5, self.horz_slice6]

		self.heart_stored = pygame.Rect(self.vert_slice3.x, self.horz_slice0.y, card_width, card_height)
		self.diamond_stored = pygame.Rect(self.vert_slice4.x, self.horz_slice0.y, card_width, card_height)
		self.spade_stored = pygame.Rect(self.vert_slice5.x, self.horz_slice0.y, card_width, card_height)
		self.club_stored = pygame.Rect(self.vert_slice6.x, self.horz_slice0.y, card_width, card_height)

		self.deck_hidden = pygame.Rect(self.vert_slice0.x, self.horz_slice6.y, card_width, card_height)
		self.deck_showing = pygame.Rect(self.vert_slice1.x, self.horz_slice6.y, card_width, card_height)

	def update_screen(self, game):

		pygame.draw.rect(self.screen, WHITE, self.deck_hidden)
		pygame.draw.rect(self.screen, WHITE, self.deck_showing)
		pygame.draw.rect(self.screen, WHITE, self.heart_stored)
		pygame.draw.rect(self.screen, WHITE, self.diamond_stored)
		pygame.draw.rect(self.screen, WHITE, self.spade_stored)
		pygame.draw.rect(self.screen, WHITE, self.club_stored)

		storage = [self.heart_stored, self.diamond_stored, self.spade_stored, self.club_stored]
		game_storage = game.get_storage()
		print(game_storage)

		for suit in range(len(game_storage)):
			pygame.draw.rect(self.screen, WHITE, storage[suit])
			text = self.font.render(game_storage[suit], True, BLACK, WHITE)
			self.screen.blit(text, storage[suit])

		return