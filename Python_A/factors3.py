def main():
    print("Enter a number : ")
    No=int(input())
    
    i=1
    print("Factors are:")
    #for i in range(1,int(No/2)+1,1):
    
    while(i<=int(No/2)):
        if No % i == 0:
            print(i)
        i=i+1
   

if __name__=="__main__":
    main()    

#10%1==0
#10%2==0
#10%3==0
#10%4==0
#10%5==0    