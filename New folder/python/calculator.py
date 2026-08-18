class bank():
    def __init__(self,balance):
        self.balance=balance

    def creadit(self,amount):

        self.balance+=amount
        print("Your balance is:",amount)

    def withdraw(self,amount):
        self.balance-=amount
        print("your balance is:",self.balance)
    
    def check(self):
        print("Your balance is:",self.balance)

detail=bank(20000)

while True:

    print("1.creadit")
    print("2.withdraw")
    print("3.check")
    print("4.exit")



    choice=int(input("enter your choice:"))
    tax=18

    if choice==1:
        amount=int(input("enter your amount:"))
        detail.creadit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))

        tax_amount = amount * tax / 100
        final_amount = amount + tax_amount

        print("Original amount:", amount)
        print("Tax (18%):", tax_amount)
        print("Final amount:", final_amount)

    elif choice==3:
        tax=balance-300
        print("tax cut:",tax)

    elif choice==4:
        amount=int(input("enter creadit amount:"))
        detail.withdraw(amount)
    elif choice==3:
        detail.check()

    elif choice==4:
        print("thank you 🥰")
    else:
        print("inficient input")