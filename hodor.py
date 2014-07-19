# Chat with Hodor
# Note: Windows has certain problems with this coz Windows!

import hashlib
import re
import time
import random


def response(user):
    '''Formulates a response from Hodor randomly'''
    md5h = hashlib.md5(user)
    question_flag = False
    hodor_speak = '...'
    if re.search('(?)', user) is not None:
        question_flag = True
    return hodor_speak


def main():
    '''Main function. Yeah!'''
    print('Hodor is online...\nYou can say \'Hi\'.')
    user_input = None
    random.seed()   # Seed with system time
    while(str.lower(user_input) != 'bye'):
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
        time.sleep(len(user_input)/5)
        # Clear the last line in case of a short response
        print(' '*20, end='\r')
        print('Hodor says: ' + hodor_speak)
    else:
        print("Hodor. :'(")

if __name__ == '__main__':
    main()
