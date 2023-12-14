# Forca Game - Developed in Python - Version 2

import random
from os import system, name

def clean_screen():
    
    if (name == 'nt'): # Windows
        _ = system('cls')
    else: # MacOS or Linux
        _ = system('clear')

def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():
    
    clean_screen()
    
    print('\nWelcome to Forca Game!')
    print('Guess the word below:\n')
    
    words = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    word = random.choice(words)
    
    list_letters_words = [letter for letter in word]
    
    tabuleiro = ['_'] * len(word)
    
    odds = 6
    
    letters_attempties = []
    
    while odds > 0:
        
        print(display_hangman(odds))
        print('Word: ', tabuleiro)
        print('\n')
        
        attempt = input('\nType a letter : ').lower()
        
        if attempt in letters_attempties:
            print('You\'ve already tried this letter. Choose another!')
            continue
        
        letters_attempties.append(attempt)
        
        if attempt in list_letters_words:
            
            print('You got the letter right!')
            
            for index in range(len(list_letters_words)):                
                if list_letters_words[index] == attempt:
                    tabuleiro[index] = attempt
            
            if '_' not in tabuleiro:
                print('\nYou won! The word was {}'.format(word))
                break            
        else:
            print('\nOops. That letter isn\'t in the word!')
            odds -= 1
            
    if '_' in tabuleiro:
        print('\nYou lost, the word was: {}'.format(word))

if __name__ == '__main__':
    game()
    