# Simple text processor to demonstrate some string features
text = ''

entry = input('> ')
while entry != '':
    display = False
    command = entry[0]
    if   command == '+':
        text += entry[1:] # slice and concatenate
        display = True
    elif command == '-':
        text = '' # empty string
    elif command == '?':
        print(entry[1:] in text) # search
    elif command == '#':
        print(text.count(entry[1:])) # count
    elif command == '^':
        text = text.upper() # upper case with reassignment
        display = True
    elif command == '/':
        fields = entry.split('/') # split string into list of strings
        if len(fields) == 3:
           text = text.replace(fields[1], fields[2]) # replace
           display = True
    elif command.isalpha() or command == ' ' :
        text = entry
    else:
        print('Unknown command')

    if display:
       print(text)
    entry = input('> ')
