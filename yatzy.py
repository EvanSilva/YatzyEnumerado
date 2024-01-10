class Yatzy:
    FIFTY = 50 
    ZERO = 0

    @staticmethod
    def chance(*dices):
        '''
        - A parameter list has too many parameters.

        '''
        total = 0
        for die in dices:
            total += die
        return total

    @staticmethod
    def yatzy(*dices):
        if all(die == dices[0] for die in dices):
                return Yatzy.FIFTY
        else:
                return Yatzy.ZERO
    
    @staticmethod
    def ones(*dices):
        '''
        - Replace a magic number with a named constant.
        - Code is too long.
        '''
        ONE = 1
        return dices.count(ONE) * ONE

    @staticmethod
    def twos(*dices):
        TWO = 2
        return dices.count(TWO) * TWO
    
    @staticmethod
    def threes(*dices):
        THREE = 3
        return dices.count(THREE) * THREE
    
    def __init__(self, *dices):
        self.dice = list(dices)
    
    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR
    

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE
    

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX
    
    @staticmethod
    def score_pair(*dices):
        TWO = 2

        highest_pair_value = 0
        for die in dices:
            if dices.count(die) == TWO:
                highest_pair_value = max(highest_pair_value,die)

        if highest_pair_value != 0:
            return highest_pair_value * TWO
        else:
            return Yatzy.ZERO
    
    @staticmethod
    def two_pair(*dices):
        TWO = 2
        THREE = 3

        pairs = []
        for die in dices:
            if dices.count(die) == TWO and die not in pairs:
                pairs.append(die)
            if dices.count(die) == THREE and die not in pairs:
                pairs.append(die)

        if len(pairs) == TWO:
            return sum(pairs) * TWO 
        else:
            return Yatzy.ZERO


    
    @staticmethod
    def four_of_a_kind(*dices):
        FOUR = 4
        FIVE = 5

        for die in dices:
            if dices.count(die) == FOUR or dices.count(die) == FIVE:
                return die * FOUR
            
        return Yatzy.ZERO
    

    @staticmethod
    def three_of_a_kind(*dices):
        THREE = 3
        FOUR = 4

        for die in dices:
            if dices.count(die) == THREE or dices.count(die) == FOUR:
                return die * THREE
        return Yatzy.ZERO
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
