# Dictionary example to lookup phone from email

contacts = {'jsmith@mymail.com': '801-555-1223',
            'jdoe@mymail.com': '810-555-9887'}

print('Enter an email address to lookup phone, or <return> when done')
email = input('> ')
while email != '':
    if email in contacts: # check if the email is a key in dictionary
       phone = contacts[email] # if so, look up value from key
       print(phone)
    else:
       print('** not found **')
    email = input('> ')
