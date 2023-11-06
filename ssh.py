from getpass import getpass
import sys
import pexpect

def login():
    ip_address = input('What is the ip address you want to connect to: ')
    username = input('login as: ')
    password = getpass('Password: ')

    #establish SSH session with switch
    session = pexpect.spawn(f'ssh -o StrictHostKeyChecking=no {username}@{ip_address}')
    session.expect('Password')
    session.sendline(password)
    #post buffer to console 
    #session.logfile = sys.stdout.buffer

    patterns = session.expect(['Password', '>', '#'])

    if patterns == 0:
        print('wrong password aborting session')
        exit()
    elif patterns == 1:
        print('enable problem')
        exit()
    elif patterns == 2:
        print(f'Connected to {ip_address}')

    return session
