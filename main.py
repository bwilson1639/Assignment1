


class Node:

    def __init__(self, data, depth, cost):
        '''Initializes the node class and fills the node with required data'''

        self.data = data
        self.depth = depth
        self.cost = cost

    def createChild(self):
        '''creates all child nodes off of current node, returns list of possible nodes'''

        for place in self.data:
            if self.data[place] == 0:
                currentBlankPosition = place

        for y in range(0,3):
            for x in range (0,3):
                if self.data[y][x] == 0:
                    xValue = x
                    yValue = y

        possibleList = [[xValue,yValue-1], [xValue,yValue+1], [xValue-1,yValue],[xValue+1,yValue]]
        possibleChildren = []
        children = []

        '''checks to see what moves are possible'''
        for coordinate in possibleList:
            if coordinate[0] >= 0 and coordinate[0] < 4 and coordinate[1] >= 0 and coordinate[1] < 4:
                possibleChildren.append(coordinate)

        '''moves the data around based on the possible children then saves it in children list'''
        for childNode in possibleChildren:
            possibleChildData = possibleChildren.pop(0)
            tempHolder = self.data[possibleChildData[1]][possibleChildData[0]]
            childData = self.data
            childData[possibleChildData[1]][possibleChildData[0]] = 0
            childData[yValue][xValue] = tempHolder
            children.append(Node(childData,self.depth + 1, 0))

        return children




class puzzleSolver:

    def __init__(self):
        self.startingState = self.inputCollector()
        self.endingSolution = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.expandedNodes = []
        self.coveredNodes = []

    def inputCollector(self):
        """gets the user input for the starting state"""

        inputtedList = []

        print("Enter 9 numbers (including 0): (there should be a space between adjacent numbers")
        for inputs in range(0,3):
            temp = input().split(" ")
            inputtedList.append(temp)


        return inputtedList

    def costCalculate(self, start, goal):
        '''calculates g(n) + h(n)'''
        return self.manhattanHeuristic(start.data,goal) + start.depth

    def manhattanHeuristic(self, start, goal):
        '''the A* heuristic, calculates the estimated cost from n to goal'''

        temp = 0

        for y in range(0, 3):
            for x in range(0, 3):
                if start[y][x] != goal [y][x] and start[y][x] != 0:
                    temp += 1

        return temp

    def puzzleSolution(self):

        initialState = Node(self.startingState, 0, 0)
        initialState.cost = self.costCalculate(initialState,self.endingSolution)
        self.expandedNodes.append(initialState)

        while(True):
            consideredNode = self.expandedNodes.pop(0)

            for i in consideredNode.data:
               for j in i:
                   print(j,end=" ")
               print(" ")

            if(consideredNode.data == self.endingSolution):
                break

            for child in consideredNode.createChild():
                child.cost = self.costCalculate(child, self.endingSolution)
                self.expandedNodes.append(child)
                self.coveredNodes.append(consideredNode)

                self.expandedNodes.sort(key = lambda x:x.cost,reverse=False)








puz = puzzleSolver()
puz.puzzleSolution()