# read a file with product information and calculate their EOQ

# calculate an economic order quantity for given parameters
def calcEOQ(demand, orderCost, holdingCost):
    result = (2 * demand * orderCost / holdingCost) ** .5
    return result

# parse an input line into separate fields and convert to numeric type
def parseLine(line):
    fields = line.split(',')
    return fields[0], int(fields[1]), float(fields[2]), float(fields[3])

f = open('eoq.txt', 'r')
f.readline() # skip over the header line
for line in f:
   line = line.rstrip('\n').strip()
   if line != '':
      fields = line.split(',')
      id, demand, orderCost, holdingCost = parseLine(line)
      print("product fields:", id, demand, orderCost, holdingCost)
      eoq = calcEOQ(demand, orderCost, holdingCost)
      print("EOQ for", id+":", round(eoq,0))
f.close()
