from ssh import login
from clear_counters import counters 
from nexus_commands import nexus_mac

while 1:    
    switchtype = input('What type of switch are you trying to connect to (Nexus/Catalyst)?: ')

    if switchtype == 'Nexus':
        session = login()
        patterns = session.expect(['Password', '>', '#'])

        if patterns == 0:
            print('wrong password aborting session')
            exit()
        elif patterns == 1:
            print('enable problem')
            exit()
        elif patterns == 2:
            print(f'Connected to {login.ip_address}')
            session.counters()
            break
    elif switchtype =='Catalyst':
        login()
        counters()
        break
    else:
        break 

