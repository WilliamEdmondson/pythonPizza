# Single Line Parser of pizza toppings

toppingList = []

# Read from Pizza File.
p = open("linPizza.txt")

# Put the topping chars into an array.
next = p.read(1)
while next != "\n":
    toppingList.append(next)
    next = p.read(1)

print ("Pizza: " , toppingList)

# Slice the pizza
# Maximum number of slices with one of each topping
# In the linear example this is a slice each time the topping changes
# This can be done L->R or R->L both are attepted

# Simple comparason slicing method
def linearSlicer (toppingList):
    tlLength = len(toppingList)
    current = toppingList[0]
    sliceList = []
    currSlice = []
    for i in range(0, tlLength):
        topping = toppingList[i]
        if topping != '':
            currSlice.append(topping)
            if topping != current:
                current = toppingList[i]
                sliceList.append(currSlice)
                currSlice = []
    # Tuple of [no. of slices, leftovers]
    util = (tlLength - len(currSlice)) / tlLength
    return [toppingList,sliceList,currSlice,util]

# prints relevant lslicer information
def lSlicerPrint ( arr ):
    toppingList = arr[0]
    sliceList = arr[1]
    currSlice = arr[2]
    util = arr[3]
    print ("Pizza: " , toppingList)
    print ("Slice Breakdown: " , sliceList)
    print ("Leftovers: " , currSlice)
    print ("# of Slices: " , len(sliceList))
    print ("Pizza Utiliation: ", util * 100 , "%")
    return

# L->R
LR = linearSlicer (toppingList)
# print("------ Slicing L -> R -------")
# lSlicerPrint(LR)

# R->L
# Define a reverse list function
def revList (list):
    newlist = []
    for index in range(len(list) - 1, -1, -1):
         newlist.append(list[index])
    return newlist

toppingList = revList (toppingList)
# print ("Reverse Pizza: " , toppingList)

RL = linearSlicer (toppingList)
# print("------ Slicing R -> L -------")
#lSlicerPrint(RL)

# Imposing an additional constraint no more that 3 of one topping
# in each slice.
def troubleMidpoints (toppingList):
    troublePoints = []
    counter = 0
    currTopping = len(toppingList[0])
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


# split about trouble points
# TODO need to be adapted to more than one troubled point
def splitAboutTP0(toppinglist):
    troublePoints = troubleMidpoints(toppingList)
    pizzaSplitR = toppingList[:int(troublePoints[0])]
    pizzaSplitL = toppingList[int(troublePoints[0]):]
    return [pizzaSplitL, pizzaSplitR]

splitPizza = splitAboutTP0(toppingList)
pizzaSplitL = splitPizza[0]
pizzaSplitR = splitPizza[1]


print("Slice A: ",pizzaSplitL , " Slice B: " , pizzaSplitR)
leftSliced = linearSlicer (pizzaSplitL)
# lSlicerPrint(leftSliced)
rightSliced = linearSlicer (pizzaSplitR)
# lSlicerPrint(rightSliced)

# performs linearSlicer both ways and returns the one
# with highest optumisation.
def twoWaySlicer (toppingList):
    lSlicerArr = linearSlicer(toppingList)
    util1 = lSlicerArr[3]
    # optumisation if 1 then return
    toppingList = revList (toppingList)
    lSlicerArr = linearSlicer(toppingList)
    util2 = lSlicerArr[3]
    if ((util1 - util2) > 0):
        toppingList = revList (toppingList)
    return linearSlicer(toppingList)

lSlicedBw = twoWaySlicer(pizzaSplitL)
rSlicedBw = twoWaySlicer(pizzaSplitR)
# lSlicerPrint(lSlicedBw)
# lSlicerPrint(rSlicedBw)

# merges 2 lSlicers into 1 slicelist
# param splitPizzaA/B => [toppingList,sliceList,currSlice,util]
def mergeSliceLists( splitPizzaA, splitPizzaB ):
    toppingList = splitPizzaA[0] + splitPizzaB[0]
    sliceList = splitPizzaA[1] + splitPizzaB[1]
    currSlice = splitPizzaA[2] + splitPizzaB[2]
    util = (len(toppingList) - len(currSlice))/len(toppingList)
    return [toppingList,sliceList,currSlice,util]

mergedSlicedBw = mergeSliceLists(lSlicedBw,rSlicedBw)
lSlicerPrint(mergedSlicedBw)

# slicer with the contraint of max of one topping
# TODO add var max(eachTopping)
def constrainedSlicer(toppingList):
    troubleMidpoints(toppingList)
    return
