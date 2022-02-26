
# create dictionary of 20 random values 1 to 99. Determine whether any duplicate
# values in dictionary. 

import random 
RandomValues = {} # dictionary declaration. 
 
for k in range(20):
  RandomValues[k] = random.randint(0,99)

uniqueElem = set() # only counts it once if there is a repeat. 
allElem = []
for elem in RandomValues:
  uniqueElem.add(elem)
  allElem.add(elem)

if len(uniqueElem) != len(allElem):
  print("Duplicates")
else:
  print("no duplicates")