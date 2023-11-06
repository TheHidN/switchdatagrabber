from getpass import getpass
import pexpect

def login():
    ip_address = input('What is the ip address you want to connect to: ')
    username = input('login as: ')
    password = getpass('Password: ')

    #establish SSH session with switch
    session = pexpect.spawn(f'ssh -o StrictHostKeyChecking=no {username}@{ip_address}')
    session.expect('Password')
    session.sendline(password)

