# Program to disply factorial of a number

def Fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)


def main():
    print("Enter a number : ")
    x=int(input())

    print("The factorial of a number is :")
    Fact(x)
    

if __name__=="__main__":
    main()        