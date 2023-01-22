#Program to disply 10to 1 on screen

def Num():
    x=int(input())
    print("The numbers are:")
    while(0<x):
        print(x)
        x=x-1

def main():
    print("Enter how many numbers you want?")
    Num()

if __name__=="__main__":
    main()

