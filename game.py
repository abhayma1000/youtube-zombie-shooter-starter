import time
import pygame
import sys
from bullet import *
from characters import *
import random
from util import *
from walls import *


class ZombieShooter():
    def __init__(self, window_width, window_height, world_height, world_width, fps, sound=False):
        self.window_width = window_width
        self.window_height = window_height
        self.world_height = world_height
        self.world_width = world_width

        self.treasure_chest = None
        self.health_drop = None

        self.paused = False

        self.gun_type = "single"
        self.fire_mode = "single"

        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))

        pygame.display.set_caption("Zombie shooter")

        self.font = pygame.font.SysFont(None, 36)

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.walls = walls_1

        # TODO: Define player

        self.background_color = (101, 101, 29)
        self.wall_color = (1, 50, 32)
        self.border_color = (255, 0, 0)

        self.announcement_font = pygame.font.SysFont(None, 100)

        self.bullets = []
        self.zombies = []

        self.zombie_top_speed = 1
        self.level_goal = 5
        self.max_zombie_count = 5
        self.level = 1
        self.sound = sound
    
    def fill_background(self):
        self.screen.fill(self.background_color)

        # TODO set player stats
        level_surface = self.font.render(f"Level: {self.level}", True, (0, 0, 0))
        self.screen.blit(level_surface, (10, 60))

        # TODO: Set ammo message and gun type
    
    def step(self):
        print("Playing zombies...")
        self.fill_background()
        time.sleep(1)

        pygame.display.flip() # Updates display