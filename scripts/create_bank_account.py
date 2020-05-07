import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import scripts.utils as utils

def setOpeningBalance():
    not_proceed = True
    while not_proceed:
        try:
            opening_balance = int(
                input("Enter the opening balance: "))
            not_proceed = False
        except ValueError as val:
            print(
                f"Error! You entered {str(val).split(' ')[-1]} which is not a number")
            not_proceed = True
    return opening_balance


def generateAccountNumber():
    if utils.isEmpty('text_files/account_numbers.txt'):
        with open('text_files/account_numbers.txt', 'a') as acFile:
            acFile.write('4000000000')
        return 4000000000

    with open('text_files/account_numbers.txt') as acFile:
        for lastAcctNum in acFile:
            pass
    newAccountNumber = int(lastAcctNum) + 1
    with open('text_files/account_numbers.txt', 'a') as acFile:
        acFile.write(f'\n{newAccountNumber}')
    return newAccountNumber


def sendToCustomersFile(data):
    with open('text_files/customer.txt', 'w') as acFile:
        acFile.write(f'{data}')


def createBankAccount():
    account_name = utils.repeat("Enter an account name: ")
    opening_balance = setOpeningBalance()
    account_type = utils.repeat("Enter account type ('current' or 'savings'): ",
                          recorrect_message="Wrong input! Please, enter either 'current' or 'savings': ", options=["current", "savings"])
    account_email = utils.repeat("Enter account email: ")
    account_number = generateAccountNumber()

    account_details = f"""'account name' = {account_name}\n'opening balance' = {opening_balance}\n'account type' = {account_type}\n'account email' = {account_email}\n'account number' = {account_number}"""

    sendToCustomersFile(account_details)

    return f'\n\nAccount number = {account_number}'