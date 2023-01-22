

prime=[]
def ChkPrime(Data_Input):
    for i in Data_Input:
        c=0
        for j in range(1,i):
            if i%j==0:
                c=c+1
        if c==1:
            prime.append(i)
    return prime       

Multi=[]
def Mult(Data_Filter):
    for i in Data_Filter:
        i=i*2
        Multi.append(i)
    return Multi 


def Maxi(Data_Map):
    for i in Data_Map:
        Data_Map.sort()
    return i
    
    
def main():
    
    
    print("Enter number of elements you want to enter : ")
    iSize=int(input())

    Data_Input=[]
    print("Please enter the data")
    for iCnt in range (0,iSize,1):
        value=int(input())
        Data_Input.append(value)
    print("Data is : ",Data_Input)    

    Data_Filter =ChkPrime(Data_Input)
    print("Data after filter is :" , Data_Filter)
    
    Data_Map=Mult(Data_Filter)
    print("Data after map is :",Data_Map)

    Output = Maxi(Data_Map)
    print("Result after reduce is : ",Output)   
    
if __name__=="__main__":
    main()    
    