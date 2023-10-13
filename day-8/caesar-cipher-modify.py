import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_word, shift, direction):
    letter = []
    symbol = []
    letter_index = []
    new_index = ""
    new_word = []
    end_word = []
    final_result = ""
    loop = True

    while loop:
        for pos in range(len(start_word)):
            if start_word[pos] in alphabet:
                letter_index.append(pos)
                letter.append(alphabet.index(start_word[pos]))
            else:
                symbol.append(start_word[pos])

        if direction == 'decode':
            shift *= -1

        for index in letter:
            new_index = index + shift
            while new_index > 25:
                new_index -= 26
            while new_index < 0:
                new_index += 26
            new_word.append(alphabet[new_index])

        start_let = 0
        start_sym = 0

        for join in range(len(start_word)):
            if join in letter_index:
                end_word.append(new_word[start_let])
                start_let += 1
            else:
                end_word.append(symbol[start_sym])
                start_sym += 1

        final_result = "".join(end_word)
        print(f"Here's the {direction}d result : {final_result}")


os.system('cls')
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_word=text, direction=direction, shift=shift)
