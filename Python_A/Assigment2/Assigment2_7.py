#Program to disply the pattern 
#    1   2   3   4   5
#    1   2   3   4   5
#    1   2   3   4   5
#    1   2   3   4   5
#    1   2   3   4   5

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=" ")
        print()    



def main():
    print("Enter a number: ")
    x=int(input())
    
    print("The pattern is :")
    

    pattern(x)


if __name__=="__main__":
    main()        