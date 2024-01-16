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
        TWO = 2
        
        two_pairs = cls._filter_repeated_pips(dices,TWO)
        return sum(two_pairs) * TWO if len(two_pairs) == 2 else Yatzy.ZERO

    
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