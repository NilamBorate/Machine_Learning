import threading    

def Even(No):
    for i in range(1,No+1,1):
        if (i%2==0):
            print("Even number : ",i)

def Odd(No): 
    for i in range(1,No,1):
        if (i%2!=0):
            print("Odd number : ",i)
   
def main():

    print("Demonstration of parallel programming using multiple threads")
    Number=20

    p1=threading.Thread(target=Even,args=(Number,))
    p2=threading.Thread(target=Odd,args=(Number,))

    print("First ten even numbers: ")
    p1.start()
    p1.join()
    

    print("First ten odd numbers: ")
    p2.start()
    p2.join()

if __name__=="__main__":
    main() 
    