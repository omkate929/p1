def register():

    username = input("Create username: ")
    password = input("Create password: ")

    file = open("users.txt", "a")
    file.write(f"{username}:{password}\n")
    file.close()

    print("User registered successfully ")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("users.txt", "r")
    data = file.readlines()
    file.close()

    for i in data:

        user,passw = i.strip().split(":")

        if username == user and password == passw:
            print("Login success")
            return True
            print("Wrong credentials ")
            return False

while True:

    print("\n===== LOGIN MENU =====")
    print("1 Register")
    print("2 Login")
    print("3 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register()

    elif choice == 2:
        result = login()
        if result:
            break

    elif choice == 3:
        print("thank you")
        exit()
    else:
        print("Invalid choice")

class Wallet():

    def __init__(self, balance):
        self.balance = balance
        self.total_spent = 0

    def add_money(self, amount):
        self.balance += amount
        print("Amount added:", amount)

    def spend_money(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.total_spent += amount
            print("Money spent:", amount)
        print("total balance:", self.balance)

    def check(self):
        print("Current balance:", self.balance)

    def analysis(self):
        print("Total spent this month:", self.total_spent)
        print("Current balance:", self.balance)

    def monthly_target(self):
                money=[]
                set_money=input("set amount:")
                money.append(set_money)
                print(money)

    def suggestion(self):
        if self.balance == 500:
            print("low balance")
        elif self.total_spent > 5000:
            print(" high payment spend")
        elif self.balance > -15000:
            print(" Good savings")
        else:
            print(" Spending is control")

detail = Wallet(0)

while True:
    print("________meanu________")
    print("1:-Add Money")
    print("2:-Spend Money")
    print("3:-Monthly terget")
    print("4:-Check Expense History")
    print("5:-Check Balance")
    print("6:-Analysis")
    print("7:-suggection")
    print("8:-Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Enter number only")
        continue

    if choice == 1:
        amount = int(input("Enter amount: "))
        detail.add_money(amount)

    elif choice == 2:
        category = input("Enter category: ")
        amount = int(input("Enter spend amount: "))

        file = open("expense.txt", "a")
        file.write(f"{category}:{amount}\n")
        file.close()
        detail.spend_money(amount)

    elif choice ==3:
        detail.monthly_target()
     
    elif choice == 4:
        file = open("expense.txt", "r")
        print("\nExpense History:")
        print(file.read())
        file.close()

    elif choice == 5:
        detail.check()

    elif choice == 6:
        detail.analysis()

    elif choice==7:
        detail.suggestion()

    elif choice == 8:
        print("Thank you for using our service ")
        break
    else:
        print("Invalid input")