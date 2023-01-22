# program to disply pattern 
#   *  *  *  *  *
#   *  *  *  *  
#   *  *  *  
#   *  *
#   *

def pattern(n):
    i=n
    while(i>0):
        print(i*"  *  ")
        i=i-1

def main():
    print("Enter a number: ")
    x=int(input())

    print("The pattern is :")
    

    pattern(x)


if __name__=="__main__":
    main()        