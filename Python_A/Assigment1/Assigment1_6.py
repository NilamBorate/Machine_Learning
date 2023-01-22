#Program to check number is positive negative or zero

def Num(A):
    if A<0:
        print("Negative Number")
    elif A==0:
        print("Zero")
    else:
        print("Positive Number")    


def main():
    print("Enter a number:") 
    X=int(input())
    
    Ans=Num(X)

if __name__=="__main__":
    main()             