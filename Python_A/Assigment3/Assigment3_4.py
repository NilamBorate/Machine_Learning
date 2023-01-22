#Program which accepts N numbers from user and store it into the list and accept another number from user and return frequency of thet number from the list


def Cnt(a):
    print("Enter the element in the given list that you want to find its count :")
    z=int(input())
    w=a.count(z)
    return w
    
    
def main():
    
    print("Enter how many elements you want?")
    x=int(input())
    y=list()
    print("Enter the elements:")
    for i in range(0,x):
        no=int(input())
        y.append(no)
    print(y)
    
   
    Ans=Cnt(y)
    print("The given number repeated in ",Ans,"times")
  
    
    
if __name__=="__main__":
    main()