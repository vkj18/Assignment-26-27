class Bookstore:
    NoOfBooks = 0
    
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        Bookstore.NoOfBooks += 1
        
    def Display(self):
        print(self.Name, "by", self.Author + ".", "No of books:", Bookstore.NoOfBooks)
        
def main():
    obj1 = Bookstore("Linux System programing", "Robert Love")
    obj1.Display()
    
    obj2 = Bookstore("C programing", "Dennis Ritchie")
    obj2.Display()
    
if __name__ == "__main__":
    main()                
        