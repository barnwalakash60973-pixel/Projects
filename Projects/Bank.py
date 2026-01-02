#accont
class Account:
    def __init__(self,accNum,balance):
        accNum=accNum
        self.balance=balance
        print("The balance in your account is",self.balance)

    
    #fxn for withdraw money in account
    def debit(self,ammount):
        self.ammount=ammount
        if 0<ammount<=self.balance:
            self.balance-=ammount
            print("The remaining ammount is",self.balance)
        else:
            print("Insufficient balance in your account.")

    
    #fxn for deposite money in account
    def credit(self,ammount):
        self.ammount=ammount
        if ammount>0:
            self.balance+=ammount
            print("Now,Currenty balance in your account is: ",self.ammount)
        else:
            print("Invalid daposited ammount.")
    def get_balance(self):
        return self.balance

open_acc=float(input("Enter the account number: "))
balance=float(input("Enter the account balance: "))
A1=Account(open_acc,balance)


while True:
    print("\n____________Menu___________")
    print("For withdraw money:Press '1' ")
    print("For deposited money:Press '2' ")
    print("For check the ammount balance:Press '3' ")
    print("For exitence the account:Press '4' ")
    choice=int(input("Enter your choice(1-4): "))
    
    if choice==1:
        amm=float(input("Enter the ammount: "))
        A1.debit(amm)
        
    elif choice==2:
        amm=float(input("Enter the ammount: "))
        A1.credit(amm)
        
    elif choice==3:
        print("your account balance is: ",A1.get_balance)
        break

    
    elif choice==4:
        print("Exist the account.")
        break
    else:
        print("Please enter the valid number.!")


print("_____________Thanks for comming_____________________")

