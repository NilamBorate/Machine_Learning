#5
# 5 * 4 * 3 * 2 * 1 --->  120


def Fact(No):
    if(No<=0):
        return 1
    else:
        return(No*Fact(No-1))  

def main():
    x=int(input("Enter a number : "))
    Ret = Fact(x)    
    print("Factorial of a number is : ",Ret)    

        
if __name__=="__main__":
    main()

    