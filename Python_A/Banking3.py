#Instance variable :Name,Amount,Address,AccountNo
#Instance Method :CreateAccount(),DisplyAccountInfo()
#Class Variables : Bank_Name,ROI_ON_FD
#class method : DisplyBankInformation

class Bank_Account:

    Bank_Name="HDFC bank PVT LTD"
    ROI_ON_FD=6.7

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
        print("Name of account Holder : ",self.Name)
        print("Account number : ",self.AccountNo)
        print("Address of account Holder : ",self.Address)
        print("Current amount in account : ",self.Amount)

    @classmethod
    def DisplyBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposite is : ",cls.ROI_ON_FD)

    

def main():
    print("Name of Bank: ",Bank_Account.Bank_Name)
    print("Rate odf Interest on fixed deposite : ",Bank_Account.ROI_ON_FD)

    Bank_Account.DisplyBankInformation()

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