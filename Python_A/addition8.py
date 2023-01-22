print("Application to demonstrate Industrial programming !!")

import marvallousmodule

def main():
    print("value of __name__ from main is : ",__name__)
    print("Enter the first number: ")
    no1=int(input())
    print("Enter second number: ")
    no2=int(input())

    sum=marvallousmodule.Addition(no1,no2)
    print("Addition is : ",sum)

    sub=marvallousmodule.Substraction(no1,no2)
    print("Substraction is : ",sub)

if __name__ == "__main__":
    main() 
    