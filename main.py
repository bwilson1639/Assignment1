


class Node:

    def __init__(self, data, depth, cost):
        '''Initializes the node class and fills the node with required data'''

        self.data = data
        self.depth = depth
        self.cost = cost

    def createChild(self):
        '''creates all child nodes off of current node'''

        for place in self.data:
            if self.data[place] == 0:
                currentBlankPosition = place




class puzzleSolver:

    def __init__(self):
        self.startingState = self.inputCollector()
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

    def puzzleSolution(self):

        endingSolution = [[0,1,2], [3,4,5], [6,7,8]]




print(puzzleSolver().startingState)