#Program to disply number is divisible by 5 or not

def Num(A):
    if A%5==0:
        print("True")
    else:
        print("False")    


def main():

    print("Enter a number :")
    x=int(input())

    Num(x)

if __name__=="__main__":
    main()


