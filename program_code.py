# Write a program that asks the user for the plaintext (all uppercase letters,
# no spaces) and the keyword (all uppercase letters) and produce the
# ciphertext using the Vigenère cipher.

# take in message and keyword from user (capital letters, no space)
message_instruct = input("Enter your message: ").upper().strip()
key_instruct = input("Key: ").upper().strip()

# translate message and key to number values
# write values of message in one row
# write values of keyword until no. of values in message == no. of values in keyword
# add values of message and keyword with same index
# for values >= 26, convert to corresponding values by starting again at index 0
# convert values to corresponding letters
# print final result
