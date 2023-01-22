#Program to disply "*" on screen

def Num(A):
    for i in range(1,A+1):
        print(int(i/i)*"*",end=" ")


def main():
    print("Enter the number:")
    x=int(input())

    Num(x)


if __name__=="__main__":
    main()    
