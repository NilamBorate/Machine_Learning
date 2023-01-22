from functools import reduce   

def filter(Helper_Function,Data):
    Result=[]
    for No in Data:
        if (Helper_Function(No)==True):
            Result.append(No)
    return Result

def map(Helper_Function,Data):
    Result=[]
    for No in Data:
          value=Helper_Function(No)
          Result.append(value) 
    return Result       

def reduce(Helper_Function,Data):
    Ans=1
    for no in Data:
        Ans=Helper_Function(Ans,no)
    return Ans     


def main():
    print("Enter number of elements you want to enter : ")
    iSize=int(input())

    Data_Input=[]
    print("Please enter the data")
    for iCnt in range (0,iSize,1):
        value=int(input())
        Data_Input.append(value)
    print("Data is : ",Data_Input)    

    Data_Filter = list(filter( lambda No:(70<= No <=90), Data_Input))
    print("Data after filter is :" , Data_Filter)

    Data_Map=list(map(lambda No:No+10,Data_Filter))
    print("Data after map is :",Data_Map)

    Output = reduce(lambda A,B: A*B,Data_Map)
    print("Result after reduce is : ",Output)

    
if __name__=="__main__":
    main()    