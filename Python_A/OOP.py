#Accept two number and perform addition and substraction of it

#1.kay karaychay ?                            ->Behaviour(functions)
#   Addition and substraction 

#2.je karaychay te karayla kay lagnaray ?     ->Characteristics(Data) 
#   Two numbers 

#Class = Characteristics + Behaviour
#Class = Data + Functions

class Arithmatic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B

    def Add(sel:f):
        return self.No1+ self.No2


    def Sub(self)
        return self.No1 - self.No2    

def main():
    print("Enter first number: ")
    Value1=int(input())

    print("Enter second number: ")
    Value2=int(input())

    obj=Arithmatic(Value1,Value2)

    Ans =obj.Add()
    print("Addition is : ",Ans)

    Ans =obj.Sub()
    print("Substraction is : ",Ans)

   

if __name__=="__main__":
    main()    