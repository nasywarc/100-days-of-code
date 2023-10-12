alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_word, shift, direction):
    letter = []
    symbol = []
    letter_index = []
    symbol_index = []
    new_index = []
    new_word = []

    for pos in range(len(start_word)):
        if start_word[pos] in alphabet:
            letter_index.append(pos)
            letter.append(alphabet.index(start_word[pos]))
        else:
            symbol_index.append(pos)
            symbol.append(start_word[pos])
    if direction == 'decode':
        shift *= -1
    for index in letter:
        new_index.append(index + shift)

    print(letter)
    print(letter_index)
    print(new_index)
    print(symbol)
    print(symbol_index)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_word=text, direction=direction, shift=shift)
