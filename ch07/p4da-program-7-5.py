# read a file with product information and calculate their EOQ

# calculate an economic order quantity for given parameters
def calcEOQ(demand, orderCost, holdingCost):
    result = (2 * demand * orderCost / holdingCost) ** .5
    return result

f = open('eoq.txt', 'r')
f.readline() # skip over the file's header line
for line in f:
   line = line.rstrip('\n').strip()
   if line != '': # skip over lines with no data
      fields = line.split(',')
      id = fields[0]
      demand = int(fields[1])
      orderCost = float(fields[2])
      holdingCost = float(fields[3])
      print("product fields:", id, demand, orderCost, holdingCost)
      eoq = calcEOQ(demand, orderCost, holdingCost)
      print("EOQ for", id+":", round(eoq,0))
f.close()
