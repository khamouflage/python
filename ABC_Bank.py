"""
A simple banking program to onboard cutomers to a bank. 
The customer can carry out basic banking operations like, deposit, withdrawal, transfer and request for account statement.
"""
import random
import time
from datetime import datetime

#data = {} #empty dictionary

with open("database.txt") as file:
    data = eval(file.read) #Open a database file and read the dictionary using eval function

####################### Functions ##################
def signup(database):
    name = input("Enter your name:")
    time.sleep(1)
    address = input("Enter your Address:")
    time.sleep(1)
    phone = input("Enter your Phone number:")
    time.sleep(1)
    pin = input("Enter your six(6) digit PIN:")
    time.sleep(1)

    print("Processing Account....")
    time.sleep(3)

    
   # account_number ="0"+ "".join([str(random.choice(range(10))) for i in range(9)])
    account_number ="0"+ str(random.randrange(100000000, 999999999))

    database[account_number] = {
        "name": name,
        "address": address,
        "phone":phone,
        "pin":pin,
        "balance": 50,
        "transactions": [],
    }

    first_name = name.split(" ")[0]
    
    print(f"Dear {first_name}\n Congratulations, your account has been successfully created. \n Your account number is {account_number} use it for login.\n Do not share your PIN with anyone.")

    return database
   








################### Codes ##########################


print("Welcome to the ABC Bank of Africa")
on = True


while on:
    print("Select 'l' to login or 's' to signup for an account\n Press any other key to quit.")
    selection = input(":> ").lower()

    if selection == "l":
        account_number = input("Enter account number:\n>")
        pin = input("Enter account six digit PIN:\n>")

        user_detail = data.get(account_number)

        if user_detail and user_detail['pin'] == pin:
            login = True
            while login:
                print(f"Welcome, {user_detail['name']}")
                print(f"Your current balance is {user_detail['balance']}")
                print(f"""Please choose an action below:
                1.Deposit
                2.Withdrawal
                3.Transfer
                4.Account Statement
                5.Logout""")
                
                action = input(":>")

                if action == "1": #Deposit
                    amount  = int(input("Deposit Amount\n>"))

                    user_detail["balance"] += amount

                    record = {
                        "amount":amount,
                        "type":"credit",
                        "action": "deposit",
                        "date": datetime.now().strftime('%d-%b-%Y, %H-%M-%S'),
                        }

                    user_detail["transactions"].append(record)

                    print("Deposit Successful\n")

                elif action == "2": #Withdrawal
                    amount = int(input("Withdrawal amount\n>"))

                    if amount <= user_detail['balance']:
                        user_detail['balance'] -= amount
                        
                        record = {
                        "amount":amount,
                        "type":"debit",
                        "action": "withdrawal",
                        "date": datetime.now().strftime('%d-%b-%Y, %H-%M-%S'),
                        }
                        
                        user_detail["transactions"].append(record)
                        
                        print("Withdrawal Successful")
                    else:
                        print("Insufficient Funds")
                        print(f"Your current balance is: {user_detail['balance']}")
                elif action == "3": #Transfer
                    beneficiary_account = input("Enter recipient account number:\n>")
                    amount = amount = int(input("Amount to Transfer\n>"))

                    beneficiary = data.get(beneficiary_account)

                    if beneficiary:
                        if amount >= user_detail['balance']:
                            print("Insufficient funds")

                        else:
                            print (f"Please confirm transfer of ${amount} to {beneficiary['name']}")
                            confirm = input("Yes/No:").lower()
                            
                            if confirm == 'yes':
                                user_detail["balance"]-= amount

                                record = {
                                    "amount":amount,
                                    "type":"debit",
                                    "action": f"transfer to {beneficiary['name']} ",
                                    "date": datetime.now().strftime('%d-%b-%Y, %H-%M-%S'),
                                    }
                                user_detail["transactions"].append(record)
                                
                                beneficiary["balance"]+= amount
                                record = {
                                    "amount" : amount,
                                    "type" : "credit",
                                    "action" : f"transfer from {user_detail['name']}",
                                    "date" : datetime.now().strftime('%d-%b-%Y, %H:%M:%S'),
                                }
                                
                                beneficiary['transactions'].append(record)
                                print("Transfer successful\n")

                            elif confirm == 'no':
                                print ("Transfer cancelled")


                    else:
                        print("Invalid recipient account number")

                elif action == "4": #Account Statement
                    records = user_detail['transactions']

                    if len(records) == 0:
                        print("No records found")
                    else:
                        print("========================================")
                        for record in records[-5:]:
                            print(f"Amount: ${record['amount']}")
                            print(f"Type: {record['type']}")
                            print(f"Action: {record['action']}")
                            print(f"Date: {record['date']}\n\n")
                        print("========================================")

                        print(f"Your balance as at {datetime.now().strftime('%d-%b-%Y, %H-%M-%S')} is {user_detail['balance']} ")

                elif action == "5":
                    login = False
                    print("Session Ended")

        else:
            print("Invalid authentication details")

    elif selection == "s":
        data = signup(data)
    else:
        print("Bye")
        on = False


with open("database.txt", "w") as file:
    file.write(str(data)) #Convert data dictionary to string and write it to file.