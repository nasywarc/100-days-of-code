alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_word, shift, direction):
    letter = []
    symbol = []
    letter_index = []
    symbol_index = []
    end_word = []

    for pos in range(len(start_word)):
        if start_word[pos] in alphabet:
            letter_index.append(pos)
            letter.append(alphabet.index(start_word[pos]))
