def counters():

    while 1:
        counters = input('Do you want to clear counters? (y/n)?: ').lower()
        
        if counters == 'y':
            session = login()
            session.expect('#')
            session.sendline('clear counters interface all')
            print('Counters cleared')
            break
        elif counters == 'n':
            print('Clear counters skipped')
            break
        else:
            print('Invalid answer')
            continue
