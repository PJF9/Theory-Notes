import itertools
import time


def get_password():
    password = ">A7C9"
    password_size = len(password)

    return password, password_size


def password_convertion(password, password_size):
    new_password = []
    for index in range(password_size):
        new_password.append(password[index])

    password = tuple(new_password)

    return password


start = time.time()


def main():
    new_password, password_size = get_password()
    password = password_convertion(new_password, password_size)

    low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    up_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    digits = ["!", "@", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", 
                "{", "]", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/",
                "?", "`", "~"]

    iterator_letters = itertools.product(low_letters + up_letters + numbers + digits, repeat=password_size)

    total_comb = pow(24, password_size)
    print(f"----> The programm is searching amomg {total_comb} combinations...")

    for letter in iterator_letters:
        print(letter)
        if letter == password:
            password = letter
            break

    print(f"----> The total time that needed was {time.time() - start}")

    string_password = ""
    for i in range(password_size):
        string_password += password[i]

    print(f"----> The password is '{string_password}'")


main()
