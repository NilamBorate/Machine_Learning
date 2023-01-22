#Program which accepts N numbers from user and store it into the list and return mimimum number from list


def Min(a):
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
    
  
    Ans=Min(y)
    print("Manimum number from the list is : ",Ans[0])
    
if __name__=="__main__":
    main()