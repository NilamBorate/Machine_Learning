#Execution time of a process
import time

def DisplyEven(No):
    for i in range(1,No,1):
        if (i%2==0):
            print("Even number : ",i)

def DisplyOdd(No): 
    for i in range(1,No,1):
        if (i%2!=0):
            print("Odd number : ",i)
   
def main():

    print("Demonstrtion of serial programming")
    DisplyEven(2000)
    DisplyOdd(2000)


if __name__=="__main__":
    start_time=time.process_time()
    main() 
    end_time=time.process_time() 
    print("Execution time is : ",end_time-start_time)  