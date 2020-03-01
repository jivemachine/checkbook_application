print("~~~~~ Welcome to The Bacon Bank of credit card debt~~~~~~~~~~~~~~~~")

def welcome_message():
    print("What would you like to do today?")
    print("1.) View current balance")
    print("2.) Withdraw funds")
    print("3.) deposit funds")
    print("4.) View transaction history")
    print("5.) Exit application")
    print()
    user_choice = input("User input: ")
    while user_choice not in ["1", "2", "3", "4"]:
        print("Not a viable option. Please choose a given option")
    return user_choice



def one():
    with open('transactions.txt') as f:
        lines = f.read()
        clean_lines = lines.replace("$", "").replace(",","")
        current_balance = [ float(num) for num in clean_lines.split()]
        print(f"This is your current financial status ${sum(current_balance)}")
    print()
    print()

def two():
    print()
    print()
    (f"How much would you like to withdraw: {withdraw_amount}")
    withdraw_amount = input(f"How much would you like to withdraw: ")
    filename = "transactions.txt"
    with open(filename, "a") as f:
        f.write("-" + withdraw_amount + "\n")
    print()
    print()

def three():
    print()
    print()
    deposit_amount = input(f"How much would you like to deposit: ")
    filename = "transactions.txt"
    with open(filename, "a") as f:
        f.write(deposit_amount + "\n")
    print()
    print()

def four():
    print()
    print()
    with open('transactions.txt') as f:
        transaction_history = f.read()
        print(transaction_history)
        transaction_clear = input("Would you like to clear your cash history?" + "\n"
        + "if yes...input yes" + "\n"
        + "if not press enter: ")
        if transaction_clear in ["yes"]:
            transaction_clear.lower()
            double_check = input("Are you SURE?!?!? ")
            if double_check in ["yes", "enter"]:
                double_check.lower()
                file_contents = "0"
                with open('transactions.txt', "w") as f:
                    f.write(file_contents + "\n")
                    print(f"Here is your new history ${file_contents}") 
            print()
            print()
            print()   


def five():
    return exit()                                



while True:
    welcome_message()
    if user_choice = 1:
        one()
        welcome_message()
    elif user_choice = 2:
        two()
        welcome_message
    elif user_choice = 3:
        three()
        welcome_message()
    elif user_choice = 4:
        four()
        welcome_message()
    elif user_choice = 5:
        five()











