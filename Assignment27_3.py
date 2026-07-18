class Numbers:
    def __init__(self, Value):
        self.Value = Value
        
    def Chkprime(self):
        if self.Value < 2:
            return False
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
                
        if sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors are:")
        for i in range(self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()
        
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i
        return sum
    
    
def main():
    obj1 = Numbers(28)
    
    print("Prime:", obj1.Chkprime())
    print("Perfect:", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors:",
obj1.SumFactors())
    
    print()
    
    obj2 = Numbers(17)
    
    print("Prime:", obj2.Chkprime())
    print("Perfect:", obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors:",
obj2.SumFactors())
    
    
if __name__ == "__main__":
    main()                            
            
                        