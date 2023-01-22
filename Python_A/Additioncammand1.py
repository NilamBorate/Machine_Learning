
from sys import *  #operating system specific file

def Addition(x,y):    
    Ans=0
    Ans=x+y
    return Ans
    

def main():
    print("Welcome to : ",argv[0])

    if(len(argv)==2):
        if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    ret=Addition(int(argv[1]),int(argv[2]))
   
    print("Addition is : ",ret)    
    
if __name__=="__main__":
    main()    

