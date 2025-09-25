#!/usr/bin/python3
import itertools
import sys

def anagram_solver(letters,display_number):
    # Load a small sample dictionary for demonstration purposes
    with open('words_alpha.txt', 'r') as file:
        dictionary = set(word.strip().lower() for word in file)

    def find_anagrams(letters, dictionary):
        letters_lower = letters.lower()
        max_length = len(letters)
        anagrams = []
        
        # Generate all possible combinations of the input letters
        for length in range(1, max_length + 1):
            for combo in itertools.permutations(letters_lower, length):
                word = ''.join(combo)
                if word in dictionary:
                    anagrams.append(word)
        
        # Sort the words by length (from longest to shortest)
        sorted_anagrams = sorted(set(anagrams), key=len, reverse=True)
        printed_anagrams = sorted_anagrams[:display_number] # Set printed word number to what the user enters or default to 10.
        return printed_anagrams # Return word list to be printed

    # Example usage
    anagrams = find_anagrams(letters, dictionary)
    return anagrams

def alpha_check(letters):
    letters = str(letters).strip(' ')
    letters_only = letters.isalpha() and len(letters) > 0
    if letters_only == True:
        return letters
    else:
        print(f'Input contains invalid characters:{letters}\n')
        sys.exit(1)

def __main__():
    if len(sys.argv) > 1:
        user_input=sys.argv[1]
    else:
        user_input=input('Please enter your letters below:\n')
    if len(user_input) < 1:
        print('Must provide letters for the anagram solver.\n')
        sys.exit(1)
    if len(sys.argv) > 2:
        display_number=int(sys.argv[2])
    else:
        display_number=10
    letters=alpha_check(user_input)
    anagrams=anagram_solver(letters,display_number)
    for word in anagrams:
        print(word)

if __name__ == '__main__':
    __main__()
