# build a contact set dynamically from user input

aset = set() # create an empty set

print('Enter email at > prompt (or <return> when done)')
entry = input('> ')
while entry != '':
   if entry[0] == '-': # a leading - indicates remove
      item = entry[1:].strip()
      if item in aset:
         aset.remove(item)
      else:
         print('** error, entry not found in set')
   else:
      aset.add(entry) # add entry to set (if not already in)
   print(aset)
   entry = input('> ')
