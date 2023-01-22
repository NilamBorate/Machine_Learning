#Program to find square of a number using lambda function

def main():
    print("Enter a number : ")
    no=int(input())
    
    
    SquareFun = lambda x: x*x
    Ans=SquareFun(no)
    print("Square of a given number using lambda function  is : ",Ans)
    
        
if __name__=="__main__":
    main()