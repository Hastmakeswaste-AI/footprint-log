import sys
import random
import pygame

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TANK_SPEED = 4
BULLET_SPEED = 8
MAX_BULLETS = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
RED = (237, 28, 36)
BLUE = (0, 162, 232)
YELLOW = (255, 242, 0)

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, color, controls):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, 40, 40), border_radius=8)
        self.turret = pygame.Surface((6, 30), pygame.SRCALPHA)
        pygame.draw.rect(self.turret, BLACK, (0, 0, 6, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = pygame.Vector2(0, -1)
        self.speed = TANK_SPEED
        self.controls = controls
        self.color = color
        self.bullets = pygame.sprite.Group()
        self.last_shot = 0
        self.shoot_delay = 250

    def update(self, dt):
        keys = pygame.key.get_pressed()
        movement = pygame.Vector2(0, 0)

        if keys[self.controls['left']]:
            movement.x = -1
        if keys[self.controls['right']]:
            movement.x = 1
        if keys[self.controls['up']]:
            movement.y = -1
        if keys[self.controls['down']]:
            movement.y = 1

        if movement.length_squared() > 0:
            movement = movement.normalize() * self.speed
            self.rect.move_ip(movement.x * dt, movement.y * dt)
            self.direction = movement.normalize()

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        if keys[self.controls['fire']]:
            self.shoot()

        self.bullets.update(dt)

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot < self.shoot_delay:
            return
        if len(self.bullets) >= MAX_BULLETS:
            return

        bullet_pos = self.rect.center + self.direction * 24
        bullet = Bullet(bullet_pos.x, bullet_pos.y, self.direction)
        self.bullets.add(bullet)
        self.last_shot = now

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        turret_rotated = pygame.transform.rotate(self.turret, -self.direction.angle_to(pygame.Vector2(0, -1)))
        turret_rect = turret_rotated.get_rect(center=self.rect.center)
        surface.blit(turret_rotated, turret_rect)
        self.bullets.draw(surface)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (4, 4), 4)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = BULLET_SPEED

    def update(self, dt):
        self.rect.move_ip(self.direction.x * self.speed * dt, self.direction.y * self.speed * dt)
        if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).contains(self.rect):
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tank Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)

        controls1 = {
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d,
            'fire': pygame.K_SPACE,
        }
        controls2 = {
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'fire': pygame.K_RETURN,
        }

        self.player1 = Tank(100, SCREEN_HEIGHT // 2, GREEN, controls1)
        self.player2 = Tank(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2, RED, controls2)

        self.walls = pygame.sprite.Group()
        self.walls.add(Wall(300, 150, 40, 200))
        self.walls.add(Wall(460, 250, 40, 200))

        self.all_sprites = pygame.sprite.Group(self.player1, self.player2, *self.walls)
        self.running = True
        self.winner = None

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 16
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        self.player1.update(dt)
        self.player2.update(dt)

        self.handle_collisions(self.player1)
        self.handle_collisions(self.player2)

        self.check_winner()

    def handle_collisions(self, tank):
        for bullet in tank.bullets:
            if pygame.sprite.spritecollideany(bullet, self.walls):
                bullet.kill()
                continue

            other_tank = self.player2 if tank is self.player1 else self.player1
            if bullet.rect.colliderect(other_tank.rect):
                bullet.kill()
                self.winner = 'Player 1' if tank is self.player1 else 'Player 2'
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.walls.draw(self.screen)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

        if self.winner:
            text = self.font.render(f'{self.winner} wins! Press ESC to quit.', True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
        else:
            title = self.font.render('Player 1: WASD + Space | Player 2: Arrows + Enter', True, WHITE)
            self.screen.blit(title, (10, 10))

        pygame.display.flip()

if __name__ == '__main__':
    Game().run()
