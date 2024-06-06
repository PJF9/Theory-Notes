def user_input(funct):
    def wrapper():
        try:
            choice = None
            while choice != 3:
                print("1) Add")
                print("2) Remove")
                print("3) Exit")
                print("-"*100)

                choice = int(input("Option: "))

                if (choice >= 1) and (choice < 3):
                    funct(choice)

        except ValueError:
            print("Only intages allowed... Exiting Program...")
    
    return wrapper()


@user_input
def app(choice=None):
    print(choice)
