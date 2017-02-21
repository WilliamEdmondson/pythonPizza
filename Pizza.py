# Single Line Parser of pizza toppings

toppingList = []

# Read from Pizza File.
p = open("linPizza.txt")

# Put the topping chars into an array.
next = p.read(1)
while next != "\n":
    toppingList.append(next)
    next = p.read(1)

# Slice the pizza
# Maximum number of slices with one of each topping
# In the linear example this is a slice each time the topping changes
# This can be done L->R or R->L both are attepted

def linearSlicer (toppingList):
    tlLength = len(toppingList)
    current = toppingList[0]
    sliceList = []
    currSlice = []
    for i in range(0,tlLength-1):
        topping = toppingList[i]
        if topping != '':
            if topping == current:
                currSlice.append(topping)
            else:
                current = toppingList[i+1]
                currSlice.append(topping)
                sliceList.append(currSlice)
                currSlice = []
    # Print the relavent information
    print ("Pizza: " , toppingList)
    print ("Slice Breakdown: " , sliceList)
    print ("Leftovers: " , currSlice)
    print ("# of Slices: " , len(sliceList))
    print ("Pizza Utiliation: ", ((tlLength - len(currSlice)) / tlLength) * 100 , "%")
    # Tuple of [no. of slices, leftovers]
    return [len(sliceList),len(currSlice)]

# L->R
print("------ Slicing L -> R -------")
linearSlicer (toppingList)

# R->L
# Define a reverse list function
def revList (list):
    newlist = []
    for index in range(len(list) - 1, -1, -1):
         newlist.append(list[index])
    return newlist

toppingList = revList (toppingList)
print ("Reverse Pizza: " , toppingList)

print("------ Slicing R -> L -------")
linearSlicer (toppingList)

# Imposing an additional constraint no more that 3 of one topping
# in each slice.
def troubleMidpoints (toppingList):
    troublePoints = []
    counter = 0
    currTopping = toppingList[0]
    for i in range(0, len(toppingList)):
        topping = toppingList[i]
        if(currTopping == topping):
            counter += 1
        else:
            if counter > 3:
                troublePoints.append(i - (counter / 2))
            currTopping = toppingList[i]
            counter = 1
    if counter > 3:
        troublePoints.append(i - (counter / 2))
    return troublePoints

# Turning the pizza 180degrees yet again
toppingList = revList (toppingList)
print ("Pizza: " , toppingList)
troublePoints = troubleMidpoints(toppingList)

pizzaSplitR = toppingList[:int(troublePoints[0])]
pizzaSplitL = toppingList[int(troublePoints[0]):]

print("Slice A: ",pizzaSplitL , " Slice B: " , pizzaSplitR)
linearSlicer (pizzaSplitL)
linearSlicer (pizzaSplitR)
