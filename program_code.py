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

# write values of message in one row
# write values of keyword until no. of values in message == no. of values in keyword
# add values of message and keyword with same index
# for values >= 26, convert to corresponding values by starting again at index 0
# convert values to corresponding letters
# print final result
