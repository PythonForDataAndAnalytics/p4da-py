# Dictionary example to display all keys and values

contacts = {'jsmith@mymail.com': '801-555-1223',
            'jdoe12@mymail.com': '801-555-9887'}

for email, phone in contacts.items():
    print(email, phone)

print(len(contacts), 'contacts in dictionary')
