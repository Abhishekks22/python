class Bank:
    def __init__(self,name,acct_no):
        self.name=name
        self.acct_no=acct_no
        self.balance=0
    def display(self):
        print("ACCOUNT DETAILS")
        print("---------------")
        print("Account Holdeer",self.name)
        print("ACCOUNT DETAILS",self.acct_no)
        print()
    def deposit(self,deposit):
        self.dp=deposit
        self.balance=self.balance+self.dp
        print("Deposition successfully")
        print()
    def withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("Amount withdrawed")
        else:
            print("not enough balance")
    def balance


