#Banking application
import os


accountNo=123
CusName=""
Mobile=0
balance=2000

class bank:
    print("Welcome to CodeBreakers Money App")

def create_bank_data_file():
    with open("Bank data.txt", "w") as file:
        file.write("2000")

def read_balance():
    if not os.path.isfile("Bank data.txt"):
        create_bank_data_file()

    with open("Bank data.txt", "r") as file:
        balance = float(file.readline())
    return balance

def write_balance(balance):
    with open("Bank data.txt", "w") as file:
        file.write(str(balance))

def log_transaction(transaction):
    with open("Transaction log.txt", "a") as file:
        file.write(transaction + "\n")

def make_deposit():
    amount = float(input("How much would you like to deposit?"))
    if amount <= 0:
        print("Invalid deposit amount.")
        return make_deposit()
    
    balance = read_balance()
    balance += amount
    log_transaction("Deposit: +{}".format(amount))
    print("Deposit successful.")
    print("Current balance:{}".format(balance))

def make_withdrawl():
    amount = float(input("How much would you like to withdraw?"))
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return make_withdrawl()
    
    balance = read_balance()
    if amount > balance:
        print("Insufficiant funds.")
        return make_withdrawl()
    
    balance = read_balance()
    balance -= amount
    write_balance(balance)
    log_transaction("Withdrawal: -{}".format(amount))
    print("Withdrawal successful.")
    print("Current balance: {}".format(balance))

def display_balance():
    balance = read_balance()
    print("Current balance: {}".format(balance))



def createAccounts ():
    global accountNo
    global CusName
    global Mobile
    global balance

    accountNo = int(input("enter account Number: "))
    CusName = input("enter Name: ")
    Mobile = int(input("enter Mobile Number: "))
    balance = float(input("enter current Balance: "))


def LogIn():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print("Total Balance: ",balance)


def showAccDetails():
    print("AccountNO:",accountNo)
    print("customerName:",CusName)
    print("mobile:",Mobile)


def checkbalance ():
    print("current Balance:",balance)

#_Main_account

print("\n1.Create account\n 2.LogIn")
choice = int(input("Select option"))
if(choice == 1):
    createAccounts()

elif(choice == 2):
    LogIn()

print("Would you like to make a transaction? \n 1.Yes \n 2.No")

choice = int(input("Select Option"))

if choice ==1:
    print("\n1.Withdraw \n 2.Deposit \n 3.Check balance")
    choice = int(input("Select Option"))

    if(choice == 1):
        make_withdrawl()
       
    if(choice == 2):
        make_deposit()
        
    elif(choice == 3):
        checkbalance()

elif choice == 2:
    print("thank you have a nice day!")
    













