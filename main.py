from ssh import login
from clear_counters import counters 
from nexus_commands import nexus_mac

while 1:    
    switchtype = input('What type of switch are you trying to connect to (Nexus/Catalyst)?: ')

    if switchtype == 'Nexus':
        login()
        counters()
        nexus_mac()
        break
    elif switchtype =='Catalyst':
        login()
        counters()
        break
    else:
        continue 


