import sys

class Line:
    """docstring for Line"""

    def __init__(self, nums, target):
        super(Line, self).__init__()
        self.nums = nums # The array of input numbers
        self.depth = len(nums) # Depth of the (abstract) binary tree, or n.
        self.target = target # The target value.
        self.found = False # Boolean for if the target value is found.
        self.finalString = "" # The working expression, or 'Impossible.'
        self.opsPermutations = [] # A 2D array of every possible sequence of operations.

    # Addition utility function
    def add(self, x, y):
        return x + y

    # Multiplication utility function
    def multiply(self, x, y):
        return x * y

# Both order functions use the abstraction of a binary tree.

    def normalOrder(self, i, ops):

        if self.found:
            return

        if (i == self.depth):

            tempArray = []

            for j in range(len(ops)):
                tempArray.append(ops[j])
            self.opsPermutations.append(tempArray)

            expressionString = str(self.nums[0])

            for j in range(self.depth - 1):
                expressionString = expressionString + " " + tempArray[j] + " "
                expressionString = expressionString + str(self.nums[j + 1])

            result = eval(expressionString)

            if result == self.target:
                self.found = True
                self.finalString = expressionString
                return
            elif (not self.found) and len(self.opsPermutations) >= 2**(self.depth - 1):
                self.finalString = "Impossible"
                return
        else:
            self.normalOrder(i + 1, ops + "+")
            self.normalOrder(i + 1, ops + "*")


    def left(self, i, currentValue, ops):

        if self.found:
            return

        if (i == self.depth):

            tempArray = []

            for j in range(len(ops)):
                tempArray.append(ops[j])
            self.opsPermutations.append(tempArray)

            expressionString = str(self.nums[0])

            for j in range(self.depth - 1):
                expressionString = expressionString + " " + tempArray[j] + " "
                expressionString = expressionString + str(self.nums[j + 1])

            #print(expressionString)
            #print(currentValue)
            result = currentValue

            if result == self.target:
                self.found = True
                self.finalString = expressionString
                return
            elif (not self.found) and len(self.opsPermutations) >= 2**(self.depth - 1):
                self.finalString = "Impossible"
                return
        else:
            self.left(i + 1, self.add(currentValue, self.nums[i]), ops + "+")
            self.left(i + 1, self.multiply(currentValue, self.nums[i]), ops + "*")

self.order == 'L' ? result = currentValue : result = eval(expressionString)

else:
    if self.order == 'L':
        self.left(i + 1, self.add(currentValue, self.nums[i]), ops + "+")
        self.left(i + 1, self.multiply(currentValue, self.nums[i]), ops + "*")
    else:
        self.normalOrder(i + 1, ops + "+")
        self.normalOrder(i + 1, ops + "*")

    def leftToRight(self, i, currentValue, ops):
        #print ("curr: " + str(currentValue), " i: " + str(i), "target: " + str(self.target))

        if (currentValue > self.target):
            return
        elif (i == self.depth) and not self.found:
            if (currentValue == self.target):
                self.found = True
                self.finalString = ops
                return
            else:
                return
        elif self.found:
            return
        else:

            plus = ops + "+"
            times = ops + "*"

            self.leftToRight(i + 1, self.add(currentValue, self.nums[i]), plus)
            self.leftToRight(i + 1, self.multiply(currentValue, self.nums[i]), times)



def main():

    # for line in input
    # if line is odd number
    # it's a number sequence line
    # assign those numbers to a nums variable (using a for loop?)
    # read the next line
    # take the target and assign it to a variable
    # create a class instance with:
    # - the nums variable as the first argument of the Line constructor
    # - the target as the second argument

    # if the order is L:
        # apply the leftToRight function on the line instance
    # elif the order is N:
        # apply the normal function on the line instance

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

            # Error: Not 2 arguments in second line of input.
            if len(constraints) != 2:
                print("Error: Second line of input must be the target value, followed by either 'L' or 'N'")
                return

            # Error: Target value is not an integer.
            if not constraints[0].isdigit():
                print("Error: First input of second line must be a target value in the form of an integer.")
                return

            target = int(constraints[0]) # Target is the first input on the second line cast to an int

            order = constraints[1].capitalize() # Either 'L' or 'N'

            myLine = Line(numSequence, target) # Create the class instance from the input

            # Error: Order is not L or N
            if (order != 'L' and order != 'N'):
                print('Invalid input for order')
                print(order)
                return

            # Left to right order of operations (L)
            elif (order == 'L'):
                myLine.left(1, numSequence[0], "") #leftToRIght
                # If target value is possible
                '''
                if myLine.found:
                    result = str(numSequence[0])
                    for i in range(len(myLine.finalString)):
                        result = result + " " + myLine.finalString[i] + " " + str(myLine.nums[i+1])
                    print("L", myLine.target, result)
                # Target value is impossible
                else:
                    print("L", myLine.target, "Impossible")
                '''
                print("L", myLine.target, myLine.finalString)

            # Normal order of operations (N)
            else:
                myLine.normalOrder(1, "")
                print("N", myLine.target, myLine.finalString)

            numSequence = [] # reset the array for the next input

        count +=1 # increment for even/odd lines



if __name__ == "__main__":
    main()
