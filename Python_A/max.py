print("//////maximum between two numbers//////")

def main():
    x=int(input("Enter the first number : "))
    y=int(input("Enter the second number : "))

    if(x>y):
        print(x ,"is greater number.")
    elif(x==y):
        print("Both are equal numbers.")
    else:
        print(y ,"is greater number.")       

if __name__=="__main__":
    print("Inside a starter.")
    main()        