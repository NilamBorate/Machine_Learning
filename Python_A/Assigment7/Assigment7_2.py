import threading

def evenFactor(No):
    s=0
    for i in range(1,int(No/2)+1):
        if(No%i==0):
            if(i%2==0):
                s=s+i
    print(s) 
 
    
def oddFactor(No):
    s=0
    for i in range(1,int(No/2)+1):
        if(No%i==0):
            if(i%2!=0):
                s=s+i
    print(s) 


def main():
    No=int(input("Enter a number : "))
    
    p1=threading.Thread(target=evenFactor,args=(No,))
    p2=threading.Thread(target=oddFactor,args=(No,))

    print("Addition of even Factors: ")
    p1.start()
    p1.join()

    print("Addition of odd Factors:  ")
    p2.start()
    p2.join()
    
    print("exit from main")
       
if __name__=="__main__":
    main()
        