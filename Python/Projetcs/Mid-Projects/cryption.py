from time import time
from random import randint, shuffle
from string import ascii_letters, digits, punctuation
from os.path import isfile, isdir
from os import listdir


class __Reverse:

    @staticmethod
    def reverse_message(message):
        new_message = message[::-1]

        return new_message

    def reverse_file(self, full_file_path):
        if isfile(full_file_path):
            with open(full_file_path, 'r') as file:
                lines = [line.replace('\n', '') for line in file.readlines()]

            with open(full_file_path, 'w') as file:
                for line in lines[::-1]:
                    file.write(self.reverse_message(line) + '\n')


class __Encoder_Decode_key:

    @staticmethod
    def __get_encoder_base_of_time():

        number_str = str(time())[11:]

        for _ in range(7 - len(number_str)):
            number_str += str(randint(0, 9))

        number_str = number_str[::-1][:-1]
        number_str += str(randint(0, 9))
        number_str = number_str[::-1]

        squered_number_str = str(int(number_str) ** 2)

        for _ in range(14 - len(squered_number_str)):
            squered_number_str += str(randint(0, 9))  # 14

        time_encoder_int = sum([int(x) for x in squered_number_str])

        return time_encoder_int, squered_number_str

    @staticmethod
    def __get_encoder_base_of_key(key):

        key_list = [x for x in key]
        alpharithmetic_symbols = [x for x in ascii_letters + digits + punctuation + ' ']  # 95
        shuffle(alpharithmetic_symbols)

        key_to_ints = []
        for elem in key_list:
            for index in range(len(alpharithmetic_symbols)):
                if elem == alpharithmetic_symbols[index]:
                    key_to_ints.append(index)

        key_encoder_int = sum([int(x) for x in ''.join(list(map(str, key_to_ints)))])

        return key_encoder_int, ''.join(list(map(str, key_to_ints)))

    def __numbers_to_alpharithmetics(self, time_key, user_key, length):

        alpharithmetic_symbols = [x for x in ascii_letters + digits + punctuation + ' ']

        total_key = time_key + user_key

        doubles, temp = [str(length)], []
        for i in range(len(total_key)):
            temp.append(total_key[i])
            if i % 2 != 0:
                if temp[0] == '0':
                    doubles.append(temp[1])
                elif ((int(temp[0]) * 10) + int(temp[1]) > 94):
                    doubles.append(temp[0])
                    doubles.append(temp[1])
                else:
                    doubles.append(temp[0] + temp[1])                
                temp = []

        if len(total_key) % 2 != 0:
            doubles.append(total_key[-1])

        d = [alpharithmetic_symbols[int(double)] for double in doubles]

        return ''.join(d)

    def create_encoder_and_key(self, key):
        
        time_encoder, time_key = self.__get_encoder_base_of_time()
        key_encoder, user_key = self.__get_encoder_base_of_key(key)
        final_key = self.__numbers_to_alpharithmetics(time_key, user_key, len(key))

        encoder = str(time_encoder + key_encoder)
        encoder = int(encoder[:2]) - int(encoder[-1])
        length_based_part = int(str(len(key))[0]) + int(str(len(key))[1])
        encoder += length_based_part

        random_factor = randint(0, 9)
        encoder += random_factor
        final_key += str(random_factor)

        return encoder, final_key


class __Decoder:

    @staticmethod
    def create_decoder(decode_key):
        alpharithmetic_symbols = [x for x in ascii_letters + digits + punctuation + ' ']
        users_key_length = alpharithmetic_symbols.index(decode_key[0])
        decode_key = decode_key[1:]

        try:
            random_part = int(decode_key[-1])
        except ValueError:
            random_part = 0

        decode_key = decode_key[:-1]

        decoder = sum(int(x) for x in ''.join([str(alpharithmetic_symbols.index(x)) for x in decode_key]))
        decoder = int(str(decoder)[:2]) - int(str(decoder)[-1])
        length_part = int(str(users_key_length)[0]) + int(str(users_key_length)[1])
        decoder += length_part
        decoder += random_part

        return decoder


class Encrypt(__Encoder_Decode_key, __Reverse):

    def __binary_alphabet(self, num, index):
        if (num == '0') or (num == "0001"):
            return ['0', "0001"][index]
        elif (num == '1') or (num == "0010"):
            return ['1', "0010"][index]
        elif (num == '2') or (num == "0011"):
            return ['2', "0011"][index]
        elif (num == '3') or (num == "0100"):
            return ['3', "0100"][index]
        elif (num == '4') or (num == "0101"):
            return ['4', "0101"][index]
        elif (num == '5') or (num == "0110"):
            return ['5', "0110"][index]
        elif (num == '6') or (num == "0111"):
            return ['6', "0111"][index]
        elif (num == '7') or (num == "1000"):
            return ['7', "1000"][index]
        elif (num == '8') or (num == "1001"):
            return ['8', "1001"][index]
        elif (num == '9') or (num == "1010"):
            return ['9', "1010"][index]
        elif (num == 'S') or (num == "1101"): # Letter splitter
            return ['S', "1101"][index]

    def __to_binary(self, message):
        unicode_char_indexes = [str(ord(letter)) for letter in message]
        chars_of_indexes = []
        binary_chars_of_indexes = []
        encrypted_message = []

        for char in unicode_char_indexes:
            temp = []
            temp = [num for num in str(char)]
            chars_of_indexes.append(temp + ["S"])

        for msg_chrs in chars_of_indexes:
            temp = []
            for char in msg_chrs:
                temp.append(self.__binary_alphabet(char, 1))

            binary_chars_of_indexes.append(temp)

        for binary_list in binary_chars_of_indexes:
            encrypted_message.extend(binary_list)

        encrypted_message = ''.join(encrypted_message)

        return encrypted_message
        
    def __encrypt_message(self, message, key, reverse=True, create_key=True, enc=None, dec_key=None, line_length=0):
        if create_key:
            encoder, decode_key = self.create_encoder_and_key(key)
        else:
            encoder, decode_key = enc, dec_key

        if reverse:
            message = self.reverse_message(message)

        try:
            sort_encoder = int(str(encoder)[0]) + int(str(encoder)[1])
        except IndexError:
            sort_encoder = encoder

        first_encrypted_message = ''
        for letter in message:
            if ord(letter) + sort_encoder > 126:
                first_encrypted_message += "-!-"
                first_encrypted_message += chr(ord(letter) - sort_encoder)
            else:
                first_encrypted_message += chr(ord(letter) + sort_encoder)

        letters = [letter for letter in first_encrypted_message]

        encrypted_message = ''.join([chr(ord(letter) + encoder + line_length) for letter in letters])

        encrypted_message = ''.join([self.__to_binary(letter) for letter in encrypted_message])
        
        return encrypted_message, decode_key

    def __encrypt_line_length(self, length):
        encoded_length = ""

        one = "000-"
        two = "001-"
        three = "010-"
        four = "100-"
        five = "011-"
        six = "110-"
        seven = "101-"
        eight = "111-"
        nine = "000A"
        zero = "001A"

        for letter in str(length):
            if letter == "1":
                encoded_length += one
            elif letter == "2":
                encoded_length += two
            elif letter == "3":
                encoded_length += three
            elif letter == "4":
                encoded_length += four
            elif letter == "5":
                encoded_length += five
            elif letter == "6":
                encoded_length += six
            elif letter == "7":
                encoded_length += seven
            elif letter == "8":
                encoded_length += eight
            elif letter == "9":
                encoded_length += nine
            elif letter == "0":
                encoded_length += zero

        return encoded_length 

    def __encrypt_file(self, full_file_path, key, create_key=True, enc=None, dec_key=None):
        if create_key:
            encoder, decode_key = self.create_encoder_and_key(key)
        else:
            encoder, decode_key = enc, dec_key

        if isfile(full_file_path):

            self.reverse_file(full_file_path)

            with open(full_file_path, 'r') as file:
                content = [line.replace('\n', '') for line in file.readlines()]

            encrypted_content = [list(self.__encrypt_message(line, key, False, False, encoder, decode_key, len(line)))[0] for line in content]

            with open(full_file_path, 'w', encoding="utf-8") as file:
                file.write("###--- It's encrypted mate ---###\n\n")
                i = 0
                for line in encrypted_content:
                    file.write(line + "$$$" + self.__encrypt_line_length(len(content[i])) + '\n')
                    i += 1

            return decode_key

    def __encrypt_folder(self, full_folder_path, key, create_key=True, enc=None, dec_key=None):
        if isdir(full_folder_path):
            if create_key:
                encoder, decode_key = self.create_encoder_and_key(key)
            else:
                encoder, decode_key = enc, dec_key

            files = [full_folder_path + '\\' + x for x in listdir(full_folder_path) if isfile(full_folder_path + '\\' + x)]

            for file in files:
                self.__encrypt_file(file, key, False, encoder, decode_key)

            return decode_key

    def __encrypt_directory(self, full_dir_path, key, create_key=True, enc=None, dec_key=None):
        if isdir(full_dir_path):
            if create_key:
                encoder, decode_key = self.create_encoder_and_key(key)
            else:
                encoder, decode_key = enc, dec_key
            
            self.__encrypt_folder(full_dir_path, key, False, encoder, decode_key)

            folders = [full_dir_path + '\\' + x for x in listdir(full_dir_path) if isdir(full_dir_path + '\\' + x)]
            
            for folder in folders:
                self.__encrypt_directory(folder, key, False, encoder, decode_key)

            return decode_key

    def go(self, encryption_argument, key):
        if (len(key) > 10) and (len(key) < 94): 
            if isdir(encryption_argument):
                decode_key = self.__encrypt_directory(encryption_argument, key)
                encrypted_message = None
            elif isfile(encryption_argument):
                decode_key = self.__encrypt_file(encryption_argument, key)
                encrypted_message = None
            else:
                encrypted_message, decode_key = self.__encrypt_message(encryption_argument, key)

            return encrypted_message, decode_key
        else:
            print("Invalid Key: Key not in range. Range is: 11 - 93")
            
            return None, None


class Decrypt(__Decoder, __Reverse):

    def __binary_alphabet(self, num, index):
        if (num == '0') or (num == "0001"):
            return ['0', "0001"][index]
        elif (num == '1') or (num == "0010"):
            return ['1', "0010"][index]
        elif (num == '2') or (num == "0011"):
            return ['2', "0011"][index]
        elif (num == '3') or (num == "0100"):
            return ['3', "0100"][index]
        elif (num == '4') or (num == "0101"):
            return ['4', "0101"][index]
        elif (num == '5') or (num == "0110"):
            return ['5', "0110"][index]
        elif (num == '6') or (num == "0111"):
            return ['6', "0111"][index]
        elif (num == '7') or (num == "1000"):
            return ['7', "1000"][index]
        elif (num == '8') or (num == "1001"):
            return ['8', "1001"][index]
        elif (num == '9') or (num == "1010"):
            return ['9', "1010"][index]
        elif (num == 'S') or (num == "1101"): # Letter splitter
            return ['S', "1101"][index]
    
    def __from_binary(self, b_message, from_file=True):
        if from_file:
            splitting_b_message = [b_message[0][i-4:i] for i in range(len(b_message[0])) if (i % 4 == 0) and (i != 0)]
        else:
            splitting_b_message = [b_message[i-4:i] for i in range(len(b_message)) if (i % 4 == 0) and (i != 0)]

        split_b_message_to_indexes = []
        temp = []
        for binary_index in splitting_b_message:
            temp.append(binary_index)

            if binary_index == "1101":
                split_b_message_to_indexes.append(temp)
                temp = []

        split_b_message_to_indexes.append(temp + ["1101"])

        from_binary_to_index = []
        for binary_list_indexes in split_b_message_to_indexes:
            temp = []
            temp = [self.__binary_alphabet(b_index, 0) for b_index in binary_list_indexes]
            from_binary_to_index.append(temp)

        one_dim_of_indexes = []
        for indexes_list in from_binary_to_index:
            string_index = ''
            for index in indexes_list[:-1]:
                string_index += index

            if string_index != '':
                one_dim_of_indexes.append(int(string_index))

        decrepted_message = ''.join([chr(acsi_index) for acsi_index in one_dim_of_indexes])

        return decrepted_message

    def __decrypt_message(self, encrypted_message, decode_key, reverse=True, line_length=0, from_file=False):
        decoder = self.create_decoder(decode_key)
        try:
            sort_decoder = int(str(decoder)[0]) + int(str(decoder)[1])
        except IndexError:
            sort_decoder = decoder

        if from_file:
            de_binary_encrypted_message = self.__from_binary(encrypted_message)
        else:
            de_binary_encrypted_message = self.__from_binary(encrypted_message, False)

        encrypted_letters = [x for x in de_binary_encrypted_message]

        first_decrypted_message = ''.join([chr(ord(x) - decoder - line_length) for x in encrypted_letters])

        decrypted_message = ''
        proceed = False
        wait = False
        i_bug_fix = 0
        for i in range(len(first_decrypted_message)):
            if i_bug_fix == 3:
                wait = False
            try:
                if (first_decrypted_message[i] == '-') and (first_decrypted_message[i+1] == '!') and (first_decrypted_message[i+2] == '-'):
                    proceed = True
                    wait = True
                    i_bug_fix = 0
            except IndexError:
                pass
            
            if wait:
                i_bug_fix += 1
            else:
                if proceed:
                    decrypted_message += chr(ord(first_decrypted_message[i]) + sort_decoder)
                    proceed = False
                else:
                    decrypted_message += chr(ord(first_decrypted_message[i]) - sort_decoder)

        if reverse:
            decrypted_message = self.reverse_message(decrypted_message)

        return decrypted_message

    def __decrypt_line_length(self, line):
        line_length = line.split("$$$")[-1]
        decoded_length = ""

        one = "000"
        two = "001"
        three = "010"
        four = "100"
        five = "011"
        six = "110"
        seven = "101"
        eight = "111"
        nine = "000A"
        zero = "001A"

        for letter in line_length.split('-'):
            if letter == one:
                decoded_length += "1"
            elif letter == two:
                decoded_length += "2"
            elif letter == three:
                decoded_length += "3"
            elif letter == four:
                decoded_length += "4"
            elif letter == five:
                decoded_length += "5"
            elif letter == six:
                decoded_length += "6"
            elif letter == seven:
                decoded_length += "7"
            elif letter == eight:
                decoded_length += "8"
            elif letter == nine:
                decoded_length += "9"
            elif letter == zero:
                decoded_length += "0"

        return decoded_length 

    def __decrypt_file(self, full_encrypted_file_path, decode_key):
        if isfile(full_encrypted_file_path):

            with open(full_encrypted_file_path, 'rb') as file:
                content_bytes = file.read()
            
            content_bytes = content_bytes.split('\r'.encode("utf-8"))
            content = [x.decode("utf-8").replace('\n', '') for x in content_bytes[2:-1]]

            decrypted_content = [self.__decrypt_message(line.split("$$$")[:-1], decode_key, False, int(self.__decrypt_line_length(line)), True) if line.split("$$$")[0] != '' else '' for line in content]
            decrypted_content = [x[::-1] for x in decrypted_content[::-1]]

            with open(full_encrypted_file_path, 'w') as file:
                for line in decrypted_content:
                    file.write(line + '\n')

    def __decrypt_folder(self, full_encrypted_folder_path, decode_key):
        if isdir(full_encrypted_folder_path):
            encrypted_files = [full_encrypted_folder_path + '\\' + x for x in listdir(full_encrypted_folder_path) if isfile(full_encrypted_folder_path + '\\' + x)]

            for file in encrypted_files:
                self.__decrypt_file(file, decode_key)

    def __decrypt_directory(self, full_encrypted_dir_path, decode_key):
        if isdir(full_encrypted_dir_path):
            self.__decrypt_folder(full_encrypted_dir_path, decode_key)

            folders = [full_encrypted_dir_path + '\\' + x for x in listdir(full_encrypted_dir_path) if isdir(full_encrypted_dir_path + '\\' + x)]

            for folder in folders:
                self.__decrypt_directory(folder, decode_key)

    def go(self, decryption_argument, decode_key):
        try:
            if isdir(decryption_argument):
                self.__decrypt_directory(decryption_argument, decode_key)
                decrypted_message = None
            elif isfile(decryption_argument):
                self.__decrypt_file(decryption_argument, decode_key)
                decrypted_message = None
            else:
                decrypted_message = self.__decrypt_message(decryption_argument, decode_key)

            return decrypted_message
        except IndexError:
            print("Invalid Decode Key: This key cannot decrypt the specified message.")
