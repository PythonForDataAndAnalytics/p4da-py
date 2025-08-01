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
        text = ''
    elif command == '?':
        print(entry[1:] in text) # search
    elif command == '#':
        print(text.count(entry[1:])) # count
    elif command == '^':
        text = text.upper() # uppercase and reset
        display = True
    elif command == '/':
        fields = entry.split('/') # parse entry from string to list of strings
        if len(fields) == 3:
           text = text.replace(fields[1], fields[2]) # replace
           display = True
    else:
        text = entry

    if display:
       print(text)
    entry = input('> ')
