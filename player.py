from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        self.radius = PLAYER_RADIUS
        self.turn_speed = PLAYER_TURN_SPEED
        self.player_speed = PLAYER_SPEED
        self.player_shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        self.shot_timer = 0

        super().__init__(x, y, self.radius)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def rotate(self, dt):
        self.rotation += self.turn_speed * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()
                self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.player_speed * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.rotation = self.rotation
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


