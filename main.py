#!/usr/bin/python3

import sys, json

def is_possible(word: str, draw: list) -> bool:
    """
    Takes in a word and a draw, returns if the word can be made with characters of the draw
    """
    draw_copy = draw.copy()
    joker = True
    for letter in word:
        if letter in draw_copy:
            draw_copy.remove(letter)
        elif joker and '?' in draw_copy:
            joker = False
        else:
            return False
    return True


def get_score(word: str, letter_score: dict[str, int]) -> int:
    """
    Takes in a word and a dictionary (dict[str, int]) of score letter, returns the score of the word
    """
    word_score = 0
    for letter in word:
        if letter in letter_score:
            word_score += letter_score[letter]
    return word_score


if __name__ == "__main__":
    """
    usage: words.txt letter_score.json "the_draw"
    """
    words = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            words.append(line[:-1])
    with open(sys.argv[2], 'r') as f:
        letter_score = json.load(f)

    draw = list(sys.argv[3])
    max_score_word = max(words, key=lambda word : get_score(word, letter_score) if is_possible(word, draw) else 0)
    print(max_score_word)
