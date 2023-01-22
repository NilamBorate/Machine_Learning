#Program to Calculate the area of a circle using OOP approach

class Circle:
    PI=3.14
    
    def __init__(self,Radius,Area,Circumference):
        self.Radius=0
        self.Area=0
        self.Circumference=0
        
        
    def Accept(self):
        print("Enter the radius : ")
        self.Radius=int(input())
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
        print("Area is : ",self.Area)
        
    def CalculateCircumference(self):
        self.Circumference=int(2)*Circle.PI*self.Radius
        print("Circumference os a circle is : ",self.Circumference)
        
    def Disply(self):
        print("Inside the Disply method")
        print("Radius of a circle is ",self.Radius)
        print("Area of a circle is ",self.Area)
        print("Circumference of a circle is ",self.Circumference)
    
def main():
    
    obj1=Circle(0,0,0)
    
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Disply()
    
    
    
if __name__=="__main__":
    main()
    