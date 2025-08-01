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
        text = '' # reset to empty string
    elif command == '?':
        print(entry[1:] in text) # search
    elif command == '#':
        print(text.count(entry[1:])) # count
    else:
        text = entry

    if display:
       print(text)
    entry = input('> ')
