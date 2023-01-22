#with less number of iteration
#half number paryantach factors astat so No/2

def main():
    print("Enter a number : ")
    No=int(input())

    print("Factors are:")

    for i in range(1,int(No/2)+1,1):
        if ((No % i) == 0):
            print(i)
        

if __name__=="__main__":
    main()    

#10%1==0
#10%2==0
#10%3==0
#10%4==0
#10%5==0   