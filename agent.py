from math import comb


class Agent:
    def __init__(self, statistics, leveling_plan):
        """
        :param statistics: default dictionary (default 0) that contains a subset of the following:
        HP - Amount of HP the agent has
        ATK - Amount of ATK the agent has
        DEF - Amount of DEF the agent has
        EXP - Amount of EXP the agent has
        LV - the level of the agent
        HP_MULT - multiplicative factor on acquired HP
        EXP_MULT - multiplicative factor on acquired EXP
        KeyItem.YELLOW_KEY - Amount of yellow keys the agent has
        KeyItem.BLUE_KEY - Amount of blue keys the agent has
        KeyItem.CRIMSON_KEY - Amount of crimson keys the agent has
        KeyItem.ICE_KEY - Amount of ice keys the agent has
        KeyItem.MATTOCK - Amount of mattocks the agent has
        KeyItem.VIOLET_KEY - Amount of violet keys the agent has
        KeyItem.PLATINUM_KEY - Amount of platinum keys the agent has
        KeyItem.GLORY_KEY - Amount of glory keys the agent has
        KeyItem.WINNER_KEY - Amount of winner keys the agent has
        KeyItem.RETURN_KEY - Amount of return keys the agent has
        STAT_FOR_LVL - function that takes an integer LEVEL and a STAT and returns how much STAT is gained
        by a level LEVEL character on level_up
        :param leveling_plan: dictionary from levels to levelup upgrades. levels start at level 2
        """
        self.statistics = statistics
        self.leveling_plan = leveling_plan

    def level_up(self):
        level_ups = 0

        def triangular_number(index):
            return comb(index + 1, 2)

        def tetrahedral_number(index):
            return comb(index + 2, 3)

        while self.statistics["EXP"] >= 10 * (triangular_number(self.statistics["LV"] + level_ups) +
                                              tetrahedral_number(self.statistics["LV"] + level_ups - 1) -
                                              tetrahedral_number(self.statistics["LV"] - 1)):
            level_ups += 1

        # statistics updates
        self.statistics["EXP"] -= 10 * (tetrahedral_number(self.statistics["LV"] + level_ups - 1) -
                                        tetrahedral_number(self.statistics["LV"] - 1))

        for level in range(self.statistics["LV"] + 1, self.statistics["LV"] + level_ups + 1):
            self.statistics[self.leveling_plan[level]] += self.statistics["STAT_FOR_LVL"](level,
                                                                                          self.leveling_plan[level])

        self.statistics["LV"] += level_ups
