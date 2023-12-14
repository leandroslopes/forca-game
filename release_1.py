# Forca Game - Developed in Python - Version 1

import random
from os import system, name

def clean_screen():
    
    if (name == 'nt'): # Windows
        _ = system('cls')
    else: # MacOS or Linux
        _ = system('clear')

def game():
    
    clean_screen()
    
    print('\nWelcome to Forca Game!')
    print('Guess the word below:\n')
    
    words = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    word = random.choice(words)
    
    letters_discoveries = ['_' for letter in word]
    
    odds = 6
    
    letters_wrong = []
    
    while odds > 0:
        
        print(" ".join(letters_discoveries))
        print('\nRemaining chances: ', odds)
        print('Wrong letters: ', ''.join(letters_wrong))
        
        attempt = input('\nType a letter : ').lower()
        
        if attempt in word:
            index = 0
            
            for letter in word:
                if attempt == letter:
                    letters_discoveries[index] = letter
                index += 1
        else:
            odds -= 1
            letters_wrong.append(attempt)
            
        if '_' not in letters_discoveries:
            print('\nYou won, the word was: ', word)
            break
    
    if '_' in letters_discoveries:
        print('\nYou lost, the word was: ', word)

if __name__ == '__main__':
    game()
    