alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = [' ', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    letter_index = []
    letter = []
    new_word = []
    symbol_index = []
    symbol = []
    let_char = []
    sym_char = []
    for char in text:
        if char in alphabet:
            letter.append(char)
            letter_index.append(alphabet.index(char))
            let_char.append(text.index(char))
        else:
            symbol.append(char)
            # symbol_index.append(text.index(char))
            sym_char.append(text.index(char))
    # print(letter_index)
    # print(symbol_index)
    # print(let_char)
    # print(sym_char)
    # print(symbol)
    # for join in range(len(text)):
    #     if direction == 'encode':
    #         for index in text :

    #     if join in letter_index:
    #         letter_index[index] += shift
    #     while letter_index[index] > 25:
    #         letter_index[index] -= 26
    # elif direction == 'decode':
    #     if index in letter_index:
    #         letter_index[index] -= shift
    #     while letter_index[index] < 0:
    #         letter_index[index] += 26
    #     else:
    #         break
    # for cipher in letter_index:
    #     if cipher in alphabet:
    #         new_word.append((alphabet[cipher]))
    #     else:
    #         new_word.append((symbol_index[cipher]))
    # if direction == 'encode':
    #     print("The encoded text is", "".join(new_word))
    # elif direction == 'decode':
    #     print("The decoded text is", "".join(new_word))
    # else:
    #     print("\nYour input is invalid.")


caesar(text=text, direction=direction, shift=shift)
