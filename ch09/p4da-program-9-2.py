# Dictionary example to lookup phone (value) from email (key)

# create the dictionary
contacts = {'jsmith@mymail.com': '801-555-1223',
            'jdoe@mymail.com': '801-555-9887'}

print('Enter an email address to lookup phone (or <return> when done)')
email = input('> ')
while email != '':
    phone = contacts[email] # use email as key to lookup phone
    print(phone)
    email = input('> ')
