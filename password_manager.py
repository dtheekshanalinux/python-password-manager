
from secret import login_key
from menu import menu, create, find, find_accounts
from getpass import getpass
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

secret = login_key()

passw = (getpass(prompt='provide the master password to start using dinindupwdmanager500: '))

if passw == secret:
    print('You\'re in')

else:
    print('no luck')
    exit() 

choice = menu()
while choice != 'q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
