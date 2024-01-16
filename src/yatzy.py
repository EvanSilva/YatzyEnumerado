from src.pips import Pips

class Yatzy:

    FIFTY = 50 
    ZERO = 0

    @staticmethod
    def chance(*dices):
        return sum(dices)

    @staticmethod
    def yatzy(*dices):
        if all(die == dices[0] for die in dices):
                return Yatzy.FIFTY
        else:
                return Yatzy.ZERO
        
    @classmethod
    def __pip_filter(cls, dices, target):
        return dices.count(target) * target
    
    @classmethod
    def ones(cls,*dices):
        ONE = Pips.ONE.value
        return cls.__pip_filter(dices,ONE)  

    @classmethod
    def twos(cls,*dices):
        TWO = Pips.TWO.value
        return cls.__pip_filter(dices,TWO)
    
    @classmethod
    def threes(cls,*dices):
        THREE = Pips.THREE.value
        return cls.__pip_filter(dices,THREE)
    
    @classmethod
    def fours(cls,*dices):
        FOUR = Pips.FOUR.value
        return cls.__pip_filter(dices,FOUR)
        
    @classmethod   
    def fives(cls,*dices):
        FIVE = Pips.FIVE.value
        return cls.__pip_filter(dices,FIVE)
    
    @classmethod
    def sixes(cls,*dices):
        SIX = Pips.SIX.value
        return cls.__pip_filter(dices,SIX)
    
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
        STAIR = list(range(1,6))

        return sum(dices) if sorted(dices) == STAIR else Yatzy.ZERO
    

    @staticmethod
    def largeStraight(*dices):
        STAIR = list(range(2,7))

        return sum(dices) if sorted(dices) == STAIR else Yatzy.ZERO
        
    

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