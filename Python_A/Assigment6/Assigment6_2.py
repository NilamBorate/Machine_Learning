
class BankAccount:
    ROI=10.5

    def __init__(self):
        print("Enter your name: ")
        self.Name=input()
        print("Enter your  Amount: ")
        self.Amount=int(input())

    def Deposite(self,value):
        self.Amount=self.Amount+value  

    def Withdraw(self,value):
        self.Amount=self.Amount-value    
       
    def CalculateInterest(self):
        self.Amount=(self.Amount*self.ROI)/100

    def Disply(self):   
        print("Name of account Holder : ",self.Name)
        print("Remaining amount is  : ",self.Amount)
        


def main():

    User1=BankAccount()
    User2=BankAccount()

    value1=int(input("The amount of User1 will be deposited: "))
    value2=int(input("The amount of User2 will be deposited: "))
    User1.Deposite(value1)
    User2.Deposite(value2)
    print("Amount of {} after deposite is : {} ".format(User1.Name,User1.Amount))
    print("Amount of {} after deposite is : {} ".format(User2.Name,User2.Amount))


    value3=int(input("The amount withdraw by the User1 : "))
    value4=int(input("The amount withdraw by the User2 : "))
    User1.Withdraw(value3)
    User2.Withdraw(value4)
    print("Amount of {} after withdraw is :{}".format(User1.Name,User1.Amount))
    print("Amount of {} after withdraw is :{}".format(User2.Name,User2.Amount))

    User1.CalculateInterest()
    User2.CalculateInterest()
    print("Interest on amount is {} for {}".format(User1.Amount,User1.Name))
    print("Interest on amount is {} for {}".format(User2.Amount,User2.Name))

    User1.Disply()
    User2.Disply()

if __name__=="__main__":
    main()    