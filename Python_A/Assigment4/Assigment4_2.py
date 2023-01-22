#Program to find product of two numbers using lambda function


def main():
    print("Enter first number : ")
    no1=int(input())
    
    print("Enter second number : ")
    no2=int(input())
    
    
    ProdFun = lambda x,y: x*y
    Ans=ProdFun(no1,no2)
    print("Product of a two numbers using lambda function is : ",Ans)
    
        
    
if __name__=="__main__":
    main()