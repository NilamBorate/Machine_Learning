#Program to disply the sum of digit of a number

def Num(n):
    sum=0
    while(n>0):
        r=n%10
        sum=sum+r
        n=n//10
        
    print("Sum of digit of a number is ",sum)    
    
def main():
    print("Enter a number: ")
    x=int(input())
    Num(x)
    
    
if __name__=="__main__":
    main()