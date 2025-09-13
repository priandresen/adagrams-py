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
                    10: {'J': 1},
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
    
    word_list = list(word.upper())

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
    score = 0
    word_list = list(word.upper())


    letter_value_dict = {
                        "A": 1,
                        'B': 3,
                        'C': 3,
                        'D': 2,
                        'E': 1,
                        'F': 4,
                        'G': 2,
                        'H': 4,
                        'I': 1,
                        'J': 8,
                        'K': 5,
                        'L': 1,
                        'M': 3,
                        'N': 1,
                        'O': 1,
                        'P': 3,
                        'Q': 10,
                        'R': 1,
                        'S': 1,
                        'T': 1,
                        'U': 1,
                        'V': 4,
                        'W': 4,
                        'X': 8,
                        'Y': 4,
                        'Z': 10                         
    }


    if len(word) == 0:
        score = 0
    elif len(word) >= 7:
        score += 8

    for letter in word_list:
        if letter in letter_value_dict:
            score += letter_value_dict.get(letter)




    return score 

def get_highest_word_score(word_list):

    best_word = word_list[0]
    best_score = score_word(word_list[0])
    winner = (best_word, best_score)

    for word in word_list:

        temp_best_word = word
        temp_best_score = score_word(word)
        if temp_best_score > best_score:
            best_score = temp_best_score
            best_word = word
        
        if temp_best_score == best_score:
            if len(temp_best_word) < len(best_word) and len(best_word) != 10:
                best_word = temp_best_word
                temp_best_score = score_word(temp_best_word)
            if len(temp_best_word) == 10:
                winner = (temp_best_word, temp_best_score)
                break

        
        winner = (best_word, best_score)


    return winner

