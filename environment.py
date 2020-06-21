from enum import Enum
from math import ceil

from agent import Agent
from typing import Union


class KeyItem(Enum):
    YELLOW_KEY = 0
    BLUE_KEY = 1
    CRIMSON_KEY = 2
    ICE_KEY = 3
    MATTOCK = 4
    VIOLET_KEY = 5
    PLATINUM_KEY = 6
    GLORY_KEY = 7
    WINNER_KEY = 8
    RETURN_KEY = 9


class GameObject:
    def __init__(self, statistics):
        """
        :param statistics:a default dictionary (default 0) that contains a subset of the following:
        HP - Amount of HP an object has
        ATK - Amount of ATK an object has
        DEF - Amount of DEF an object has
        EXP_UP - Amount of EXP an object gives
        ATK_UP - Amount of ATK an object gives
        DEF_UP - Amount of DEF an object gives
        HP_UP - Amount of HP an object gives
        HP_MULT_UP - Amount of HP_MULT an object gives
        EXP_MULT_UP -  Amount of EXP_MULT an object gives
        REQUIRES_KEYITEM - type of keyitem an object takes, as an enum
        GIVES_KEYITEM - tuple containing type of keyitem an object gives, as an enum, then quantity given (KeyItem, int)
        """
        self.statistics = statistics

    def engage(self, agent) -> Union[bool, Agent]:
        """makes a copy of agent, simulates its interaction with this GameObject
        returns that agent, if move is possible, otherwise returns false"""
        new_agent_stats = agent.statistics.copy()

        if self.statistics["HP"] > 0:  # enemies
            # simulate battle
            if new_agent_stats["ATK"] <= self.statistics["DEF"]:
                return False
            if new_agent_stats["DEF"] < self.statistics["ATK"]:
                new_agent_stats["HP"] -= (ceil(self.statistics["HP"] /
                                               (new_agent_stats["ATK"] - self.statistics["DEF"])) - 1) *\
                                         (self.statistics["ATK"] - new_agent_stats["DEF"])
            new_agent_stats["EXP"] += int(new_agent_stats["EXP_MULT"] * self.statistics["EXP"])
            if new_agent_stats["HP"] <= 0:
                return False
        elif self.statistics["REQUIRES_KEYITEM"]:  # lock or wall
            # uses key item
            if not new_agent_stats[self.statistics["REQUIRES_KEYITEM"]]:
                return False
            new_agent_stats[self.statistics["REQUIRES_KEYITEM"]] -= 1
        elif self.statistics["GIVES_KEYITEM"]:
            new_agent_stats[self.statistics["GIVES_KEYITEM"][0]] += self.statistics["GIVES_KEYITEM"][1]
        else:  # stat increase item
            new_agent_stats["ATK"] += self.statistics["ATK_UP"]
            new_agent_stats["DEF"] += self.statistics["DEF_UP"]
            new_agent_stats["HP"] += int(new_agent_stats["HP_MULT"] * self.statistics["HP_UP"])

        new_agent = Agent(new_agent_stats, agent.leveling_plan)
        new_agent.level_up()
        return new_agent
