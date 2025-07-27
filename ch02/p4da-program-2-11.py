# String concatenation and some methods

message = 'Hi '
name = input('Please enter your name: ')
name = name.strip().capitalize()
message += name + '!'
print(message)
