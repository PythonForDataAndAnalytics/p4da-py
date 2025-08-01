# Number entry with checking'
entry = input('Enter a number: ')
try:
   value = float(entry)
   print(value)
except:
   print('Error converting entry to number')
print("Program ends")
