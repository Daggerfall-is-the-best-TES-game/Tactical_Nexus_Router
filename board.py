from collections import defaultdict
from environment import GameObject, KeyItem

import numpy as np


power_piece = GameObject(defaultdict(int, {"ATK_UP": 1, "REPR": "p"}))
power_gem = GameObject(defaultdict(int, {"ATK_UP": 2, "REPR": "P"}))
guard_piece = GameObject(defaultdict(int, {"DEF_UP": 1, "REPR": "g"}))
guard_gem = GameObject(defaultdict(int, {"DEF_UP": 2, "REPR": "G"}))
life_potion = GameObject(defaultdict(int, {"HP_UP": 2000, "REPR": "L"}))
power_potion = GameObject(defaultdict(int, {"HP_UP": 300, "ATK_UP": 3, "REPR": "O"}))
red_potion = GameObject(defaultdict(int, {"HP_UP": 200, "REPR": "r"}))
blue_potion = GameObject(defaultdict(int, {"HP_UP": 800, "REPR": "b"}))
heavenly_potion = GameObject(defaultdict(int, {"HP_UP": 3000, "ATK_UP": 3, "DEF_UP": 3, "REPR": "H"}))
yellow_lock = GameObject(defaultdict(int, {"REQUIRES_KEYITEM": KeyItem.YELLOW_KEY, "REPR": "K"}))
yellow_key = GameObject(defaultdict(int, {"GIVES_KEYITEM": (KeyItem.YELLOW_KEY, 1), "REPR": "L"}))

junior_fighter = GameObject(defaultdict(int, {"HP": 120, "ATK": 55, "DEF": 25, "EXP": 2, "REPR": "q"}))
fighter = GameObject(defaultdict(int, {"HP": 320, "ATK": 110, "DEF": 40, "EXP": 5, "REPR": "w"}))
elder_fighter = GameObject(defaultdict(int, {"HP": 600, "ATK": 145, "DEF": 65, "EXP": 10, "REPR": "e"}))
junior_ranger = GameObject(defaultdict(int, {"HP": 200, "ATK": 200, "DEF": 10, "EXP": 4, "REPR": "a"}))
ranger = GameObject(defaultdict(int, {"HP": 200, "ATK": 350, "DEF": 20, "EXP": 16, "REPR": "s"}))

Tactical_tutorial_board = np.full((5, 2, 15, 15), GameObject(), dtype=GameObject)
Tactical_tutorial_board[[0, 0, 0, 0], [1, 1, 1, 1], [4, 5, 5, 6], [6, 5, 7, 6]] = power_piece


