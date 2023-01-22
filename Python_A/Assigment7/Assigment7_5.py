import threading    

def Thread1(No):
    i=1
    while(i<=No):
        print(i)
        i=i+1
        
def Thread2(No): 
    while(No>0):
        print(No)
        No=No-1
           
def main():

    print("Demonstration of parallel programming using multiple threads")
    print("Enter a number: ")
    Number=int(input())

    p1=threading.Thread(target=Thread1,args=(Number,))
    p2=threading.Thread(target=Thread2,args=(Number,))

    print("Thread1 Excecutes: ")
    p1.start()
    p1.join()

    print("Thread2 Executes: ")
    p2.start()
    p2.join()

if __name__=="__main__":
    main() 
    