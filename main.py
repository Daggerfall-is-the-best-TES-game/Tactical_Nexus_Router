from collections import defaultdict
from agent import Agent, Level
from environment import GameObject

if __name__ == "__main__":
    leveling_plan = defaultdict(lambda x: Level.ATK)
    stats = defaultdict(int, {"HP": 1000, "ATK": 50, "HP_MULT": 1.0, "EXP_MULT": 1.0})
    agent = Agent(stats, leveling_plan)
    print(agent.statistics)
    power_gem = GameObject(defaultdict(int, {"ATK_UP": 2}))
    guard_gem = GameObject(defaultdict(int, {"DEF_UP": 2}))
    life_potion = GameObject(defaultdict(int, {"HP_UP": 2000}))
    junior_fighter = GameObject(defaultdict(int, {"HP": 120, "ATK": 55, "DEF": 25, "EXP": 2}))
    elder_fighter = GameObject(defaultdict(int, {"HP": 600, "ATK": 145, "DEF": 65, "EXP": 10}))
    agent = power_gem.engage(agent)
    agent = life_potion.engage(agent)
    agent = junior_fighter.engage(agent)

    print(agent.statistics)
