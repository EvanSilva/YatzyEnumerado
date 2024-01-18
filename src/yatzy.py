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
    def __pip_counter(cls, dices, target):
        return dices.count(target) * target
    
    @classmethod
    def ones(cls,*dices):
        ONE = Pips.ONE.value
        return cls.__pip_counter(dices,ONE)  

    @classmethod
    def twos(cls,*dices):
        TWO = Pips.TWO.value
        return cls.__pip_counter(dices,TWO)
    
    @classmethod
    def threes(cls,*dices):
        THREE = Pips.THREE.value
        return cls.__pip_counter(dices,THREE)
    
    @classmethod
    def fours(cls,*dices):
        FOUR = Pips.FOUR.value
        return cls.__pip_counter(dices,FOUR)
        
    @classmethod   
    def fives(cls,*dices):
        FIVE = Pips.FIVE.value
        return cls.__pip_counter(dices,FIVE)
    
    @classmethod
    def sixes(cls,*dices):
        SIX = Pips.SIX.value
        return cls.__pip_counter(dices,SIX)
    
    @classmethod
    def _filter_repeated_pips(cls,dices,times):
        return list(filter(lambda x: dices.count(x) >= times,Pips.values()))
        
    @classmethod
    def score_pair(cls, *dices):
        TWO = Pips.TWO.value

        pairs = cls._filter_repeated_pips(dices,TWO)
        return pairs[-1] * TWO if pairs else Yatzy.ZERO


    @classmethod
    def two_pair(cls,*dices):
        TWO = Pips.TWO.value
        
        two_pairs = cls._filter_repeated_pips(dices,TWO)
        return sum(two_pairs) * TWO if len(two_pairs) == 2 else Yatzy.ZERO
    
    @classmethod
    def three_of_a_kind(cls,*dices):
        THREE = Pips.THREE.value

        trio = cls._filter_repeated_pips(dices,THREE)
        return trio[-1] * THREE if trio else Yatzy.ZERO

    @classmethod
    def four_of_a_kind(cls,*dices):
        FOUR = Pips.FOUR.value

        poker = cls._filter_repeated_pips(dices,FOUR)
        return poker[-1] * FOUR if poker else Yatzy.ZERO

    @classmethod
    def smallStraight(cls,*dices):
        STAIR = list(range(1,6))

        return cls.chance(*dices) if sorted(dices) == STAIR else Yatzy.ZERO
    

    @classmethod
    def largeStraight(cls,*dices):
        STAIR = list(range(2,7))

        return cls.chance(*dices) if sorted(dices) == STAIR else Yatzy.ZERO
        
    

    @classmethod
    def fullHouse(cls,*dices):
        TWO = Pips.TWO.value
        THREE = Pips.THREE.value

        pair = cls._filter_repeated_pips(dices,TWO)
        trio = cls._filter_repeated_pips(dices,THREE)

    
        return (pair[-1] * TWO) + (trio[-1] * THREE) if (pair and trio) else Yatzy.ZERO