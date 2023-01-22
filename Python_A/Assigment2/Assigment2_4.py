#Program to disply addition of a factors of a number

def factor(n):
    sum=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            print(i)
            sum=sum+i
    print("The sum of factors is : ",sum)

def main():
    print("Enter a number: ")
    x=int(input())

    print("The factors are : ")

    factor(x)



if __name__=="__main__":
    main()        