# read a product file into a dictionary, keyed by product ID

# supporting function function to parse product file line
def parseProductLine(line):
    fields = line.split(',')
    return fields[0], fields[1], float(fields[2])

# supporting function to parse sales file line
def parseSalesLine(line):
    fields = line.split(',')
    return fields[0], fields[1], fields[2], int(fields[3])

# read product file into a dictionary of dictionaries
def readProductFile(filename):
   adict = {}
   fin = open('products.txt')
   fin.readline() # skip header
   for line in fin:
      line = line.rstrip('\n')
      id, div, price = parseProductLine(line)
      adict[id] = {'price': price, 'sales': 0} # add sub-dictionary
   fin.close()
   return adict

# read sales file, cumulating sales by product
def readSalesFile(filename, products):
   fin = open(filename)
   fin.readline() # skip header
   for line in fin:
      line = line.rstrip('\n')
      date, id, region, count = parseSalesLine(line)
      price = products[id]['price']
      products[id]['sales'] += price * count # cumulate sales
   fin.close()
   return products
    
products = readProductFile('products.txt')
readSalesFile('sales.txt', products)

# display results
for id in products.keys():
   print(id.ljust(6), format(products[id]['sales'], '8.2f'))
