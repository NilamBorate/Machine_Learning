#program to disply number of a digit in a number

def Num(n):
    count=0
    while(n>0):
        n=n//10
        count=count+1
    print("Total number of digits :",count)    
    
def main():
    print("Enter a number: ")
    x=int(input())
    Num(x)
    
    
if __name__=="__main__":
    main()