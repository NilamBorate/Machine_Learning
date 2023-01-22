def DisplyFactors(No):
    i=1
    print("Factors are:")
    while(i<=int(No/2)):
        if No % i == 0:
            print(i)
        i=i+1
   
def main():
    print("Enter a number : ")
    No=int(input())

    DisplyFactors(No) 
   

if __name__=="__main__":
    main()    