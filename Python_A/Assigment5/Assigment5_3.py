#Program to find the addition ,substraction,multiplication and division of a two numbers using OOP approch

class Arithmetic:
    
    def __init__(self,Value1,Value2):
        self.Value1=0
        self.Value2=0
        
    def Accept(self):
        self.Value1=int(input("Enter the first value: "))
        self.Value2=int(input("Enter the second  value: "))
        
    def Addition(self):
        print("Addition of numbers is : ",self.Value1+self.Value2)
        
    def Substraction(self):
        print("Substraction of numbers is : ",self.Value1-self.Value2)
        
    def Multiplication(self):
        print("Multiplication of numbers is : ",self.Value1*self.Value2)
        
    def Division(self):
        print("Division of numbers is : ",self.Value1/self.Value2)
            
                   
def main():
    obj1=Arithmetic(0,0)
    obj1.Accept()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()
    
if __name__=="__main__":
    main()
        