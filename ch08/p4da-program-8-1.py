# Simple text processor with assignment and concatenation
text = '' # initialize as empty string

entry = input('> ') # input() returns a string
while entry != '': # string compare
    command = entry[0] # character access
    if   command == '=': text = input('>> ')   # assignment
    elif command == '+': text += input('>> ')  # concatenation
    elif command == '-': text = ''             # reset to empty string

    print(text)
    entry = input('> ')
