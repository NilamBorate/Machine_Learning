

import MarvellousNum
def main():
    print("enter how many elements you want to store in the list")
    x=int(input())
    y=[]
    print("Enter the elements: ")
    for i in range(0,x):
        no=int(input())
        y.append(no)
    print(y)  
    

    print("Prime numbers in the list as : ")
    ListPrime=MarvellousNum.ChkPrime(y)
    
    
        
if __name__=="__main__":
    main()
    