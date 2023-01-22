def main():
    print("Enter a number : ")
    No=int(input())

    print("Factors are:")

    for i in range(1,No,1):
        if No % i == 0:
            print(i)
        

if __name__=="__main__":
    main()    


#10%1==0
#10%2==0
#10%3==0
#10%4==0
#10%5==0