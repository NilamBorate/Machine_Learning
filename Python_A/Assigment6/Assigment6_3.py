
class Numbers:
    def __init__(self):
        print("Enter a value: ")
        self.Value=int(input())

    def Factors(self):
        for i in range(1,int((self.Value/2)+1)):
            if(self.Value%i==0):
                 print(i)
               
                    
    def SumFactors(self):
        Sum=0
        for i in range(1,int((self.Value/2)+1)):
            if(self.Value%i==0):
                Sum=Sum+i
        return Sum


    def CheckPerfect(self):
        Ans=self.SumFactors()

        if(self.Value==Ans):
            return True
        else:
            return False   

        
    def CheckPrime(self):
        i=0
        Flag=True

        for i in range(2,int(self.Value/2)+1):
            if(self.Value%i==0):
                Flag=False
                break
        return Flag

def main():

    obj=Numbers()
    print("Factors of a number are : ")
    fact=obj.Factors()
    

    Out=obj.SumFactors()
    print("Sum of a factors is : ",Out)


    Ret=obj.CheckPerfect()
    if (Ret==True):
        print("{} is a perfect number ".format(obj.Value))
    else:
        print("{} is not a perfect  number ".format(obj.Value))  


    Ret=obj.CheckPrime()
    if (Ret==True):
        print("{} is a prime number ".format(obj.Value))
    else:
        print("{} is not a prime number ".format(obj.Value))

if __name__=="__main__":
    main()    