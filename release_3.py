# Forca Game - Developed in Python - Version 3

import random
from os import system, name

def clean_screen():
    
    if (name == 'nt'): # Windows
        _ = system('cls')
    else: # MacOS or Linux
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:
    
    def __init__(self, word):
        self.word = word
        self.error_letters = []
        self.choice_letters = []
    
    def guess(self, letter):
        
        if (letter in self.word and letter not in self.choice_letters):
            self.choice_letters.append(letter)
        
        elif (letter not in self.word and letter not in self.error_letters):
            self.error_letters.append(letter)
        
        else:
            return False
        
        return True

    def hagman_over(self):
        
        return self.hangman_won() or (len(self.error_letters) == 6)
    
    def hangman_won(self):
        
        if ('_' not in self.hide_word()):
            return True
        return False
    
    def hide_word(self):
        
        rtn = ''
        
        for letter in self.word:
            if letter not in self.choice_letters:
                rtn += '_'
            else:
                rtn += letter
        
        return rtn
    
    def print_game_status(self):
        
        print(board[len(self.error_letters)])
        
        print('\nWord: ' + self.hide_word())
        
        print('\nError Letters: ',)
        
        for letter in self.error_letters:
            print(letter,)
            
        print()
        
        print('Correct letters: ',)
        
        for letter in self.choice_letters:
            print(letter,)
        
        print()
        
def rand_word():
    
    words = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    word = random.choice(words)
    
    return word

def main():
    
    clean_screen()
    
    game = Hangman(rand_word())
    
    while not game.hagman_over():
        
        game.print_game_status()
        
        user_input = input('\nEnter a letter: ')
        
        game.guess(user_input)
        
    game.print_game_status()
    
    if game.hangman_won():
        print('\nCongratulations! You win!!!')
    
    else:
        print('\nGame over! You lose!!!')
        print('The word was ' + game.word)
    
    print('\nFoi bom jogar com você! Agora vá estudar!!!\n')
    
if __name__ == '__main__':
    main()
    
    