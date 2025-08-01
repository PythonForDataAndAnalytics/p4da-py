# Simple text processor with slicing
text = ''

entry = input('> ')
while entry != '':
    command = entry[0]
    if   command == '+': text += entry[1:] # slice and concatenate
    elif command == '-': text = ''
    else:                text = entry
    print(text)
    entry = input('> ')
