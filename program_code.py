# Write a program that asks the user for the plaintext (all uppercase letters,
# no spaces) and the keyword (all uppercase letters) and produce the
# ciphertext using the Vigenère cipher.

# import built-in modules for design
import pyfiglet
import time
from colorama import Back

# create list of colors for font
yellow = "\033[93m"
red = "\033[91m"
magenta = "\033[95m"
white = "\033[97m"
green = "\033[92m"
colors = [yellow, red, magenta, white]

# print program title
print(f'{green}='*185)
print(Back.BLACK + pyfiglet.figlet_format('The Vigenere Cipher', font='cybermedium', width=175, justify='center'), end='')
print(Back.RESET + '='*185 + '\n')
time.sleep(0.5)

# take in message and keyword from user (capital letters, no space)
message_instruct = f"{green}Enter your message: "

for letter in message_instruct:
    print(letter, end='')
    time.sleep(0.01)
user_message = input().upper().strip()

key_instruct = f"{green}Key: "

for letter in key_instruct:
    print(letter, end='')
    time.sleep(0.01)

user_key = input().upper().strip()
time.sleep(0.3)


class Cipher:         # create class for Vigenère Cipher
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def produce_cipher(self):           # translate message and key to number values
        # create dict for letters and corresponding values
        translation = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                       'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                       'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

        # create lists to contain results of every step
        translated_message = []  # translated values of message
        translated_key = []  # translated values of key
        add_list = []  # added values
        mod_list = []  # mod values
        ciphertext = []  # ciphered text
        converted_cipher = ''  # ciphered text in str

        # translate each letter in message and key by getting value in dict
        for i in range(len(self.message)):
            if self.message[i] in translation:
                trans1 = translation.get(self.message[i])
                translated_message.append(trans1)  # insert each value to translated_message

        n = 0
        while n != len(translated_message):  # execute until len(translated_key) == len(translated_message)
            for i in range(len(self.key)):
                if self.key[i] in translation:
                    trans2 = translation.get(self.key[i])
                    translated_key.append(trans2)  # insert each value to translated_key
                    n += 1
                if n == len(translated_message):
                    break

        # add values with same index in translated_message and translated_key
        for i in range(len(translated_message)) and range(len(translated_key)):
            add = translated_message[i] + translated_key[i]
            add_list.append(add)  # insert each result in add_list

        # for values >= 26, convert to corresponding values by starting again at index 0
        # add result to mod_list
        for i in range(len(add_list)):
            if add_list[i] >= 26:
                mod = add_list[i] - 26
                mod_list.append(mod)
            else:
                mod_list.append(add_list[i])

        # find corresponding letters to accumulated values in mod_list
        for i in range(len(mod_list)):
            for each_letter, value in translation.items():
                if value == mod_list[i]:
                    ciphertext.append(each_letter)  # add result to ciphertext

        # convert each element in ciphertext to str and concatenate to converted_cipher
        for i in range(len(ciphertext)):
            str_cipher = str(ciphertext[i])
            converted_cipher += f'{str_cipher} '

        # print final result
        fin_output = (pyfiglet.figlet_format(converted_cipher, font='basic', width=140))
        txt = f'{green}\nGenerated cipher text: \n{Back.BLACK + fin_output}'

        count = 0
        while count != 4:
            for i in range(len(colors)):
                loading = (f"{colors[i]}Generating cipher text" + "." * count)
                print('\r', loading, end="")
                time.sleep(0.6)
                count += 1
                if count == 4:
                    print('\r' + '                                   ', end='')
                    break
            time.sleep(0.4)

        for each_letter in txt:
            print(each_letter, end='')
            time.sleep(0.01)


to_cipher = Cipher(user_message, user_key)
to_cipher.produce_cipher()
