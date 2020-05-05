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


def sendToSession(data):
    with open('staff_session.txt', 'a') as acFile:
        acFile.write(f'{data}')


def createBankAccount():
    account_name = utils.repeat("Enter an account name: ")
    opening_balance = setOpeningBalance()
    account_type = utils.repeat("Enter account type ('current' or 'savings'): ",
                                recorrect_message="Wrong input! Please, enter either 'current' or 'savings': ", options=["current", "savings"])
    account_email = utils.repeat("Enter account email: ")
    account_number = generateAccountNumber()

    account_details = {
        "account name": account_name,
        "opening balance": opening_balance,
        "account type": account_type,
        "account email": account_email,
        "account number": account_number
    }
    sendToSession(account_details)
    return account_details


print(createBankAccount())
