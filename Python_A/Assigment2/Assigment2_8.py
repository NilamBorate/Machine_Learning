#Program to disply the pattern as 
#  1
#  1  2
#  1  2   3
#  1  2   3   4
#  1  2   3   4   5

def pattern(n):
    for j in range(1,n+1):
        for i in range(1,(j-1)+1):
            print(i,end=" ")
        print(j)    



def main():
    print("Enter a number: ")
    x=int(input())

    print("The pattern is :")


    pattern(x)


if __name__=="__main__":
    main()        