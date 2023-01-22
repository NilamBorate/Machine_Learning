import Arithmetic

def main():
    print("Enter the first number: ")
    no1=float(input())
    print("Enter second number: ")
    no2=float(input())

    sum=Arithmetic.Add(no1,no2)
    print("Addition is : ",sum)

    sub=Arithmetic.Sub(no1,no2)
    print("Substraction is : ",sub)

    Mult=Arithmetic.Mult(no1,no2)
    print("Multiplication is : ",Mult)

    Div=Arithmetic.Div(no1,no2)
    print("Division is : ",sub)


if __name__ == "__main__":
    main() 
    