# read a file with product information and calculate their EOQ
# write the results to a file

# calculate an economic order quantity for given parameters
def calcEOQ(demand, orderCost, holdingCost):
    result = (2 * demand * orderCost / holdingCost) ** .5
    return result

# parse an input line into separate fields and convert to numeric type
def parseLine(line):
    fields = line.split(',')
    return fields[0], int(fields[1]), float(fields[2]), float(fields[3])

fin = open('eoq.txt', 'r')
fin.readline() # skip over the input file header line
i = 1 # counter for lines read

fout = open('eoqout.txt', 'w')
print('id', "eoq", file=fout, sep=',') # header line for output file
j = 1 # counter for lines written

for line in fin:
   line = line.rstrip('\n').strip()
   if line != '':
      fields = line.split(',')
      id, demand, orderCost, holdingCost = parseLine(line)
      eoq = calcEOQ(demand, orderCost, holdingCost)
      print(id, round(eoq,0), sep=',', file=fout)
      j += 1
   i += 1
print(i, 'lines read;', j, 'lines written')
fin.close()
fout.close()
