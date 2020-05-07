import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts.create_bank_account import createBankAccount
from scripts.utils import repeat, isEmpty

def logout():
    print("Thank you for your time. Goodbye!")


def getAccountDetails():
    a = ""
    with open('text_files/customer.txt') as customerFile:
        for line in customerFile:
            a += line
    return a

def actions():
    staff_choice = repeat(
        "Enter your desired action. Just enter a digit.\n1. create bank account\n2. check account details\n3. logout\nEnter digit here: ", recorrect_message="You must enter a digit. (1, 2 or 3): ", options=['1', '2', '3'])
    return staff_choice

def runStaffActions(callback):
    staff_choice = actions()
    if staff_choice == '1':
        createBankAccount()
    if staff_choice == '2' and isEmpty('text_files/customer.txt'):
        print("You haven't created an account for a customer")
        createBankAccount()
    if staff_choice == '2' and not(isEmpty('text_files/customer.txt')):
        print(getAccountDetails())

    else:
        logout()
        callback(4)


runStaffActions(lambda z: z + 1)
