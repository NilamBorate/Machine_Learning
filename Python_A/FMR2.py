
def main():
    print("Enter number of elements you want to enter : ")
    iSize=int(input())

    Data_Input=[]
    print("Please enter the data")
    for iCnt in range (0,iSize,1):
        value=int(input())
        Data_Input.append(value)

    print("Data is : ",Data_Input)    




if __name__=="__main__":
    main()    