import random
import string
import os

settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
}

def clear_screen():
    os.system('cls')

def get_user_password_length(option, default, pw_min_length=4, pw_max_length=30):
    # pw : password
    while True:
        user_input  = input('Enter password length . '
                            f'(default is {default}) (Enter : default) : ')
        if user_input == '':
            return default
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length <= pw_max_length:
                return int(user_input)
            print('Invalid input.')
            print('password length shoould be '
                f'between {pw_min_length} and {pw_max_length} ')
        else:
            print('Invalid input. you should enter a number. ')
            
        print('please try again')


def get_yes_or_no_for_setting(option, default):
    while True:
        user_input = input(f'include {option} ? '
                            f' (default is {default} ) (y: yes, n: no): ')

        if user_input == "":
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input. please try again.')

def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_setting(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length

def ask_if_change_settings(settings):
    while True:
        user_answer = input('Do you wan to change default settings ? (y: yes,  n: no,  enter: yes): ')
        
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                get_setting_from_user(settings)
            break
        else:
            print('Invalid input')
            print('please try again')


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_number():
    return random.choice(string.digits)

def get_random_symbol():
    return random.choice(string.punctuation)


def generate_rand_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '

def password_generator(settings):

    final_password = ''
    password_length = settings['length']
    
    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'symbol', 'number', 'space']))

    for i in range(password_length):
        final_password += generate_rand_char(choices)
    return final_password

def try_again():
    user_need = input('do you like this password ? ( y: finish, n: get another password ): ')

def ask_user_to_generate_another_password():
    user_answer = input('Do you want another password? (y: yes, n: no, enter: yes ): ')

    if user_answer in ['y', 'n', '']:
        if user_answer == 'n':
            return False
        return True
    else:
        print('Invalid input')
        print('please try again')



def password_generator_loop():
        while True:
            print('-'*62)
            print(f'The Generated Password: {password_generator(settings)}')

            if ask_user_to_generate_another_password() == False:
                break

def run():
    clear_screen()
    ask_if_change_settings(settings)
    password_generator_loop()
    print('Thank you for choosing us!')

run()