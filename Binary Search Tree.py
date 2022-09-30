

nullpointer = -1
 #leftpointer, data, rightpointer
Arraynodes = [[i+1,0,-1] for i in range(20)]
Arraynodes[19][0] = -1 #SHOWS ITS LAST FREE NODE
freenode = 0
root = -1

def addnode( Arraynodes, rootP, freeP):

    newdata = int(input("input your data"))
    # return values byref
    if freeP <= 19 :
        Arraynodes[freeP][0] = -1
        Arraynodes[freeP][1] = newdata
        Arraynodes[freeP][2] = -1
        if rootP == nullpointer:
            rootP = 0
        else:
            placed = False
            currentnode = rootP
            while placed == False:
                if newdata < Arraynodes[currentnode][ 1]:
                    if Arraynodes[currentnode][0] == -1:
                        Arraynodes[currentnode][0] = freeP
                        placed = True
                    else:
                        currentnode = Arraynodes[currentnode][0]
                else:
                    if Arraynodes[currentnode][ 2] == -1:
                        Arraynodes[currentnode][2] = freeP
                        placed = True
                    else:
                        currentnode = Arraynodes[currentnode][2]
        freeP = freeP + 1
    else:
        print("tree is full")

    return Arraynodes, rootP, freeP



def printall ():
    for i in range(len(Arraynodes)):
        print(Arraynodes[i][0],Arraynodes[i][1], Arraynodes[i][2])


for i in range(10):
    Arraynodes, root, freenode = addnode(Arraynodes, root, freenode)
    print(Arraynodes)















