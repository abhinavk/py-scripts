# Chat with Hodor
# Note: Windows has certain problems with this coz Windows!

import re
import time
import random


def response(user):
    '''Formulates a response from Hodor'''
    if re.search(r'([wW]inter)', user) or random.randint(0, 100) is 7:
        return 'Winter is coming. Hodor!'
    hodor_speak = ['... ', 'Hodor ' * random.randrange(0, 24, 2)]
    if re.search(r'[\?\!]', user) is not None or random.choice([0, 1]) is 1:
        hodor_speak.append('huh huh? ')
    hodor_speak.append('Hodor ' * random.randrange(4, 20, 2))
    hodor_speak.append('...')
    return ''.join(hodor_speak)


def main():
    '''Main function. Yeah!'''
    print('Hodor is online...\nYou can say \'Hi\'.')
    user_input = ''
    random.seed()   # Seed with system time
    while(str.lower(user_input) != 'bye'):
        print('You: ', end='')
        user_input = input()
        # \r doesn't work on Windows command line. Neither does ncurses. :(
        print('Hodor is thinking...', end='\r')
        user_length = len(user_input)
        if user_length > 100:
            time.sleep(20)
            print('You confused him with so many words. Please try again.')
            break
        else:
            time.sleep(user_length/5)
        print('Hodor is typing...  ', end='\r')
        hodor_speak = response(user_input)
        time.sleep(len(hodor_speak)/50)
        # Clear the last line in case of a short response
        print(' '*20, end='\r')
        print('Hodor says: ' + hodor_speak)
    else:
        print("Hodor. :'(")

if __name__ == '__main__':
    main()
