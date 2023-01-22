# * * * * *

def Disply(No):
    if(No>0):
        print("*",end=" ")
        No=No-1
        Disply(No)    

def main():
    x=int(input("Enter a number : "))
    Disply(x)
    
if __name__=="__main__":  
    main()