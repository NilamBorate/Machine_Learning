#Program to check even odd numbers

def ChkNum(A):
    if A%2==0:
        print("The number is even",A)
    else:
        print("The number is odd",A)  


def main():
    print("Enter a number:")
    x=int(input())

    Ans=ChkNum(x)


if __name__=="__main__":
    main()              