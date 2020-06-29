from collections import defaultdict
from environment import GameObject, KeyItem, Structure

import numpy as np


power_piece = GameObject({"ATK_UP": 1, "REPR": "p"})
power_gem = GameObject({"ATK_UP": 2, "REPR": "P"})
guard_piece = GameObject({"DEF_UP": 1, "REPR": "g"})
guard_gem = GameObject({"DEF_UP": 2, "REPR": "G"})
life_potion = GameObject({"HP_UP": 2000, "REPR": "L"})
guard_potion = GameObject({"HP_UP": 300, "DEF_UP": 3, "REPR": "U"})
power_potion = GameObject({"HP_UP": 300, "ATK_UP": 3, "REPR": "O"})
red_potion = GameObject({"HP_UP": 200, "REPR": "r"})
blue_potion = GameObject({"HP_UP": 800, "REPR": "b"})
heavenly_potion = GameObject({"HP_UP": 3000, "ATK_UP": 3, "DEF_UP": 3, "REPR": "H"})
yellow_lock = GameObject({"REQUIRES_KEYITEM": KeyItem.YELLOW_KEY, "REPR": "K"})
yellow_key = GameObject({"GIVES_KEYITEM": (KeyItem.YELLOW_KEY, 1), "REPR": "L"})
grey_wall = GameObject({"STRUCTURE": Structure.WALL, "REPR": "█"})
up_stairs = GameObject({"STRUCTURE": Structure.UP_STAIRS, "REPR": ">"})
down_stairs = GameObject({"STRUCTURE": Structure.DOWN_STAIRS, "REPR": "<"})

junior_fighter = GameObject({"HP": 120, "ATK": 55, "DEF": 25, "EXP": 2, "REPR": "q"})
fighter = GameObject({"HP": 320, "ATK": 110, "DEF": 40, "EXP": 5, "REPR": "w"})
elder_fighter = GameObject({"HP": 600, "ATK": 145, "DEF": 65, "EXP": 10, "REPR": "e"})
junior_ranger = GameObject({"HP": 200, "ATK": 200, "DEF": 10, "EXP": 4, "REPR": "a"})
ranger = GameObject({"HP": 200, "ATK": 350, "DEF": 20, "EXP": 16, "REPR": "s"})

Tactical_tutorial_board = np.full((5, 2, 15, 15), GameObject(), dtype=GameObject)
Tactical_tutorial_board[0, 1, [4, 5, 5, 6], [6, 5, 7, 6]] = power_piece
Tactical_tutorial_board[0, 1, [5, 5, 7, 9], [6, 10, 3, 10]] = power_gem
Tactical_tutorial_board[0, 1, [7, 7, 7, 7, 8, 9, 9, 10, 5, 5, 9, 9], [6, 8, 10, 11, 6, 5, 7, 6, 8, 11, 8, 11]] = guard_piece
Tactical_tutorial_board[0, 1, [9, 3, 4, 3], [6, 7, 8, 9]] = guard_gem
Tactical_tutorial_board[0, 1, 3, 8] = guard_potion
Tactical_tutorial_board[0, 1, 11, 8] = power_potion
Tactical_tutorial_board[0, 1, [3, 6, 8, 11, 4, 5, 9, 10], [10, 12, 12, 10, 12, 13, 13, 12]] = red_potion
Tactical_tutorial_board[0, 1, [6, 7, 8], [8, 7, 8]] = blue_potion
Tactical_tutorial_board[0, 1, 7, 9] = heavenly_potion
Tactical_tutorial_board[0, 1, 7, 12] = yellow_key
Tactical_tutorial_board[0, 1, 7, 13] = yellow_lock
Tactical_tutorial_board[0, 1, [7, 5, 9], [4, 12, 12]] = life_potion

Tactical_tutorial_board[0, 1, [2, 12], 7:12] = grey_wall
Tactical_tutorial_board[0, 1, [3, 11], 6:13:6] = grey_wall
Tactical_tutorial_board[0, 1, [4, 10], 5:14:2] = grey_wall
Tactical_tutorial_board[0, 1, [5, 9], 4:15:10] = grey_wall
Tactical_tutorial_board[0, 1, [6, 8], 5:14:2] = grey_wall
Tactical_tutorial_board[0, 1, [6, 8], 0:5] = grey_wall
Tactical_tutorial_board[0, 1, [6, 8], 14] = grey_wall
Tactical_tutorial_board[0, 1, 7, 14] = up_stairs

Tactical_tutorial_board[0, 0, [3, 11], 10] = junior_ranger
Tactical_tutorial_board[0, 0, [6, 8], 12] = ranger
Tactical_tutorial_board[0, 0, [5, 7, 7, 7, 9], [11, 6, 8, 10, 11]] = junior_fighter
Tactical_tutorial_board[0, 0, [5, 7, 9], [8, 11, 8]] = fighter
