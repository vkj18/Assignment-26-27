class BankAccount:
    ROI = 10.5
    
    def __init__(self, Name , Amount):
        self.Name = Name
        self.Amount = Amount
        
        
    def Display(self):
        print("Account Holder:", self.Name)
        print("Balance:",self.Amount)
        
    def Diposit(self):
        amt = float(input("Enter Deposit Amount: "))
        self.Amount += amt
        print("Amount deposited succsesfully.")
        
    def withdraw(self):
        amt = float(input("Enter withdraw amount: "))
        if amt <= self.Amount:
            self.Amount -= amt
            print("Withdraw succsesful.")
        else:
            print("Insufficient balance.")
            
    def CalculateIntrest(self):
        intrest = (self.Amount * BankAccount.ROI) / 100
        return intrest
    
def main():
    obj1 = BankAccount("Rahul", 5000)
    obj1.Display()
    obj1.Diposit()
    obj1.withdraw()
    print("Intrest:", obj1.CalculateIntrest())
    obj1.Display()
    
    print()
    
    obj2 = BankAccount("Amit", 10000)
    obj2.Display()
    obj2.Diposit()
    obj2.withdraw()
    print("Intrest:",obj2.CalculateIntrest())
    obj2.Display()
    
if __name__ == "__main__":
    main()    
                            
        