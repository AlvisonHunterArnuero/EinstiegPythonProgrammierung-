def main_menu():
    balance = 3000
    msg = ""
    while True:
        print("-"*40)
        print("My Silly ATM Transactions Program")
        print("-"*40)
        print("1 - Deposit \n2 - Withdraw \n3 - Check Balance \n4 - Quit")
        sel_opt = int(input("Enter your selected transaction: "))

        if sel_opt < 4:
            if(sel_opt == 1):
                deposit_amnt = float(input("Enter Amount to deposit: "))
                balance += deposit_amnt
                msg = "Transaction completed."
            elif(sel_opt == 2):
                withdraw_amnt = float(input("Enter Amount to withdraw: "))
                balance -= withdraw_amnt
                msg = "Transaction completed."
            elif(sel_opt == 3):
                msg = f"Current Balance: {balance}"
            elif(sel_opt == 4):
                msg = "Successfully logged out"
                break
            print(msg)
        else:
            print("Invalid Option. Please try again.")


def login():
    logout = True
    if logout == True:
        pn = int(input("Please ENTER Pin Number: "))
        if pn != 4567:
            print("Invalid pin Number")
        else:
            logout = False
            main_menu()


# Call main function
login()
