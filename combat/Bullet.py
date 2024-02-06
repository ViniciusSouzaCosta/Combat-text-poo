from random import random
import Tank
import game
import Labyrinth

def shoot(self, shooter, target):
    hit_chance = 0.5
    distance = abs(shooter.x - target.x) + abs(shooter.y - target.y)

    if distance == 1:
        hit_chance = 0.8
    elif distance == 2:
        hit_chance = 0.6
    return random.random() < hit_chance