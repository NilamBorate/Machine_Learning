

def main():
    Arr= list()

    print("Enter how many elements you want to store?")
    size=int(input())

    print("Please enter the values")

    for i in range(0,size):
        no=int(input())
        Arr.append(no)  #Arr.insert(i,no)

    print(Arr)

    for i in Arr:
        if i%2==0:
            print("The number is even",i)    
        else:
            print("The number is odd",i)    


if __name__=="__main__":
    main()
    
