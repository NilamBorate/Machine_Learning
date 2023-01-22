
class Arithmatic:
    
    def __init__(self,A,B):
        print("Inside init method")
        self.No1=A
        self.No2=B

    def Addition(self):
        Ans=self.No1+self.No2
        return Ans

    def Substraction(self):
        Ans=self.No1-self.No2
        return Ans


def main():
    print("Inside main Method")

    obj=Arithmatic(11,10)
    
    Add=obj.Addition()
    print("Addition is : ",Add)
    
    Sub=obj.Substraction()
    print("Substraction is : ",Sub)

    objX=Arithmatic(21,20)

if __name__=="__main__":
    print("Inside Starter")
    main()    