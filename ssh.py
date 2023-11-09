from getpass import getpass
from netmiko import ConnectHandler
import json
import time

username = input('login as: ')
password = getpass('Password: ')
devicetype = input('Type 1 for Nexus Switch, 2 for XE switch: ')

if devicetype == '1':
    devicetype = 'cisco_nxos'
elif devicetype == '2':
    devicetype = 'cisco_ios'
else:
    print('Enter a valid number')

creds = {
    'port': '22',
    'username': username,
    'password': password,
    'device_type': devicetype
}

nex_command = ['show mac address-table']
#nex_command = ['show mac address-table','show ip arp','show interface status',
      #  'show port-channel sum', 'show vpc | inc up']

ios_command = []

json_list = []

def login(ip):
    #connect to switch
    session = ConnectHandler(host=ip, **creds)
    
    #send command output as json to convert to excel.
    if devicetype =='cisco_nxos':
        
        for cmd in nex_command:
            output = session.send_command(cmd, use_textfsm=True)
            
            with open(f'{cmd}.json', 'w') as f:
                json.dump(output, f, indent=2)

    elif devicetype =='cisco_ios':
        for cmd in ios_commands:
            output = session.send_command(ios_commands, use_textfsm=True)
            pprint(output[0])

    session.disconnect()

login('172.21.98.34')
