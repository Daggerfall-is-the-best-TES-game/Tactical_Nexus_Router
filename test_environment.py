from collections import defaultdict
from unittest import TestCase

from agent import Agent
from environment import GameObject, KeyItem


class TestGameObject(TestCase):
    def test_engage(self):
        leveling_plan = defaultdict(lambda: "ATK")

        def stat_for_level(level, stat):
            if stat == "ATK":
                return level + 3
            elif stat == "DEF":
                return 2 * (level + 3)
            else:
                raise Exception

        stats = defaultdict(int,
                            {"HP": 1000, "ATK": 50, "HP_MULT": 1.0, "EXP_MULT": 1.0, "STAT_FOR_LVL": stat_for_level,
                             "LV": 1})
        agent = Agent(stats, leveling_plan)
        print(agent.statistics)
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

        agent = power_gem.engage(agent)
        agent = life_potion.engage(agent)
        agent = junior_fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = blue_potion.engage(agent)
        agent = junior_fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = heavenly_potion.engage(agent)
        agent = junior_fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = yellow_key.engage(agent)
        agent = yellow_lock.engage(agent)
        agent = heavenly_potion.engage(agent)
        agent = junior_fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = power_potion.engage(agent)
        agent = blue_potion.engage(agent)
        agent = junior_ranger.engage(agent)
        agent = red_potion.engage(agent)
        agent = life_potion.engage(agent)
        agent = power_gem.engage(agent)
        agent = fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = blue_potion.engage(agent)
        agent = fighter.engage(agent)
        agent = guard_piece.engage(agent)
        agent = guard_piece.engage(agent)
        agent = guard_piece.engage(agent)
        agent = guard_piece.engage(agent)
        agent = guard_piece.engage(agent)
        agent = power_gem.engage(agent)
        agent = heavenly_potion.engage(agent)
        agent = power_potion.engage(agent)
        agent = ranger.engage(agent)
        agent = red_potion.engage(agent)
        agent = power_potion.engage(agent)
        agent = blue_potion.engage(agent)
        agent = elder_fighter.engage(agent)
        agent = guard_gem.engage(agent)
        self.assertEqual(agent.statistics, {'HP': 8246, 'ATK': 85, 'HP_MULT': 1.0, 'EXP_MULT': 1.0,
                                                'STAT_FOR_LVL': stat_for_level, 'LV': 3, 'DEF': 22, 'EXP': 13,
                                                KeyItem.YELLOW_KEY: 0})
