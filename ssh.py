from getpass import getpass

def login():
    import pexpect

    login.ip_address = input('What is the ip address you want to connect to: ')
    login.username = input('login as: ')
    login.password = getpass('Password: ')

    #establish SSH session with switch
    session = pexpect.spawn(f'ssh -o StrictHostKeyChecking=no {login.username}@{login.ip_address}')
    session.expect('Password')
    session.sendline(login.password)

    return session
