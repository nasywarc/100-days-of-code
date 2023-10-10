alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def caesar(text, shift, direction):
    index_list = []
    new_word = []
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    for letter in text:
        index_list.append(alphabet.index(letter))
    for index in range(len(index_list)):
        if direction == 'encode':
            index_list[index] += shift
            while index_list[index] > 25:
                index_list[index] -= 26
        elif direction == 'decode':
            while index_list[index] < 0:
                index_list[index] += 26
        else:
            print("Your input is invalid.")
    for cipher in index_list:
        new_word.append((alphabet[cipher]))
        if direction == 'encode':
            print("The encoded text is ", "".join(new_word))
        else:
            print("The decoded text is ", "".join(new_word))


def encrypt(plain_text, shift_amount):
    index_list = []
    new_word = []
    for letter in plain_text:
        index_list.append(alphabet.index(letter))
    for index in range(len(index_list)):
        index_list[index] += shift_amount
        while index_list[index] > 25:
            index_list[index] -= 26
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
        while index_list[index] < 0:
            index_list[index] += 26
    for cipher in index_list:
        new_word.append((alphabet[cipher]))
    print("".join(new_word))


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
