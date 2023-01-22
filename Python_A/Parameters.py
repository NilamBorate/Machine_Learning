#Positinal arguments/Keyword arguments
def Add1(No1,No2):
    print("Valiue of No1 : ",No1)
    print("Value of No2: ",No2)
    return No1+No2

def Sub1(No1,No2):
    print("Valiue of No1 : ",No1)
    print("Value of No2: ",No2)
    return No1-No2    



def main():
 
    Ans=Add1(10,11)       #positional argument
    print("Addition is : ",Ans)

    Ans=Sub1(No2=10,No1=11)   #keyword argument
    print("Substraction is : ",Ans)

    Ans=Sub1(No1=10,No2=11)   #keyword argument
    print("Substraction is : ",Ans)
    

if __name__=="__main__":
    main()
