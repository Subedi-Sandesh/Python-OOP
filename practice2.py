class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    #Debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Your {self.acc_no} has been Debited by NPR{amount}\nYour new balance is {self.balance}")
        
    #Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Your {self.acc_no} has been Credited by NPR{amount}\nYour new balance is {self.balance}")
  
acc1 = Account(10000, 12345)

acc1.debit(1000)
acc1.credit(12000)


        