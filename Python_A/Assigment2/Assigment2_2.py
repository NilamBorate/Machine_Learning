#Program to disply pattern as 
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *

def pattern(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            print(int(i/i)*"*",end="  ")
        print()   


def main():
    print("Enter a number :")
    x=int(input())

    print("The pattern is :")
    
    pattern(x)


if __name__=="__main__":
    main()        

