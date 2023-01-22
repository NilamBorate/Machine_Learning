import threading

def small(a):
    l=[]
    for i in a:
        k=i.islower()
        if k==True:
         
            l.append(i)
    print(len(l))

        
def capital(a):
    u=[]
    for i in a:
        k=i.isupper()
        if k==True:
            u.append(i) 
    print(len(u))

def digit(a):
    u=[]
    for i in a:
        k=i.isnumeric()
        if k==True:
            u.append(i) 
    print(len(u))
    
    
def main():
    Name=input("Enter a string : ")
    
    p1=threading.Thread(target=small,args=(Name,))
    print("Number of small letter characters in the given string is : ")
    p1.start()
    print("Id of small thread is : ",id(small))
    print("Name of thread1 is small")
    print("\n")
    
    p2=threading.Thread(target=capital,args=(Name,))
    print("Number of capital letter characters in the given string is : ")
    p2.start()
    print("Id of capital thread is : ",id(capital))
    print("Name of thread2 is capital")
    print("\n")
    
    p3=threading.Thread(target=digit,args=(Name,))
    print("Number of digits in the given string is : ")
    p3.start()
    print("Id of digit thread is : ",id(digit))
    print("Name of thread3 is digit")
    print("\n")
      
if __name__=="__main__":
    main()