import sys

class Arithmetic:

    def __init__(self, nums, target, order):
        super(Arithmetic, self).__init__()
        self.nums = nums # The array of input numbers
        self.depth = len(nums) # Depth of the (abstract) binary tree, or n.
        self.target = target # The target value.
        self.found = False # Boolean for if the target value is found.
        self.finalString = "" # The working expression, or 'Impossible.'
        self.opsPermutations = [] # A 2D array of every possible sequence of operations.
        self.order = order # Left to right, or Normal order of operations

    # Addition utility function
    def add(self, x, y):
        return x + y

    # Multiplication utility function
    def multiply(self, x, y):
        return x * y

    # calculate assumes an binary tree abstraction for evaluating permutations of operation sequences.
    def calculate(self, i, ops, currentValue = None):

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
        else:
            if self.order == 'L':
                self.calculate(i + 1, ops + "+", self.add(currentValue, self.nums[i]))
                self.calculate(i + 1, ops + "*", self.multiply(currentValue, self.nums[i]))
            else:
                self.calculate(i + 1, ops + "+")
                self.calculate(i + 1, ops + "*")


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
                myArithmetic.calculate(1, "", numSequence[0])
                print(order, myArithmetic.target, myArithmetic.finalString)

            numSequence = [] # reset the array for the next input

        count +=1 # increment for even/odd lines


if __name__ == "__main__":
    main()
