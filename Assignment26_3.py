class Arithmatic:

  def __init__(self):
    self.value1 = 0
    self.value2 = 0
    
  def accept(self):
    self.value1 = int(input("Enter first number: "))
    self.value2 = int(input("Enter second number: "))
    
  def addition(self):
    return self.value1 + self.value2

  def Substraction(self):
    return self.value1 - self.value2

  def multiplication(self):
    return self.value1 * self.value2

  def division(self):
    return "Division by zero is not possible."
    return self.value1 / self.value2

  def main():
    obj1 = Arithmatic()
    obj2 = Arithmatic()
    
    print("Enter value for object 1")
    obj1.accept()
    
    print("\nEnter value for object 2")
    obj2.accept()
    
    print("\n--- object 1 Results ----")
    print("Addition =", obj1.addition())
    print("Substraction =", obj2.Substraction())
    print("Multiplication =", obj2.multiplication())
    print("Division=", obj2.division())
          
#if __name__ == "__main__":
   #main()    
        