import scripts.utils  as utils
from scripts.run_staff_actions import runStaffActions
import os

def staffSession():
    usernames = utils.getUsernames()
    username = utils.repeat("Input your username: ",
                            recorrect_message="Username not found, be sure to enter a correct username.\nTo exit, enter 'exit'.\nEnter username: ", options=usernames)

    if username == 'exit':
        print("Remember your username next time!")
        entryPoint()
    else:
        validpassword = utils.getPassword(username)
        utils.repeat("Input your password: ",
                                recorrect_message="Password incorrect. Input the right password: ", options=[validpassword])
        open("text_files/staff_session.txt", "w+")
        runStaffActions(entryPoint)


def entryPoint():
    print("\nWelcome to the SN Bank App")
    staffSessionOption = utils.repeat("\nInput your desired action as a digit\n1. staff login\n2. close app\nInput digit here: ",
                                      "Wrong input. Please, input one of these (1 or 2): ", ['1', '2'])

    if staffSessionOption == '2':
        print("Thank you for your time. Goodbye!")
        if os.path.exists('text_files/staff_session.txt'):
            os.remove('text_files/staff_session.txt')
    else:
        staffSession()


entryPoint()
