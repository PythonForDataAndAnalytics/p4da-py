# with for, read a file and echo its lines to the screen
# Add try/except in case file is not found

def echo(f):
   for line in f:
      line = line.rstrip('\n')
      print(line)

try:
   f = open('measures0.txt', 'r')
   echo(f)
   f.close()
except:
   print("File not found")
