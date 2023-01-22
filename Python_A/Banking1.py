#Instance variable :Name,Amount,Address,AccountNo
#Instance Method :CreateAccount(),DisplyAccountInfo()

class Bank_Account:

    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=0

    def CreateAccount(self):
        print("Enter your name: ")
        self.Name = input() 

        print("Enter your initial Amount : ")
        self.Amount = int(input()) 

        print("Enter your Adress : ")
        self.Address = input() 

        print("Enter your Account Number: ")
        self.AccountNo = int(input())  


    def DisplyAccountInfo(self):
        print("------------Your Account Information is as below ----------")    
        print("Name of accouCurrentnt Holder : ",self.Name)
        print("Account number : ",self.AccountNo)
        print("Address of account Holder : ",self.Address)
        print(" amount in account : ",self.Amount)


def main():

    User1=Bank_Account()
    User2=Bank_Account()

    print("Creating the first account ")
    User1.CreateAccount()
    print("Creating the Second account ")
    User2.CreateAccount()

    User1.DisplyAccountInfo()
    User2.DisplyAccountInfo()

if __name__=="__main__":
    main()    