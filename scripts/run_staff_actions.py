import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import scripts.utils as utils
from scripts.create_bank_account import createBankAccount


def logout():
    print("Thank you for your time. Goodbye!")


def actions():
    staff_choice = utils.repeat(
        "\nEnter your desired action. Just enter a digit.\n1. create bank account\n2. check account details\n3. logout\nEnter digit here: ", recorrect_message="You must enter a digit. (1, 2 or 3): ", options=['1', '2', '3'])
    return staff_choice


def runStaffActions(callback):
    staff_choice = actions()
    breakLoop = False

    while not(breakLoop):
        if staff_choice == '1':
            createBankAccount()
            staff_choice = actions()
        if staff_choice == '2' and utils.isEmpty('text_files/customer.txt'):
            print("You haven't created an account for any customer")
            createBankAccount()
            staff_choice = actions()
        if staff_choice == '2' and not(utils.isEmpty('text_files/customer.txt')):
            account_number = utils.repeat("Enter the desired account number: ",
                                          recorrect_message="Account number not found. Please, ensure you enter an existing account number.\nIf you're tired and would like to exit, enter 'exit'.\nEnter exiting 10 digit account number: ", options=utils.getAccountNumbers())
            print(utils.getAccountDetails(account_number))
            staff_choice = actions()
        else:
            logout()
            breakLoop = True
            callback()
