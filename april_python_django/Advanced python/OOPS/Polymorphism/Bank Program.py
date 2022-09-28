#Bank
#print balance after withdraw
#print balance after deposit

class Bank:
    bname="Standard Chartered Bank"

    def account_creationset(self,name,acno):
        self.name=name
        self.acno=acno
        self.minbal=1000
        self.bal=self.minbal

    def account_creationprint(self):
        print("From ", Bank.bname)
        print("Hello ",self.name,"Welcome to ",Bank.bname)
        print("Congratulation! Your account number is ",self.acno)
        print("Minimum balance for your account is ",self.minbal,"INR","and current balance is: ",self.bal,"INR")

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.bal:
            print("From ", Bank.bname)
            print("Insufficient Balance")
        else:
            self.bal=self.bal-self.amount
            print("From ",Bank.bname)
            print("You have withdrawn:",self.amount,"INR","Your account balance is ",self.bal,"INR")
    def deposit(self,damount):
        self.damount=damount
        self.bal=self.bal+self.damount
        print("From ",Bank.bname)
        print("You have deposited: ",self.damount," Your account balance is: ",self.bal,"INR")
ob=Bank()
ob.account_creationset("Vishnu",101)
ob.withdraw(1001)
ob.deposit(5000)
