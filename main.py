import scripts.utils  as utils
import scripts.run_staff_actions as staffActions

def staffSession():
    usernames = utils.getUsernames()
    username = utils.repeat("Input your username: ",
                            recorrect_message="Username not found, be sure to enter a correct username. To exit, enter 'exit'. Enter username: ", options=usernames)

    if username == 'exit':
        print("Remember your username next time!")
        entryPoint()
    else:
        validpassword = utils.getPassword(username)
        password = utils.repeat("Input your password: ",
                                recorrect_message="Password incorrect. Input the right password: ", options=[validpassword])
        open("text_files/staff_session.txt", "w+")
        staffActions.runStaffActions(entryPoint)


def entryPoint():
    print("Welcome to the SN Bank App")
    staffSessionOption = utils.repeat("Input your desired action ('staff login' or 'close app'): ",
                                      "Wrong input. Please, input one of these ('staff login' or 'close app'): ", ["staff login", "close app"])

    if staffSessionOption == 'close app':
        print("Thanks for your time. Goodbye!")
    else:
        staffSession()


entryPoint()
