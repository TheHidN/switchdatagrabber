from getpass import getpass
from netmiko import ConnectHandler
from openpyxl import Workbook
import time

username = input('login as: ')
password = getpass('Password: ')

commands = ['show mac address-table','show ip arp','show interface status',
        'show port-channel sum', 'show vpc | inc up']

def login(ip):
    
    session = ConnectHandler(host=ip,
                             port='22',
                             username=username,
                             password=password,
                             device_type='cisco_ios')

    workbook = Workbook()
    workbook.active
    
    for cmd in commands:
        worksheet = workbook.create_sheet(title=cmd.rstrip())
        output = session.send_command(cmd)
        output = output.splitlines()
        for i in range(0, len(output)):
            start_row = i + 1
            e = worksheet.cell(row=start_row, column=1)
            e.value = output[i]
    
    print(workbook.get_sheet_by_name('Sheet'))
    print(workbook.get_sheet_by_name('Sheet'))
    print(workbook.get_sheet_by_name('Sheet'))
    print(workbook.get_sheet_by_name('Sheet'))
    print(workbook.get_sheet_by_name('Sheet'))
    workbook.remove_sheet('<Worksheet "Sheet">')
    workbook.save(filename='test.xlsx')

    session.disconnect()

    print(output[0])

login('172.21.98.34')
