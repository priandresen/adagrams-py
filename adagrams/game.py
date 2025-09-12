from random import randint

def draw_letters():

    letter_available = {
                    1:  {'A': 9},
                    2:  {'B': 2},
                    3:  {'C': 2},
                    4:  {'D': 4},
                    5:  {'E': 12},
                    6:  {'F': 2},
                    7:  {'G': 3},
                    8:  {'H': 2},
                    9:  {'I': 9},
                    11: {'K': 1},
                    12: {'L': 4},
                    13: {'M': 2},
                    14: {'N': 6},
                    15: {'O': 8},
                    16: {'P': 2},
                    17: {'Q': 1},
                    18: {'R': 6},
                    19: {'S': 4},
                    20: {'T': 6},
                    21: {'U': 4},
                    22: {'V': 2},
                    23: {'W': 2},
                    24: {'X': 1},
                    25: {'Y': 2},
                    26: {'Z': 1}
    }

    hand = []
    #letter_available_copy = letter_available.copy()

    while len(hand) < 10:
        picked_letter = randint(1, len(letter_available))
        print(picked_letter)
        for num, inner_dict in letter_available.items():
            if num == picked_letter:
                for letter, num_available, in inner_dict.items():
                    if num_available != 0:
                        hand.append(letter)
                        inner_dict[letter] = num_available - 1

    return hand

def uses_available_letters(word, letter_bank):
    
    word_upper_case = word.upper()
    word_list = list(word_upper_case)

    word_dict = dict.fromkeys(word_list, 0)
    letter_bank_dict = dict.fromkeys(letter_bank, 0)

    for letter in word_list:
        if letter in word_dict:
                word_dict[letter] += 1
            

    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1

    print(word_dict)
    print(letter_bank_dict)

    for letter in word_dict:
        if word_dict.get(letter) > letter_bank_dict.get(letter, 0):
            return False
        
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

