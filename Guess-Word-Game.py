import random

def get_input():
    """this function return a correct word"""
    while True:
        user_input = input('enter your guess: ')
        if user_input.isalpha():
            return user_input.lower()
        print('your input was not correct. please enter again')

def get_input_from_list(words):
    user_input = get_input()

    while user_input not in words:
        print('you should guess a word from the given words list!')
        user_input = get_input()

    return user_input.lower()

def print_game_intro():
    print('-'* 15)
    print('hi, welcome to the guess game.')
    print('All words: ', list_of_words)
    print('start guessing')
    print("-"* 15)

def run_game(number_of_rounds, words):
    print_game_intro()
    print(f'number of guesses: {number_of_rounds}')
    correct_word = random.choice(words)
    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)
        if user_input == correct_word:
            print("YOU WON!")
            return
        else:
            print('you guessed wrong')
            print(f"please try again!  number of rounds left: {number_of_rounds-1-i}")
    print('YOU LOST!')
    
list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
run_game(5, list_of_words)
