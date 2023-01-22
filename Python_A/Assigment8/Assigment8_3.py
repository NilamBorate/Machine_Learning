# 5 4 3 2 1 

def Disply(No):
    if(No>0):
        print(No,end=" ")
        No=No-1
        Disply(No)    

def main():
    x=int(input("Enter a number : "))
    Disply(x)
    
if __name__=="__main__":  
    main()