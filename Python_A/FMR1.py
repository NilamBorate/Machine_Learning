#Filter , Map , Reduced

def CheckEven(No):
    return (No%2==0)

def Increment(No):
    return No+2


def filterx(Arr,Function_Name):
    Result =[]
    for no in Arr:
        if (Function_Name(no)):
            Result.append(no)
    return Result        

def mapx(Arr,Function_Name):
    Result=[]
    for no in Arr:
        value=Function_Name(no)
        Result.append(value)
    return Result    

def reducex(Arr):
    sum=0
    for no in Arr:
        sum=sum+no
    return sum

def main():
    Data=[2,3,1,6,4,5,11,16,20]

    print("Original Data : ",Data)

    Data_filter=list(filterx(Data,CheckEven))

    print("Data after filter : ",Data_filter)

    Data_map=list(mapx(Data_filter,Increment))

    print("Data after map : ",Data_map)

    Ret = reducex(Data_map)
    print("Data after reduce : ",Ret)

if __name__=="__main__":
    main()    

