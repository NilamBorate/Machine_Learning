

def Digit_Sum(n):
    if n<10:
        return n
    else: 
        return n%10 + Digit_Sum(int(n/10))    


def main():
    x=int(input("Enter a number : "))
    Ret=Digit_Sum(x)
    print("Sum of digit of a number is : ",Ret)


if __name__=="__main__":
    main()    