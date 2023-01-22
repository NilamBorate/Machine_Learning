class Numbers:
    def __init__(self):
        self.Size=0
        self.Arr=list()

    def Accept(self):
        print("Enter how many elements you want : ")
        self.Size=int(input())

        print("Please enter the elements: ")
        Value=0
        for i in range(0,self.Size):
            Value=int(input())
            self.Arr.append(Value)

    def Disply(self):
        print("Elements from list are : ")
        for i in range(0,self.Size):
            print(self.Arr[i])
   
    def Addition(self):
        sum=0
        for i in range(0,self.Size):
            sum=sum+self.Arr[i]
        return sum

    def Average(self):
        sum=0
        for i in range(0,self.Size):
            sum=sum+self.Arr[i]
        return (sum/self.Size)    

def main():

    obj=Numbers()
    obj.Accept()
    obj.Disply()
    Add=obj.Addition()
    print("Addition of all elements in a list is : ",Add)

    Avg=obj.Average()
    print("Average of all elements in a list is : ",Avg)

    

if __name__=="__main__":
    main()    