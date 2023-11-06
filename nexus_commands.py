def nexus_mac():
    from ssh import login
    session = login()
    session.expect('#')
    mac_address_table = session.sendline('show mac address-table')
