import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	print("Starting asteroids!")

	game_clock = pygame.time.Clock()
	dt = 0  # delta_time

	group_updatable = pygame.sprite.Group()
	group_drawable = pygame.sprite.Group()
	group_asteroid = pygame.sprite.Group()
	group_shot = pygame.sprite.Group()

	Player.containers = (group_updatable, group_drawable)
	Asteroid.containers = (group_asteroid, group_updatable, group_drawable)
	AsteroidField.containers = group_updatable
	Shot.containers = (group_shot, group_drawable, group_updatable)

	my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # removed obj bc using groups
	AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0, 0, 0))

		# my_player.draw(screen)
		# my_player.update(dt)

		for obj in group_updatable:
			obj.update(dt)

		for obj in group_asteroid:
			for new_obj in group_shot:
				if new_obj.collision(obj):
					obj.split()  # split() new method in asteroid class
					new_obj.kill()

			if obj.collision(my_player):
				sys.exit("Game Over")

		for obj in group_drawable:
			obj.draw(screen)

		pygame.display.flip()

		amount_time = game_clock.tick(60)
		dt = amount_time / 1000


if __name__ == "__main__":
	main()
