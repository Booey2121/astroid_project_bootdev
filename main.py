import pygame
from constants import *
from player import Player


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	print("Starting asteroids!")

	game_clock = pygame.time.Clock()
	dt = 0  # delta_time

	group_updatable = pygame.sprite.Group()
	group_drawable = pygame.sprite.Group()

	Player.containers = (group_updatable, group_drawable)

	Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # removed obj bc using groups

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0, 0, 0))

		# my_player.draw(screen)
		# my_player.update(dt)

		for obj in group_updatable:
			obj.update(dt)

		for obj in group_drawable:
			obj.draw(screen)

		pygame.display.flip()

		amount_time = game_clock.tick(60)
		dt = amount_time / 1000


if __name__ == "__main__":
	main()
