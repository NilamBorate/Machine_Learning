import time
import multiprocessing


def DisplyEven(No):
    for i in range(1,No,1):
        if (i%2==0):
            print("Even number : ",i)

def DisplyOdd(No): 
    for i in range(1,No,1):
        if (i%2!=0):
            print("Odd number : ",i)
   
def main():

    print("Demonstrtion of parallel programming using multiple processes")
    Number=2000

    p1=multiprocessing.Process(target=DisplyEven,args=(Number,))
    p2=multiprocessing.Process(target=DisplyOdd,args=(Number,))

    p1.start()
    p2.start()

    print("End of main")

if __name__=="__main__":
    start_time=time.process_time()
    main() 
    end_time=time.process_time() 
    print("Execution time is : ",end_time-start_time)  