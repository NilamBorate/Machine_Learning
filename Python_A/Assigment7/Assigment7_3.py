import threading

def evenlist(lst):
    s=0
    for i in lst:
        if(i%2==0):
            s=s+i
    print(s)
 
def oddlist(lst):
    s=0
    for i in lst:
        if(i%2!=0):
            s=s+i
    print(s)
 

def main():
    value=[]
    No=int(input("Enter how many elements you want to store in list : "))
    for i in range(1,No+1):
        na=int(input())
        value.append(na)
    print(value)
    
    
    t1=threading.Thread(target=evenlist,args=(value,))
    t2=threading.Thread(target=oddlist,args=(value,))
    
    print("Addition of all even numbers from the list is: ")
    t1.start()
    t1.join()
    
    print("Addition of all odd numbers from the list is: ")
    t2.start()
    t2.join()
    
if __name__=="__main__":
    main()