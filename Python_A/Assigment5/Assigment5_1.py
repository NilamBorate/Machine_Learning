#Program to demonstarte the concept of class and init constructor fundamental

class Demo:
    value=10
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
    def Fun(self):
        print("Values of no1 and no2 in Fun :",self.i,self.j)
    def Gun(self):
        print("Values of no1 and no2 in Gun :",self.i,self.j)

def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)
    
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()
       
if __name__=="__main__":
    main()