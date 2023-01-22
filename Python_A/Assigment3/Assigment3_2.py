#Program which accepts N numbers from user and store it into the list and return maximum number from list


def Max(a):
    a.sort()
    return a

def main():
    
    print("Enter how many elements you want?")
    x=int(input())
    y=list()
    print("Enter the elements:")
    
    for i in range(0,x):
        no=int(input())
        y.append(no)
    print(y)
    
  
    Ans=Max(y)
    print("Maximum number from the list is : ",Ans[-1])
    
if __name__=="__main__":
    main()