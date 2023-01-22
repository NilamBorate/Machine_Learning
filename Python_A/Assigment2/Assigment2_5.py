#Program to disply number is prime or not

def Num(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i ==0:
                print(n,"is not prime number")
                break
        else:
            print(n,"is prime number")        
    


def main():
    print("Enter a number: ")
    x=int(input())

    Num(x)


if __name__=="__main__":

    main()        
    