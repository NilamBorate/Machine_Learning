#Program to diply first 10 even number on screen


def Num(A):
    for i in range(1,A+1):
        if i % 2==0:
            print(i)


def main():
    print("Upto which number you want the even numbers?")
    x=int(input())

    print("First",int(x/2),"even numbers are:")
    Num(x)

if __name__=="__main__":
    main()    
