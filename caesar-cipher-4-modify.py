alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    index_list = []
    new_word = []
    symbol_index = []
    symbol = []
    for letter in text:
        if letter in alphabet:
            index_list.append(alphabet.index(letter))
        else:
            symbol.append(letter)
            symbol_index.append(symbol.index(letter))
    for index in range(len(index_list)):
        if direction == 'encode':
            if index in index_list:
                index_list[index] += shift
            while index_list[index] > 25:
                index_list[index] -= 26
        elif direction == 'decode':
            if index in index_list:
                index_list[index] -= shift
            while index_list[index] < 0:
                index_list[index] += 26
        else:
            break
    for cipher in index_list:
        if cipher in alphabet:
            new_word.append((alphabet[cipher]))
        else:
            new_word.append((symbol_index[cipher]))
    if direction == 'encode':
        print("The encoded text is", "".join(new_word))
    elif direction == 'decode':
        print("The decoded text is", "".join(new_word))
    else:
        print("\nYour input is invalid.")


caesar(text=text, direction=direction, shift=shift)
