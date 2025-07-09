import pydb;

def validateAccount(account_id):
    if not account_id.isnumeric():
        print(pydb.Color.RED + "Incorrect entry - account id must be a numeric value!!! \n" + pydb.Color.END)
        return 0

    if not pydb.accountExists(account_id):
        print(pydb.Color.RED + "The account id does not exist in system!!!" + pydb.Color.END)
        return 0
    return 1

def validateAdmin(account_id) :
    if not pydb.isUserAdmin(account_id):
        print(pydb.Color.RED + "You are not in Admin role!!!" + pydb.Color.END)
        return 0
    return 1

def validatePassword(account_id, password) :
    userAccount = pydb.validatePassword(account_id, password)

    if userAccount is None:
        print(pydb.Color.RED + "The password you entered is incorrect!!!" + pydb.Color.END)
        return None
    return userAccount

def validateUser(user_id) :
    if (pydb.userIdExists(user_id)):
        print(pydb.Color.RED + "The user id with the same name already exist in system!!!" + pydb.Color.END)
        return 0
    return 1

def add_user(userAccount):
    return pydb.addAccount(userAccount)

def printAccount(account) :
    print("ACCOUNT_ID = ", account.account_id)
    print("USER_ID = ", account.user_id)
    print("PASSWORD = ", account.password)
    print("AMOUNT = ", account.amount, "\n")

def greetUser():
    print(pydb.Color.BOLD + pydb.Color.BLUE + "DAILY BANK MONEY TRACKER\n" + pydb.Color.END)
    print(pydb.Color.BOLD + pydb.Color.BLUE + "A penny saved is a penny earned!!!" + pydb.Color.END)
    print(
        pydb.Color.BLUE + "This is your personalised money tracker to check on your daily expenditure, and manage and analyse your spending.\n" + pydb.Color.END)

def userChoice (choice, account) :
    print("----------")
    if int(choice) == 1:
        withdrawal = input(pydb.Color.BOLD + "Kindly enter the net amount of money that you wan to withdraw from your account: " + pydb.Color.END)

        if isChoiceEmpty(withdrawal):
            return 0

        if not withdrawal.isnumeric():
            print(pydb.Color.RED + "Incorrect entry - enter a numeric value!!! \n" + pydb.Color.END)
            return 0

        if(float(withdrawal) > float(account.amount)):
            print(pydb.Color.RED + "You cannot withdraw more than " + str(account.amount) + "\n"+ pydb.Color.END)
            return 0

        balance = int(account.amount) - int(withdrawal)
        print(pydb.Color.PURPLE + "Your final balance is :", str(balance) + pydb.Color.END)

        if account.amount > 0 :
            perc = (balance / int(account.amount)) * 100
            print(pydb.Color.PURPLE +  "This is ", str(perc), "% of your initial amount." + pydb.Color.END)

            if perc < 60:
                print(pydb.Color.PURPLE + "TIP: Spend your money more carefully as your balance is just ", perc, "% of how much you had before." + pydb.Color.END)
                # break
            if perc > 90:
                print(pydb.Color.PURPLE + "Bravo! You spend your money very carefully" + pydb.Color.END)
                # break

        account.amount = balance
        pydb.updateAccount(account)

    if int(choice) == 2:
        deposit = input(pydb.Color.BOLD + "Kindly enter the net amount of money that you want to deposit to your account: " + pydb.Color.END)
        if isChoiceEmpty(deposit):
            return 0

        balance= int(account.amount) + int(deposit)
        print(pydb.Color.PURPLE + "Your final balance is :", str(balance) + pydb.Color.END)

        if account.amount > 0 :
            perc = (balance / int(account.amount)) * 100
            print(pydb.Color.PURPLE + "This is ", str(perc), "% of your initial amount." + pydb.Color.END)

            if perc > 150:
                print(pydb.Color.PURPLE + "WOW! Today you have deposited a lot of money" + pydb.Color.END)
                # break

        account.amount = balance
        pydb.updateAccount(account)

    if int(choice) == 3:
        print(pydb.Color.PURPLE +  "Your user id is: ", account.user_id + pydb.Color.END)
        print(pydb.Color.PURPLE +  "Your account id is: ", str(account.account_id) + pydb.Color.END)
        print(pydb.Color.PURPLE +  "Your password  is: ", str(account.password) + pydb.Color.END)
        print(pydb.Color.PURPLE +  "Your role  is: ", str(account.admin) + pydb.Color.END)
        print(pydb.Color.PURPLE +  "The current amount in your account is: ", str(account.amount) + pydb.Color.END)
        check = input(pydb.Color.BOLD + "Do you want to change your password (Enter 'Y' for Yes and 'N' for No): "+ pydb.Color.END)
        if isChoiceEmpty(check):
            return 0

        if str(check).lower() == 'y':
            newPassword = input(
                pydb.Color.BOLD + "Enter new password: " + pydb.Color.END)
            if isChoiceEmpty(newPassword):
                return 0
            account.password = newPassword;
            pydb.updatePassword(account)
            print(pydb.Color.PURPLE +  "Your password is changed to: ", account.password + pydb.Color.END)
        else:
            print(pydb.Color.PURPLE + "Thanks for using money management tool!!! \n" + pydb.Color.END)
            return 0
    if int(choice) == 4:
        print(pydb.Color.PURPLE + "Thanks for using money management tool!!! \n" + pydb.Color.END)
        return 0

    if int(choice) == 5:
        pydb.printAllUsers(0)
        return 0

    if int(choice) == 6:
        account_id = input(pydb.Color.BOLD + "Enter the Account id of user to delete: "+ pydb.Color.END)
        if isChoiceEmpty(account_id):
            return 0

        if not account_id.isnumeric():
            print(pydb.Color.RED + "Incorrect entry - account id is a numeric value!!! \n" + pydb.Color.END)
            return 0
        pydb.deleteAccount(account_id)
        return 0
    print("----------\n")
    print(pydb.Color.PURPLE + "Thanks for using Personal Bank Money Management tool!!! \n"+ pydb.Color.END)

greetUser()

pydb.setDatabase()

def isChoiceEmpty(choice):
    if len(str(choice).strip()) == 0 :
        print(pydb.Color.RED + "Invalid Input!!!" + "\n" + pydb.Color.END)
        return 1
    return 0

while True:
    print('\n')
    ans = input(
        pydb.Color.BOLD + "Are you an Admin or an User (Enter 'A' for Admin and 'U' for new or existing User; Enter 'EXIT' to exit): " + pydb.Color.END)

    if isChoiceEmpty(ans) :
        continue

    if str(ans).lower() == 'a':

        account_id = input(pydb.Color.GREEN + "Kindly enter your account id: " + pydb.Color.END)

        if isChoiceEmpty(account_id):
            continue

        if not validateAccount(account_id):
            continue

        if not validateAdmin(account_id):
            continue

        password = input(pydb.Color.GREEN + "Kindly enter your password: " + pydb.Color.END)
        if isChoiceEmpty(password):
            continue

        userAccount = validatePassword(account_id, password)
        if userAccount is None:
            continue

        choice = input(
            pydb.Color.BOLD + "Kindly enter your choice: \n 5--- View all users \n 6 --- Delete user \n" + pydb.Color.END)

        if isChoiceEmpty(choice):
            continue

        if int(choice) == 5 or int(choice) == 6 :
            if (userChoice(choice, userAccount)):
                break
        else:
            print(pydb.Color.RED + "Wrong choice entered!!!" + pydb.Color.END)
            continue



    elif str(ans).lower() == 'u':

        ans = input(pydb.Color.BOLD + "Are you a new user (Enter 'Y' for Yes and 'N' for No; Enter 'EXIT' to exit): " + pydb.Color.END)

        if isChoiceEmpty(ans):
            continue

        if str(ans).lower() == 'y':
            user_id = input(pydb.Color.GREEN +  "Kindly enter a user id: " + pydb.Color.END)

            if isChoiceEmpty(user_id):
                continue

            if not validateUser(user_id):
                continue

            while True:
                password = input(pydb.Color.GREEN +  "Kindly enter a new password: "+ pydb.Color.END)
                if isChoiceEmpty(password):
                    continue
                re_enter_pass = input(pydb.Color.GREEN +  "Kindly re-enter the password: "+ pydb.Color.END)
                if isChoiceEmpty(re_enter_pass):
                    continue
                if re_enter_pass == password:
                    break
                print(pydb.Color.RED + "The re-entered password doesn't match the entered password" + pydb.Color.END)

            acc_amount = input(pydb.Color.GREEN + "Kindly deposit some amount to your new account: "+ pydb.Color.END)
            if isChoiceEmpty(acc_amount):
                continue

            userAccount  = pydb.Account(0, user_id, password,'User' ,acc_amount);

            userAccount = add_user(userAccount)

            choice = input(
                pydb.Color.BOLD + "If you want to modify your newly-added account, kindly enter your choice: \n 1 --- Withdrawal \n 2 --- Deposit \n 3 --- Your Bank Info \n 4 --- Exit  \n"+ pydb.Color.END)

            if isChoiceEmpty(choice):
                continue

            if int(choice) == 1 or int(choice) == 2 or int(choice) == 3 or int(choice) == 4:
                if (userChoice(choice, userAccount)):
                    break
            else:
                print(pydb.Color.RED + "Wrong choice entered!!!" + pydb.Color.END)
                continue

        elif str(ans).lower() == 'n':

            account_id = input(pydb.Color.GREEN +  "Kindly enter your account id: " + pydb.Color.END)
            if isChoiceEmpty(account_id):
                continue

            if not validateAccount(account_id):
                continue

            password = input(pydb.Color.GREEN +  "Kindly enter your password: " + pydb.Color.END)
            if isChoiceEmpty(password):
                continue

            userAccount = validatePassword(account_id, password)
            if userAccount is None:
                continue

            choice = input(pydb.Color.BOLD + "Kindly enter your choice: \n 1 --- Withdrawal \n 2 --- Deposit \n 3 --- Your Bank Info \n 4 --- Exit  \n"+ pydb.Color.END)
            if isChoiceEmpty(choice):
                continue

            if not choice.isnumeric():
                print(pydb.Color.RED + "Incorrect entry!!! \n" + pydb.Color.END)
                continue

            if int(choice) == 1 or int(choice) == 2 or int(choice) == 3 or int(choice) == 4:
                if (userChoice(choice, userAccount)):
                    break
            else:
                print(pydb.Color.RED + "Wrong choice entered!!!" + pydb.Color.END)
                continue

        elif str(ans).lower() == "exit":
            break

        else:
            print(pydb.Color.BOLD + pydb.Color.RED + "Invalid Entry"+ pydb.Color.END)
