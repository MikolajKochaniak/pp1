class bank_account():
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0
    def deposit(self,add):
        self.balance += add
        self.add =0
    def withdraw(self,remove):
        if self.balance < remove:
            print("Insufficient funds on the account")
            return None
        else:
            self.balance -= remove
    def status(self):
        print(self.balance)

account = bank_account(account_no="11 1111 1111 1111 1111 1111 1111")
account.status()
account.deposit(25.30)
account.status()
account.withdraw(31.70)
account.status()
account.withdraw(14)
account.status()

