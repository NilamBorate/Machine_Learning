# 1 2 3 4 5  

def Disply(No):
    if No>0:
        Disply(No-1)
        print(No,end=" ") 
   
        
def main():
    x=int(input("Enter a number : "))
    Disply(x)
    
if __name__=="__main__":  
    main()