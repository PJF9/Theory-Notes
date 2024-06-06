import random

low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
hight_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

size = int(input("Size of the password? : "))

low_letters_index = 0
hight_letters_index = 0
numbers_index = 0
special_chars_index = 0

for _ in range(size):
    num = random.randint(1, 4)

    low_letters_index += 1 if num == 1 else 0
    hight_letters_index += 1 if num == 2 else 0
    numbers_index += 1 if num == 3 else 0
    special_chars_index += 1 if num == 4 else 0

total_low_letters_list = []
total_hight_letters_list = []
total_numbers_list = []
total_special_chars_list = []

for _ in range(low_letters_index):
    i_letter = random.randint(0, len(low_letters)-1)
    total_low_letters_list.append(low_letters[i_letter])

for _ in range(hight_letters_index):
    i_letter = random.randint(0, len(hight_letters)-1)
    total_hight_letters_list.append(hight_letters[i_letter])

for _ in range(numbers_index):
    i_number = random.randint(0, len(numbers)-1)
    total_numbers_list.append(numbers[i_number])

for _ in range(special_chars_index):
    i_special_char = random.randint(0, len(special_chars)-1)
    total_special_chars_list.append(special_chars[i_special_char])

password = ""

for _ in range(size):
    random_list = random.randint(1, 4)

    password += total_low_letters_list[random.randint(0, len(total_low_letters_list)-1)] if random_list == 1 else ""
    password += total_hight_letters_list[random.randint(0, len(total_hight_letters_list)-1)] if random_list == 2 else ""
    password += total_numbers_list[random.randint(0, len(total_numbers_list)-1)] if random_list == 3 else ""
    password += total_special_chars_list[random.randint(0, len(total_special_chars_list)-1)] if random_list == 4 else ""


print(f"The password is: {password}")
