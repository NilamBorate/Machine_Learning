#Program for print 5 times Mravellous on screen

def Marvellous():
    x=int(input())
    for i in range(1,x+1):
        print("Marvellous")

def main():
    print("Enter how many times you want to print the string on screen?")
    
    Marvellous()

if __name__=="__main__":
    main()    
