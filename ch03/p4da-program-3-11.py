# Check Python ordering of strings  
string1 = input('Enter string 1: ')
string2 = input('Enter string 2: ')
if string1 == string2:
   print('The strings are equal')
elif string1 < string2:
   print(string1, 'is before',  string2)
else:
   print(string1, 'is after', string2)
