
print(" ~~~~~~~ Welcome to Your Cash Money ~~~~~~~~~~~~")
print()
print("What Would You Like to do?")
print("1.) View current balance")
print("2.) Record a debit")
print("3.) Record a credit")
print("4.) Exit")

user_choice = input("Enter destination: ")

def user_options(user_choice):
    while user_choice not in ["1","2","3","4"]:
        print(f"{user_choice} is not a valid destination. Please input a valid destination.")
        user_choice = input("Enter destination: ")


current_balance = float(0)
withdraw_value = float(0)
deposit_value = float(0)

if user_choice in ["4"]:
    print("Goodbye!")
    exit()

if user_choice in ["1"]:
    print()
    print()
    print(f"This is your current fincancial status: ${current_balance}")
    print()
    print()
    print("What would you like to do next?")
    print("1.) View current balance")
    print("2.) Record a debit")
    print("3.) Record a credit")
    print("4.) Exit")
    user_choice = input("Enter destination: ")
    
    

if user_choice in ["2"]:
    print()
    print()
    print(f"How much would you like to withdraw: {withdraw_value}")
    

user_options(user_choice)


