# contacts as a dictionary of dictionary records 

# establish a dictionary of dictionaries
contacts = {
    'jsmith@mymail.com':
      {'phone': '801-555-1223', 'last':'Smith', 'first':'John'},
    'jdoe12@mymail.com':
      {'phone': '801-555-1223', 'last':'Doe', 'first':'Jane'},      
}

# display the data as a table
for email, data in contacts.items():
    print(email, data['first'], data['last'], sep='\t')
