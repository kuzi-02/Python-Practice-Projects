
class treasurechest:
    def __init__(self, question, answer, points):
        self.__question = question #stored as string
        self.__points = points #stored as integer
        self.__answer = answer #stored as integer

    def getqstn(self):
        return self.__question

    def checkanswer(self, answer):
        if answer == int(self.__answer):
            return True
        else:
            return False

    def getpoints(self, nattempts):
        if nattempts == 1:
           return self.__points
        elif nattempts == 2:
            return int(self.__points)//2
        elif nattempts == 3 or nattempts == 4:
            return int(self.points)//4
        else:
            return 0
arTreasure = []
def readdata():
        try:
            file = open("TreasureCD.txt", "r")
            detached = file.readline().strip()
            while detached != "":
                question = detached
                answer = file.readline().strip()
                points = file.readline().strip()
                arTreasure.append(treasurechest(question, answer, points))
                detached = file.readline().strip()
        except FileNotFoundError:
            print("File not found")

readdata()
qn = int(input("Enter question number"))
flag = False
count = 0
for i in range(len(arTreasure)):
    while flag == False:
         if i == qn:
            print(arTreasure[i][0])
            answer = int(input("Anser is:"))
            if treasurechest.checkanswer(treasurechest, answer) == True:
                flag = True
            else:
                flag = False
                count += 1

print(treasurechest.getpoints(treasurechest, count))





















