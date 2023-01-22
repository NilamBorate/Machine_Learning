#Program which accepts N numbers from user and store it into the list and return addition of all the elements in the list


def Add(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum   
    

def main():
    
    print("Enter how many elements you want?")
    x=int(input())
    y=list()
    print("Enter the elements:")
    for i in range(0,x):
        no=int(input())
        y.append(no)
    print(y)
    
    Ans=0
    Ans=Add(y)
    print("Addition of elements in the list is : ",Ans)
    
if __name__=="__main__":
    main()