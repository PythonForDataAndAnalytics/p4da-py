# build a contact dictionary dynamically from user input

contacts = {} # create an empty dictionary

print('Enter email and phone # at > prompt (<return> when done)')
entry = input('> ')
while entry != '':
    email, phone = entry.split()
    contacts[email] = phone # add entry to dictionary
    print(contacts)
    entry = input('> ')
