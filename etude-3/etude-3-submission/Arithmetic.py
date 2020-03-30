import sys
import time
import traceback

class Arithmetic:

    def __init__(self, nums, target, order):
        super(Arithmetic, self).__init__()
        self.nums = nums # The array of input numbers
        self.depth = len(nums) # Depth of the (abstract) binary tree, or n.
        self.target = target # The target value.
        self.found = False # Boolean for if the target value is found.
        self.finalString = "Impossible - currentValues exceed target" # The working expression, or 'Impossible.'
        self.opsPermutations = [] # A 2D array of every possible sequence of operations.
        self.order = order # Left to right, or Normal order of operations
        self.operations = "+*"

    # Addition utility function
    def add(self, x, y):
        return x + y

    # Multiplication utility function
    def multiply(self, x, y):
        return x * y

    # calculate assumes an binary tree abstraction for evaluating permutations of operation sequences.
    def calculate(self, i, ops, currentValue):

        if self.found:
            return
            # If the function is in a max depth state (is at the end of the expression)
        elif (i == self.depth):

            possiblePermutation = []

            # Append the operation sequence as an array to the 2D array containing all permutations of operation sequences.
            for j in range(len(ops)):
                possiblePermutation.append(ops[j])
            self.opsPermutations.append(possiblePermutation)

            # Add the first number to expressionString
            expressionString = str(self.nums[0])

            # Create the expressionString which is a possible soultion to achieve the target value
            for j in range(self.depth - 1):
                expressionString = expressionString + " " + possiblePermutation[j] + " "
                expressionString = expressionString + str(self.nums[j + 1])

            # result is the accumulated value if left to right order, or it is the normal evaluation of the entire expression.
            result = currentValue if self.order == 'L' else eval(expressionString)

            # If the target is achieved by the permutation
            if result == self.target:
                self.found = True
                self.finalString = expressionString
                return
            # target is not achieved and all permutations have been evaluated
            elif (not self.found) and len(self.opsPermutations) >= 2**(self.depth - 1):
                self.finalString = "Impossible"
                return
        elif currentValue >= self.target:
            return
        else:
            self.calculate(i + 1, ops + "+", self.add(currentValue, self.nums[i]))
            self.calculate(i + 1, ops + "*", self.multiply(currentValue, self.nums[i]))


    def calcIterative(self):


        currentValue = str(self.nums[0])
        i = 1

        while i < self.depth:
            for k in range(2):
                for j in self.operations:
                    currentValue = currentValue + j + str(self.nums[i])
                    print("Current value: ", currentValue)
                    result = eval(currentValue)
                    print(result)
            i = i + 1


        #while not self.found:

    def dfsLeft(self):

        possible = []
        i = 0
        toVisit = [self.nums[i]]
        n = 1

        while len(toVisit) > 0 and not self.found:

            perms = 2**(n-1)
            if i < self.depth - 1:
                #print("i = ", i)
                for k in range(perms):
                    try:
                        currentNode = toVisit.pop()
                    except IndexError:
                        print('Nothing to pop')
                        break
                    #print("Popped:", currentNode)
                    for j in self.operations:
                        if j == '+':
                            left = str(currentNode) + j + str(self.nums[i + 1])
                            leftValue = eval(left)
                            #print("Left", left,  "=", leftValue)
                            #toVisit.append(leftValue)
                            if leftValue <= self.target:
                                if i + 1 == self.depth - 1 and leftValue == self.target:
                                    print("TARGET FOUND", leftValue)
                                    self.found = True
                                    break
                                #print("Left value", leftValue, "Add to stack")
                                toVisit.insert(0, leftValue)
                        elif j == '*':
                            right = str(currentNode) + j + str(self.nums[i + 1])
                            rightValue = eval(right)
                            #print("Right", right,  "=", rightValue)
                            #toVisit.append(rightValue)
                            if rightValue <= self.target:
                                if i + 1 == self.depth - 1 and rightValue == self.target:
                                    print("TARGET FOUND", rightValue)
                                    self.found = True
                                    break
                                #print("Right value", rightValue, "Add to stack")
                                toVisit.insert(0, rightValue)

                    if self.found:
                        break

                        #currentValue = eval(str(currentValue) + j + str(self.nums[i + 1]))
                        #toVisit.insert(0, j + str(self.nums[i + 1]))
                    #print("Stack:", toVisit)
                i = i + 1
                n = n + 1
            else:
                #change this to just find the target using .index()
                '''
                try:
                    toVisit.index(self.target)
                    print("Found target")
                    break
                except ValueError:
                    print("Not found")
                    break
                '''

                try:
                    currentNode = toVisit.pop()
                except IndexError:
                    print('Nothing to pop: Impossible')
                    break
                #print("Popped:", currentNode)
                possible.append(currentNode)

        if possible:
            print("Possible: ", possible)
            for x in possible:
                if x == self.target:
                    self.found = True
                    print("Found target: ", x)
                    break



def main():

    count = 0 # Tracks whether a line is even or odd
    numSequence = [] # List of integers

    for line in sys.stdin:
        # First line of input
        if count % 2 == 0:
            for numberString in line.strip().split(" "): # Get strip and split the input into an array
                # Exception: Line of numbers contains at least one non-integer
                if not numberString.isdigit():
                    print("Error: First line of input must contain only digits separated by spaces")
                    return
                numSequence.append(int(numberString)) #numSequence is now the list of integers
        # Second line of input.
        else:
            constraints = line.strip().split(" ") # Get strip and split the input into an array.
            # Error: Not 2 arguments in second line of input, or target value is not an integer.
            if len(constraints) != 2 or not constraints[0].isdigit():
                print("Error: Second line of input must be an integer target value, followed by either 'L' or 'N'")
                return

            target = int(constraints[0]) # Target is the first input on the second line cast to an int
            order = constraints[1].capitalize() # Either 'L' or 'N'
            myArithmetic = Arithmetic(numSequence, target, order) # Create the class instance from the input

            # Error: Order is not L or N
            if (order != 'L' and order != 'N'):
                print('Invalid input for order')
                print(order)
                return
            else:
                #start = time.time()
                #myArithmetic.calculate(1, "", numSequence[0])
                #end = time.time()
                #print(order, myArithmetic.target, myArithmetic.finalString)
                #print("Iterative: ", myArithmetic.calcIterative())
                print(myArithmetic.nums, myArithmetic.target)
                start = time.time()
                myArithmetic.dfsLeft()
                end = time.time()
                print("Time elapsed", (end - start))
                print()


            numSequence = [] # reset the array for the next input

        count +=1 # increment for even/odd lines


if __name__ == "__main__":
    main()
