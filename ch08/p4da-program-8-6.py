# search for matching products from a file of price data

# read a file of price data into a list of lists
def loadProductData():
   fin = open("products.txt", 'r')
   productData = [ ]
   fin.readline() # read and skip header line
   for line in fin: # read each subsequent line
      line = line.rstrip('\n') # remove trailing newline
      if line[0] != '#' and line.count(',') == 2:
         productID, division, price = line.split(',')
         # add sublist to list
         productData.append((productID, division, price))
   return productData

# get user interest for product of interest
def getProductFilter():
   productFilter = input("Enter product ID (starts with): ")
   productFilter = productFilter.strip().lower() # adjust entry for matching
   return productFilter

# load product prices into a list of lists
productData = loadProductData()

# based on user's request, display matching product data
productFilter = getProductFilter()
while productFilter != 'quit':
    for productRecord in productData:
       if productRecord[0].lower().startswith(productFilter): # check for match
          print(productRecord[0], productRecord[1], productRecord[2], sep='\t')
    productFilter = getProductFilter()
