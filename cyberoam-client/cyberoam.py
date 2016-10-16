# Cyberoam.py
# A login interface written in Python for the Cyberoam firewall system
# copyright Abhinav Kumar me@abhinavk.me

import urllib.request
import urllib.parse
import time
import sys
import xml.etree.ElementTree

data = {'cyberoam_server': 'http://172.16.73.12:8090'}
logged_in = False


def setcyberoamserver(srvr):
    data['cyberoam_server'] = srvr
    print('New server set: ' + data['setcyberoamserver'], end=' ')
    return


def login(usr='', pwd='', keep_alive=1, display_logs=1):
    '''
    Logins to the specified Cyberoam server with username and password passed
    as parameters. A third parameter keep_alive has default value 1 to prevent
    Cyberoam client from logging you off. Pass 0 as third parameter to block
    this behavior
    '''
    data['username'] = usr
    data['password'] = pwd
    param = {'mode': '191', 'username': data['username'],
             'password': data['password'],
             'a': str(int(time.time()*1000))}
    param = urllib.parse.urlencode(param)
    param = param.encode('utf-8')
    req = urllib.request.Request(data['cyberoam_server'] + '/login.xml', param)
    res = urllib.request.urlopen(req, timeout=1)
    markup = res.read()
    res.close()
    request_info = xml.etree.ElementTree.fromstring(markup)
    status, msg = request_info[0].text, request_info[1].text
    if status.lower() == 'live':
        if display_logs:
            print('You have successfully logged in...(Ctrl+C to logout)\n')
        while(keep_alive):
            time.sleep(179.5)
            keep_alive()
        return True
    else:
        if display_logs:
            print(status + msg, end='\n')
        return False


def keep_alive():
    '''
    Polls the server every 3 minutes to acknowledge
    '''
    param = {'mode': '192', 'username': data['username'],
             'password': data['password'],
             'a': str(int(time.time()*1000))}
    param = urllib.parse.urlencode(param)
    param = param.encode('utf-8')
    req = urllib.request.Request(data['cyberoam_server'] + '/live?', param)
    res = urllib.request.urlopen(req, timeout=1)
    markup = res.read()
    res.close()
    request_info = xml.etree.ElementTree.fromstring(markup)
    status, msg = request_info[0].text, request_info[1].text
    if status.lower() == 'ack':
        print('Connection acknowledged...')
    else:
        print('Error' + msg)


def logout(usr):
    '''
    Logs out the specified username passed as only parameter
    '''
    data['username'] = usr
    if logged_in is True:
        param = {'mode': '193', 'username': data['username'],
                 'a': str(int(time.time()*1000))}
        param = urllib.parse.urlencode(param)
        param = param.encode('utf-8')
        req = urllib.request.Request(data['cyberoam_server'] + '/logout.xml',
                                     param)
        res = urllib.request.urlopen(req, timeout=1)
        markup = res.read()
        res.close()
        request_info = xml.etree.ElementTree.fromstring(markup)
        msg = request_info[1].text
        print(msg)
        return True
    else:
        print('You are already logged off.')
        return False


if __name__ == '__main__':
    if 3 < len(sys.argv) < 6:
        # if len(sys.argv) == 5:
        #     setcyberoamserver(sys.argv[4])
        if(sys.argv[1] == 'login'):
            login(sys.argv[2], sys.argv[3])
        else:
            print('Wrong syntax')
    else:
        print('Invalid number of arguments. Quitting...')
