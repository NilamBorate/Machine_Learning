#Program to disply Addition of two numbers

def Add(x,y):
    Addition=x+y
    return Addition

def main():
    print("Enter the first number")  
    A=int(input())

    print("Enter the Second number")  
    B=int(input())

    Ans=0
    Ans=Add(A,B)
    print("Addition of two numbers is ",Ans)

if __name__=="__main__":
    main()    

        