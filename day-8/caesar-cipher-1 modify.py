alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):
    index_list = []
    new_word = []
    for letter in plain_text:
        index_list.append(alphabet.index(letter))
    # print(index_list)
    for index in range(len(index_list)):
        index_list[index] += shift_amount
        if index_list[index] > 26:
            index_list[index] -= 27
    for cipher in index_list:
        new_word.append((alphabet[cipher]))
    print("".join(new_word))


def decrypt(cipher_text, shift_amount):
    index_list = []
    new_word = []
    for letter in cipher_text:
        index_list.append(alphabet.index(letter))
    for index in range(len(index_list)):
        index_list[index] -= shift_amount
    for cipher in index_list:
        new_word.append((alphabet[cipher]))
    print("".join(new_word))

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("Your input is invalid.")

# print(len(alphabet))
