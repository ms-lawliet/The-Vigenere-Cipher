# Write a program that asks the user for the plaintext (all uppercase letters,
# no spaces) and the keyword (all uppercase letters) and produce the
# ciphertext using the Vigenère cipher.

# take in message and keyword from user (capital letters, no space)
message_instruct = input("Enter your message: ").upper().strip()
key_instruct = input("Key: ").upper().strip()

# create class for Vigenère Cipher


class Cipher:
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

        # print final result


to_cipher = Cipher(message_instruct, key_instruct)        # for testing
to_cipher.produce_cipher()
