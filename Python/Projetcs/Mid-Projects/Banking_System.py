import os
import sqlite3
import logging

# Make the app prettier
os.system("cls")
os.system("color 03")

# Creating the table to store our data
conn = sqlite3.connect("bank_system.db")
c = conn.cursor()
c.execute('''
        CREATE TABLE data(
            account_name text,
            account_type text,
            account_password text,
            account_money real
        )
    ''')
conn.commit()

# Creating the Logegr
logger = logging.getLogger("Bank Logger")
# Setting the loger level
logger.setLevel(logging.INFO)
# Create a formatter for the logger
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
# Create the file that the logger will take place
file_handler = logging.FileHandler("Banking_status.log")
# Add the formatter to the log file
file_handler.setFormatter(formatter)
# Add the logger and the log file together
logger.addHandler(file_handler)


class BankingSystem:

    def __init__(self):
        # initialize the class wembers we want
        self.__account_name = ""
        self.__account_type = ""
        self.__account_password = ""
        self.__account_money = 0
        self.__id = 0

    def __repr__(self):
        if (self.__account_type == "P") or (self.__account_type == "p"):
            return f'''
            /~ Account Name: {self.__account_name}
            /~ Account Type: Personal
            /~ Account Balance: {self.__account_money}
            '''
        return f'''
        /~ Account Name: {self.__account_name}
        /~ Account Type: Business
        /~ Account Balance: {self.__account_money}
        '''

    def set_account_name(self):
        name = input("/~ Please Insert The Account Name You Want: ")
        print()

        if len(name) >= 20:
            print("/~ Invalid Account Name: Account Name Too Long ( 2-20 ) ~\\")
            print("/~ Account Name Still Unsigned ~\\")

        elif (name == "") or (len(name) == 1):
            print("/~ Invalid Account Name: Account Name Too Small ( 2-20 ) ~\\")
            print("/~ Account Name Still Unsigned ~\\")

        else:
            self.__account_name = name
            print("/~ Your Account Name Has Been Set Succesfully ~\\")

    def set_account_type(self):
        type_ = input("/~ Please Insert The Account Type You Want: ")
        print()
        if (type_ == "p") or (type_ == "P") or (type_ == "b") or (type_ == "B"):
            self.__account_type = type_
            print("/~ Your Account Type Has Been Set Succesfully ~\\")
        elif len(type_) > 1:
            print("/~ Invalid Account Type: The Length Must Be Equal To 1 ~\\")

        else:
            print("/~ Inavlid Account Type: The Only Options Are ~ P,p -> Personal, B,b -> Business ~\\")

    def set_account_password(self):
        password = input("/~ Please Insert The Account Password You Want: ")
        print()
        self.__account_password = password
        print("/~ Your Account Password Has Been Set Succesfully ~\\")

    def change_account_password(self):
        while True:
            print("---"*20)
            password = input("/~ Please Type Your Previous Password: ")

            if password == self.__account_password:
                while True:
                    new_password = input("/~ Please Insert Your New Password: ")
                    confrim_password = input("/~ Please Verify Your New Password: ")

                    if new_password == confrim_password:
                        self.__account_password = new_password
                        print()
                        print("/~ Your Account Password Has Been Changed Succesfully ~\\")
                        print("---"*20)
                        return
                    else:
                        print()
                        print("/~ Passwords Don't Machts ~\\")
                        print("---"*20)

                        while True:
                            choice_1 = input(
                                "/~ Want to Cancel The Account Change Process? ( y-n ): ")
                            if (choice_1 == "y") or (choice_1 == "n"):
                                break
                            else:
                                print("/~ Sorry, Only Options Are ( y-n ) ~\\")

                        if choice_1 == "y":
                            print("---"*20)
                            print("/~ Quitting Out Process ~\\")
                            return
            else:
                print()
                print("/~ Your Password Is Incorrect ~\\")
                print("---"*20)
                while True:
                    choice_2 = input("/~ Want To Try Again? ( y-n ): ")
                    if (choice_2 == "y") or (choice_2 == "n"):
                        break
                    else:
                        print("/~ Sorry, Options Are ( y-n ) ~\\")

                if choice_2 == "n":
                    print("---"*20)
                    print("/~ Quitting Out Process ~\\")
                    return

    def change_account_name(self):
        while True:
            choice = input("/~ Are You Sure You Want To Change Your Account Name? ( y-n ): ")
            if (choice == "y") or (choice == "n"):
                break
            else:
                print("/~ Sorry, Only Options Are ( y-n ) ~\\")

        if choice == "y":
            new_account_name = input("/~ Insert The New Account Name You Want: ")
            if (len(new_account_name) <= 1) or (len(new_account_name) > 20) or (new_account_name == ""):
                print("---"*20)
                print("/~ Invalid Account Name: Account Name Range Is ( 2-21 )")
                print("/~ Your Account Name Have Been Not Updated")
            else:
                self.__account_name = new_account_name
                print()
                print("/~ Your Account Name Have Been Updated ~\\")
                print("---"*20)
        else:
            print("/~ Quitting Out Process ~\\")

    def change_account_type(self):
        while True:
            choice = input("/~ Are You Sure You Want To Change Your Account Type ( y-n ): ")
            if (choice == "y") or (choice == "n"):
                break
            else:
                print("/~ Sorry, Only Options Are ( y-n ) ~\\")

        if choice == "y":
            new_account_type = input("/~ Insert The New Account Type You Want: ")
            if (new_account_type != "p") and (new_account_type != "P") \
                    and (new_account_type != "b") \
                    and (new_account_type != "B"):

                print("---"*20)
                print("/~ Invalid Account Type: Only Options Are p-P, b-B ~\\")
                print("/~ Your Account Type Have Been Not Updated ~\\")
            else:
                self.__account_type = new_account_type
                print()
                print("/~ Your Account Type Have Been Updated ~\\")
                print("---"*20)
        else:
            print("/~ Quitting Out Process ~\\")

    def deposit(self):
        while True:
            try:
                deposit_ammount = float(
                    input("/~ Please Insert The Ammount You Want To Deposit To Your Account: "))
            except ValueError:
                print("/~ Invalid Deposit Ammount: No Characters Allowed ~\\")
                print("/~ Your Account Balance Has Not Been Changed ~\\")
                print()

                while True:
                    choice_1 = input("/~ What To Try Again? ( y-n ): ")
                    if (choice_1 == "y") or (choice_1 == "n"):
                        break
                    else:
                        print("/~ Sorry, Only Options Are ( y-n ) ~\\")

                if choice_1 == "y":
                    print("---"*20)
                else:
                    print("---"*20)
                    print("/~ Your Account Balance Has Not Been Changed ~\\")
                    print("/~ Quitting Deposit Process ~\\")
                    return

            else:
                if (deposit_ammount < 0):
                    print("/~ Invalid Deposit Ammount: Only Positives Numbers Allowed ~\\")
                    print("/~ Your Account Balance Has Not Been Changed ~\\")
                    print()

                    while True:
                        choice_2 = input("/~ Want To Try Again ( y-n )? : ")
                        if (choice_2 == "y") or (choice_2 == "n"):
                            break
                        else:
                            print("/~ Sorry Only Options Are ( y-n ) ~\\")

                    if choice_2 == "n":
                        print("/~ Your Account Balance Has Not Been Changed ~\\")
                        print("/~ Quitting Deposit Process ~\\")
                        return

                else:
                    print(
                        f"/~ You Have Added To You Account {deposit_ammount}$ To Your Account ~\\")
                    print(f"/~ Your Account Now Has {self.__account_money + deposit_ammount}$ ~\\")
                    print()
                    print("/~ Quitting Deposit Process ~\\")
                    self.__account_money += deposit_ammount

                    logger.info(f"-{self.__account_name} has deposit {deposit_ammount}$")

                    break

    def withdraw(self):
        while True:
            try:
                withdraw_ammount = float(
                    input("/~ Please Insert The Ammount You Want To Withdraw From Your Account: "))
            except ValueError:
                print("/~ Invalid Withdraw Ammount: No Characters Allowed ~\\")
                print("/~ Your Account Balance Has Not Been Changed ~\\")
                print()

                while True:
                    choice_1 = input("/~ What To Try Again? ( y-n ): ")
                    if (choice_1 == "y") or (choice_1 == "n"):
                        break
                    else:
                        print("/~ Sorry, Only Options Are ( y-n ) ~\\")

                if choice_1 == "y":
                    print("---"*20)
                else:
                    print("---"*20)
                    print("/~ Your Account Balance Has Not Been Changed ~\\")
                    print("/~ Quitting Deposit Process ~\\")
                    return

            else:
                if (withdraw_ammount < 0):
                    print("/~ Invalid Withraw Ammount: Only Positives Numbers Allowed ~\\")

                    while True:
                        choice_2 = input("/~ Want To Try Again ( y-n )? : ")
                        if (choice_2 == "y") or (choice_2 == "n"):
                            break
                        else:
                            print("/~ Sorry Only Options Are ( y-n ) ~\\")

                    if choice_2 == "n":
                        print("/~ Your Account Balance Has Not Been Changed ~\\")
                        print("/~ Quitting Deposit Process ~\\")
                        return

                elif (withdraw_ammount > self.__account_money):
                    print("/~ Sorry You Don't Have Such Money On Your Account ~\\")

                    while True:

                        choice_3 = input("/~ Want To Try Again? ( y-n ): ")
                        if (choice_3 == "y") or (choice_3 == "n"):
                            break
                        else:
                            print("/~ Sorry Only Options Are ( y-n ) ~\\")

                    if choice_3 == "n":
                        print("/~ Your Account Balance Has Not Been Changed ~\\")
                        print("/~ Quitting Withdraw Process ~\\")
                        return

                else:
                    print(f"/~ You Have Withraw {withdraw_ammount}$ From Your Account ~\\")
                    print(
                        f"/~ Your Account Has {self.__account_money - withdraw_ammount}$ Left ~\\")
                    print("/~ Quitting Deposit Process ~\\")
                    self.__account_money -= withdraw_ammount

                    logger.info(f"-{self.__account_name} has withdraw {withdraw_ammount}$")

                    break

    def get_account_name(self):
        if self.__account_name != "":
            return self.__account_name
        return "None"

    def get_account_type(self):
        if self.__account_type != "":
            return self.__account_type
        return "None"

    def get_account_money(self):
        if self.__account_money >= 0:
            return str(self.__account_money)
        return "None"

    def get_account_password(self):
        if self.__account_password != "":
            return self.__account_password
        return "None"

    def show_account(self):
        print(f"/~ Account Name --> {self.__account_name}")
        print(f"/~ Account Type --> {self.__account_type}")
        print(f"/~ Account Balance --> {self.__account_money}")


def option():
    input("/~ Press Enter To Continue...")
    os.system("cls")


def menu_choices():
    print("---"*20)
    print("\tBanking System")
    print("---"*20)
    print('''
      | 1. Change Account Name      ~\\  |
      | 2. Change Account Type      ~\\  |
      | 3. Change Account Password  ~\\  |
      |---------------------------------|
      | 4. Deposit Ammount          ~\\  |
      | 5. Withdraw Ammount         ~\\  |
      |---------------------------------|
      | 6. Get Account Name         ~\\  |
      | 7. Get Account Password     ~\\  |
      | 8. Get Account Type         ~\\  |
      | 9. Get Account Balance      ~\\  |
      |---------------------------------|
      | 10. Show Overall Account    ~\\  |
      |---------------------------------|
      | 11. Exit Programm           ~\\  |
    ''')
    print("---"*20)


def menu(account):
    menu_choices()

    conn = sqlite3.connect("bank_system.db")
    c = conn.cursor()

    while True:

        user_choice = int(input("/~ Insert Account Action: "))
        if (user_choice > 11) or (user_choice < 1):
            print("/~ Sorry Only Options Are ( 1-11 ) ~\\")

            while True:
                print()
                user_choice = input("/~ Want To Try Again? ( y-n ): ")
                if (user_choice == "y") or (user_choice == "n"):
                    os.system("cls")
                    menu_choices()
                    break
                else:
                    print("/~ Sorry Only Options Are ( y-n ) ~\\")

            if user_choice == "n":
                print("/~ Exiting Programm ~\\")
                return

        if user_choice == 1:
            print("---"*20)
            account.change_account_name()
            c.execute('''
                UPDATE data SET account_name = :new_name WHERE oid = :id_key
            ''',
                      {
                          "new_name": account.get_account_name(),
                          "id_key": account._BankingSystem__id
                      }
                      )
            conn.commit()
            print()
            option()
            menu_choices()

        elif user_choice == 2:
            print("---"*20)
            account.change_account_type()
            c.execute('''
                UPDATE data SET account_type = :new_type WHERE oid = :id_key
            ''',
                      {
                          "new_type": account.get_account_type(),
                          "id_key": account._BankingSystem__id
                      }
                      )
            conn.commit()
            print()
            option()
            menu_choices()

        elif user_choice == 3:
            print("---"*20)
            account.change_account_password()
            c.execute('''
                UPDATE data SET account_money = :new_money WHERE oid = :id_key
            ''',
                      {
                          "new_money": account.get_account_money(),
                          "id_key": account._BankingSystem__id
                      }
                      )
            conn.commit()
            print()
            option()
            menu_choices()

        elif user_choice == 4:
            print("---"*20)
            account.deposit()
            c.execute('''
                UPDATE data SET account_money = :new_money WHERE oid = :id_key
            ''',
                      {
                          "new_money": account.get_account_money(),
                          "id_key": account._BankingSystem__id
                      }
                      )
            conn.commit()
            print()
            option()
            menu_choices()

        elif user_choice == 5:
            print("---"*20)
            account.withdraw()
            c.execute('''
                UPDATE data SET account_money = :new_money WHERE oid = :id_key
            ''',
                      {
                          "new_money": account.get_account_money(),
                          "id_key": account._BankingSystem__id
                      }
                      )
            conn.commit()
            print()
            option()
            menu_choices()

        elif user_choice == 6:
            print("---"*20)
            print(f"/~ Account Name: {account.get_account_name()}")
            print()
            option()
            menu_choices()

        elif user_choice == 7:
            print("---"*20)
            print(f"/~ Account Password: {account.get_account_password()}")
            print()
            option()
            menu_choices()

        elif user_choice == 8:
            print("---"*20)
            if (account.get_account_type == "p") or (account.get_account_type == "P"):
                print("/~ Account Type: Personal")
            else:
                print("/~ Account Type Business")
            print()
            option()
            menu_choices()

        elif user_choice == 9:
            print("---"*20)
            print(f"/~ Account Balance: {account.get_account_money()}")
            print()
            option()
            menu_choices()

        elif user_choice == 10:
            print(account)
            print()
            option()
            menu_choices()

        elif user_choice == 11:
            print("/~ Quitting Programm ~\\")
            break


def login(account):
    user_account_name = input("/~ Account Name: ")
    user_password = input("/~ Account Password: ")
    print()

    conn = sqlite3.connect("bank_system.db")
    c = conn.cursor()

    c.execute("SELECT *,oid FROM data")
    all_data = c.fetchall()

    for data in all_data:
        if (user_account_name == data[0]) and (user_password == data[2]):
            correct_account_name = True
            correct_password = True
            account._BankingSystem__account_name = user_account_name
            account._BankingSystem__account_password = user_password
            account._BankingSystem__account_type = data[1]
            account._BankingSystem__account_money = data[3]
            account._BankingSystem__id = data[-1]
            break

        elif (user_account_name != data[0]) and (user_password == data[2]):
            correct_account_name = False
            correct_password = True
            break

        elif (user_account_name == data[0]) and (user_password != data[2]):
            correct_account_name = True
            correct_password = False
            break

        else:
            correct_account_name = False
            correct_password = False

    if correct_account_name and correct_password:
        print("/~ You Have Logged In Succesfully ~\\")
        print("---"*20)
        option()
        conn.close()
        return True

    elif correct_account_name and not correct_password:
        print("/~ Incorrect Password ~\\")
        print("---"*20)
        conn.close()
        return False

    elif not correct_account_name and correct_password:
        print("/~ Incorrect Account Name ~\\")
        print("---"*20)
        conn.close()
        return False

    else:
        print("/~ Both Account Name And Account Password Are Incorrect ~\\")
        print("---"*20)
        conn.close()
        return False


def register(account):
    while True:
        choice = input("/~ Do You Want To Register? ( y-n ): ")
        print("---"*20)
        if (choice == "y") or (choice == "n"):
            break
        else:
            print("/~ Sorry Only Options Are ( y-n ) ~\\")

    if choice == "n":
        print("/~ Then I have Nothing Left For You ~\\")
        print("/~ Quitting Programm ~\\")
        print("---"*20)

    else:
        conn = sqlite3.connect("bank_system.db")
        c = conn.cursor()

        while True:
            account.set_account_name()
            print("---"*20)
            if account.get_account_name() != "None":
                break
            else:
                print("/~ None Is An Incorrect Account Name ~\\")

        while True:
            account.set_account_type()
            print("---"*20)
            if account.get_account_type() != "None":
                break

        while True:
            account.set_account_password()
            print("---"*20)
            if account.get_account_password() != "None":
                break

        c.execute("INSERT INTO data VALUES(:account_name, :account_type, :account_password, :account_money)",
                  {
                      "account_name": account.get_account_name(),
                      "account_type": account.get_account_type(),
                      "account_password": account.get_account_password(),
                      "account_money": account.get_account_money()
                  }
                  )
        conn.commit()
        conn.close()
        print()
        option()
        menu(account)


def login_register():
    print("---"*20)
    print("\tBanking System")
    print("---"*20)

    while True:
        choice = input("/~ Have You Already A Banking Account? ( y-n ): ")
        if (choice == "y") or (choice == "n"):
            break
        else:
            print("/~ Sorry, Only Options Are ( y-n ) ~\\")

    print("---"*20)

    return choice


def keyboard_interaction(funct):
    def wrapper(*args, **kwargs):
        try:
            rv = funct(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n")
            print("/~ Rage Quit ~\\")
            print("---"*20)
        else:
            return rv
    return wrapper


@keyboard_interaction
def main():
    account = BankingSystem()
    user_choice_1 = login_register()

    if user_choice_1 == "y":
        while True:
            login_reasult = login(account)

            if not login_reasult:
                while True:
                    user_choice_2 = input("/~ What To Try Again ( y-n ): ")
                    print()
                    if (user_choice_2 == "y") or (user_choice_2 == "n"):
                        break
                    else:
                        print("/~ Sorry, Only Options Are ( y-n ) ~\\")

                if user_choice_2 == "n":
                    os.system("cls")
                    print("---"*20)
                    print("\tBanking System")
                    print("---"*20)
                    register(account)
                    menu(account)
                    break

            else:
                menu(account)
                break

    else:
        register(account)


if __name__ == "__main__":
    main()
    c = conn.cursor()
    c.execute("SELECT *,oid FROM data")
    data = c.fetchall()

    total_bank_balance = 0
    for d in data:
        total_bank_balance += float(d[-2])

    logger.info(f"-Total Bank Balance is {total_bank_balance}$")
    logger.info("\n")

    conn.close()
