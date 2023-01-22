print("Application to demonstrate Industrial programming !!")

def Addition(value1,value2):
    Ans=value1+value2  
    return Ans

def main():
    print("Enter the first number: ")
    no1=int(input())
    print("Enter second number: ")
    no2=int(input())

    sum=Addition(no1,no2)
    print("Addition is : ",sum)


if __name__ == "__main__":
    main() 
    