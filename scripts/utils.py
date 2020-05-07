import os

def repeat(initial_message, recorrect_message="", options=[]):
    mode = input(initial_message)
    if len(options) > 0:
        while mode not in options:
            mode = input(recorrect_message)
            if mode == 'exit':
                print("Alright, since you want to exit. Bye!")
                break
    return mode


def getUsernames():
    with open('text_files/staff.txt') as staffFile:
        rawUsernames = [
            line for line in staffFile if line.startswith('Username')]
        usernames = list(map(lambda x: x[11:][:-1], rawUsernames))
    return usernames


def getPassword(username):
    usernames = getUsernames()
    index = usernames.index(username)
    with open('text_files/staff.txt') as staffFile:
        rawPasswords = [
            line for line in staffFile if line.startswith('Password')]
        passwords = list(map(lambda x: x[11:][:-1], rawPasswords))
    return passwords[index]


def isEmpty(path):
    return os.stat(path).st_size==0


def getAccountNumbers():
    with open('text_files/customer.txt') as customerFile:
        rawAcctNums = [
            line for line in customerFile if line.startswith("'account number'")]
        acctNums = list(map(lambda x: x[19:29], rawAcctNums))
    return acctNums

def getAccountDetails(account_number):
    account_nums = getAccountNumbers()
    index = account_nums.index(account_number)
    rawData = ""

    with open('text_files/customer.txt', 'r') as customerFile:
        for line in customerFile:
            rawData += line
        data = rawData.split('\n\n')[index].join('\n\n')
 
    return data
