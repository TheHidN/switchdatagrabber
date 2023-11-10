from getpass import getpass
import json
from netmiko import ConnectHandler
import os
import openpyxl
import pandas as pd

username = input('login as: ')
password = getpass('Password: ')
device_type = input('Type 1 for IOS, 2 for Nexus: ')

if device_type == '1':
    devicetype = 'cisco_ios'
elif device_type == '2':
    devicetype = 'cisco_nxos'
else:
    print('Enter a valid number')

creds = {
    'port': '22',
    'username': username,
    'password': password,
    'device_type': devicetype
}

ios_command = [
    'show clock',
    'show ver',
    'show mac address-table',
    'show ip arp',
    'show interface status',
    'show cdp neighbors',
    'sh ip int br',
    'sh ip int br | inc up',
    'sh ip int br | inc down',
    'sh ip int br | inc admin'
]

nex_command = ['show mac address-table',
               'show ip arp',
               'show interface status',
               'show port-channel sum',
               'show vpc | inc up'
]

def login(ip):
    #connect to switch
    session = ConnectHandler(host=ip, **creds)

    #get hostname
    hostname = session.find_prompt()[:-1]

    #create excel
    wb = openpyxl.Workbook()
    wb.save(hostname + ".xlsx")

    #send command output as json to convert to excel.
    if devicetype =='cisco_ios':
        for cmd in ios_command:

            with pd.ExcelWriter(hostname +".xlsx", engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                output = session.send_command(cmd, use_textfsm=True)
                router_output = json.dumps(output, indent=4)
                convert_json = json.loads(router_output)
                try:
                    df = pd.json_normalize(convert_json)
                    print(f'Grabbing configs from: {hostname}, {ip} Command: {cmd}')
                    df.to_excel(writer, sheet_name=(cmd), index=False)
                except:
                    print(f'Unable to grab: {hostname}, {ip} Command: {cmd}')
                    with open ('error.txt', 'a') as e:
                        e.write(f'Unable to grab: {hostname}, {ip} Command: {cmd}')

    elif devicetype =='cisco_nxos':
        for cmd in nex_command:

            with pd.ExcelWriter(hostname +".xlsx", engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                output = session.send_command(cmd, use_textfsm=True)
                router_output = json.dumps(output, indent=4)
                convert_json = json.loads(router_output)
                try:
                    df = pd.json_normalize(convert_json)
                    print(f'Grabbing configs from: {hostname}, {ip} Command: {cmd}')
                    df.to_excel(writer, sheet_name=(cmd), index=False)
                except:
                    print(f'Unable to grab: {hostname}, {ip} Command: {cmd}')
                    with open ('error.txt', 'a') as e:
                        e.write(f'Unable to grab: {hostname}, {ip} Command: {cmd}')

    wb = openpyxl.load_workbook(hostname +".xlsx")
    del wb['Sheet']
    wb.save(hostname +".xlsx")

    session.disconnect()

with open('ip.txt', 'r') as ip_list:
    for ip in ip_list:
        login(ip)

