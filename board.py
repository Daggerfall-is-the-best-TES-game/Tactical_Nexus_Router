from collections import defaultdict
from environment import GameObject, KeyItem

import numpy as np


power_piece = GameObject(defaultdict(int, {"ATK_UP": 1}))
power_gem = GameObject(defaultdict(int, {"ATK_UP": 2}))
guard_piece = GameObject(defaultdict(int, {"DEF_UP": 1}))
guard_gem = GameObject(defaultdict(int, {"DEF_UP": 2}))
life_potion = GameObject(defaultdict(int, {"HP_UP": 2000}))
power_potion = GameObject(defaultdict(int, {"HP_UP": 300, "ATK_UP": 3}))
red_potion = GameObject(defaultdict(int, {"HP_UP": 200}))
blue_potion = GameObject(defaultdict(int, {"HP_UP": 800}))
heavenly_potion = GameObject(defaultdict(int, {"HP_UP": 3000, "ATK_UP": 3, "DEF_UP": 3}))
yellow_lock = GameObject(defaultdict(int, {"REQUIRES_KEYITEM": KeyItem.YELLOW_KEY}))
yellow_key = GameObject(defaultdict(int, {"GIVES_KEYITEM": (KeyItem.YELLOW_KEY, 1)}))

junior_fighter = GameObject(defaultdict(int, {"HP": 120, "ATK": 55, "DEF": 25, "EXP": 2}))
fighter = GameObject(defaultdict(int, {"HP": 320, "ATK": 110, "DEF": 40, "EXP": 5}))
elder_fighter = GameObject(defaultdict(int, {"HP": 600, "ATK": 145, "DEF": 65, "EXP": 10}))
junior_ranger = GameObject(defaultdict(int, {"HP": 200, "ATK": 200, "DEF": 10, "EXP": 4}))
ranger = GameObject(defaultdict(int, {"HP": 200, "ATK": 350, "DEF": 20, "EXP": 16}))

Tactical_tutorial_board = np.empty((15, 15, 2, 5), dtype=GameObject)
Tactical_tutorial_board[[5, 6, 6, 7], [8, 9, 9, 10], [1, 1, 1, 1], [0, 0, 0, 0]] = power_piece


