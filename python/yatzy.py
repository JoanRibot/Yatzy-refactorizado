class Yatzy:


    def __init__(self,*dices):
        self.dices = list(dices)
    
    @staticmethod
    def chance(*dices):
        total = 0
        for i in dices:
            total +=i
        return total

    @staticmethod
    def yatzy(*dices):
        for i in dices:
            if dices.count(i) == 5: 
                return 50
        return 0
    
    def SumSameNumber(number, dices):
        total=number*dices.count(number)
        return total
    
    @staticmethod
    def ones(*dices):
        return Yatzy.SumSameNumber(1,dices)

    
    @staticmethod
    def twos(*dices):
        return Yatzy.SumSameNumber(2,dices)
    
    @staticmethod
    def threes(*dices):
        return Yatzy.SumSameNumber(3,dices)
    
    def fours(self):
        return Yatzy.SumSameNumber(4,self.dices)
    

    def fives(self):
        return Yatzy.SumSameNumber(5,self.dices)
    

    def sixes(self):
        return Yatzy.SumSameNumber(6,self.dices)
    
    @staticmethod
    def score_pair(*dices):
        pair=2
        for i in range(6,0,-1):
            if dices.count(i) >= pair:
                return i * 2
        return 0

            
    
    @staticmethod
    def two_pair(*dices):
        sum=0
        contador=0
        pair=2
        for i in range(6,0,-1):
            if dices.count(i) >= pair:
                sum+= i * 2
                contador +=1
                if contador==2:
                    return sum
        return 0



    
    @staticmethod
    def four_of_a_kind(*dices):
        cuadra=4
        for i in range(6,0,-1):
            if dices.count(i) >= cuadra:
                return i * 4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dices):
        triple=3
        for i in range(6,0,-1):
            if dices.count(i) >= triple:
                return i * 3
        return 0
    

    @staticmethod
    def smallStraight(*dices):
        if sorted(dices) == [1,2,3,4,5]:
            return 15
        return 0
    

    @staticmethod
    def largeStraight(*dices):
        if sorted(dices) == [2,3,4,5,6]:
            return 20
        return 0

    @staticmethod
    def fullHouse(*dices):
        def par(*dices):
            pair=2
            for i in range(6,0,-1):
                if dices.count(i)== pair:
                    return i*2
                else:
                    return 0
        if par(*dices) and Yatzy.three_of_a_kind(*dices):
            return par(*dices) + Yatzy.three_of_a_kind(*dices)
        return 0
 
