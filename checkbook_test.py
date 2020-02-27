import locale
locale.setlocale(locale.LC_ALL, '')


print(" ~~~~~~~ Welcome to Your Cash Money ~~~~~~~~~~~~")   # Epic introduction 
print()




app_running = True




while app_running == True:
    print("What Would You Like to do?")
    print("1.) View current balance")
    print("2.) Record a debit")
    print("3.) Record a credit")
    print("4.) Show me the cash money")
    print("5.) Exit")
    user_choice = input("Enter destination: ")
    
    if user_choice == "1":
        print()
        print()
        with open('transactions.txt') as f:
            lines = f.read()
            clean_lines = lines.replace("$","").replace(",","")
            current_balance = [ float(num) for num in clean_lines.split()]
            print(f"This is your current financial status ${sum(current_balance)}")
        print()
        print()

    elif user_choice == "2":
        print()
        print()
        while True:
            withdraw_amount = input(f"How much would you like to withdraw: ")
            try:
                val = float(withdraw_amount)
                break
            except ValueError:
                print("Not a number. Please input a number.")
        filename = "transactions.txt"
        with open(filename, "a") as f:
            f.write("-" + withdraw_amount + "\n")
        print()
        print()

    elif user_choice == "3":
        print()
        print()
        while True:
            deposit_amount = input(f"How much would you like to deposit: ")
            try:
                val = float(deposit_amount)
                break
            except ValueError:
                print("Not a number...please input a number")
        filename = "transactions.txt"
        with open(filename, "a") as f:
            f.write(deposit_amount + "\n")
        print()
        print()
    elif user_choice == "4":
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
    elif user_choice == "5":
        print("Goodbye!")
        exit()  
    else:
        print(f"{user_choice} is not a valid destination. Please input a valid destination.")
        user_choice = input("Enter new destination: ")

    
