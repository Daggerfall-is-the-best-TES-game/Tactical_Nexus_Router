class Agent:
    def __init__(self, statistics):
        """
        :param statistics: default dictionary (default 0) that contains a subset of the following:
        HP - Amount of HP the agent has
        ATK - Amount of ATK the agent has
        DEF - Amount of DEF the agent has
        EXP - Amount of EXP the agent has
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
        """
        self.statistics = statistics
