 #Application to find out the maximum number

def Max(No1,No2):
    if(No1>No2):
        return No1
    else:
        return No2


def main():
    print("Enter first number :")
    value1=input()

    print("Enter second number : ")
    value2=input()
 
    Ans=Max(int(value1),int(value2))

    print("Largest number is ",Ans)
    

if __name__=="__main__":
    main()