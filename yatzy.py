class Yatzy:
    FIFTY = 50 
    ZERO = 0

    @staticmethod
    def chance(*dices):
        '''
        - A parameter list has too many parameters.
        . A middle man object isn't doing anything
        '''
        return sum(dices)

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
    
    @staticmethod
    def fours(*dices):
        FOUR = 4
        return dices.count(FOUR) * FOUR
    
    @staticmethod   
    def fives(*dices):
        FIVE = 5
        return dices.count(FIVE) * FIVE
    
    @staticmethod
    def sixes(*dices):
        SIX = 6
        return dices.count(SIX) * SIX
    
    @staticmethod
    def score_pair(*dices):
        TWO = 2

        highest_pair_value = 0
        for die in dices:
            if dices.count(die) >= TWO:
                highest_pair_value = max(highest_pair_value,die)

        return highest_pair_value * TWO if highest_pair_value != 0 else Yatzy.ZERO


    @staticmethod
    def two_pair(*dices):
        TWO = 2
        THREE = 3
        FOUR = 4

        pairs = []
        for die in dices:
            if dices.count(die) == TWO and die not in pairs:
                pairs.append(die)
            elif dices.count(die) == THREE and die not in pairs:
                pairs.append(die)
            elif dices.count(die) >= FOUR and die not in pairs:
                pairs.extend([die,die])

    
        return sum(pairs) * TWO if len(pairs) == TWO else Yatzy.ZERO


    
    @staticmethod
    def four_of_a_kind(*dices):
        FOUR = 4

        for die in dices:
            if dices.count(die) >= FOUR:
                return die * FOUR
            
        return Yatzy.ZERO
    

    @staticmethod
    def three_of_a_kind(*dices):
        THREE = 3

        for die in dices:
            if dices.count(die) >= THREE:
                return die * THREE
            
        return Yatzy.ZERO
    

    @staticmethod
    def smallStraight(*dices):
        FIFTEEN = 15
        STAIR = list(range(1,6))

        return FIFTEEN if sorted(dices) == STAIR else Yatzy.ZERO
    

    @staticmethod
    def largeStraight(*dices):
        TWENTY = 20

        return TWENTY if sorted(dices) == [2,3,4,5,6] else Yatzy.ZERO
        
    

    @staticmethod
    def fullHouse(*dices):
        TWO = 2
        THREE = 3

        full = []
        for die in dices:
            if dices.count(die) == TWO and die not in full:
                full.append(die)
            if dices.count(die) == THREE and die not in full:
                full.append(die)

    
        return sum(dices) if len(full) == TWO else Yatzy.ZERO