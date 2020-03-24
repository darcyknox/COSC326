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

    def add(self, x, y):
        return x + y


    def multiply(self, x, y):
        return x * y


# add the sign, and the nums[i]

    def normalOrder(self, i, ops):

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



    def leftToRight(self, i, currentValue, ops):
        #print ("curr: " + str(currentValue), " i: " + str(i), "target: " + str(self.target))

        if (currentValue > self.target):
            #print("Target not found (values exceed target): " + str(self.target))
            #print(self.found)
            return
        elif (i == self.depth) and not self.found:
            if (currentValue == self.target):
                #print ("Found target: " + str(currentValue))
                self.found = True
                #print (self.found)
                #print ("final", self.oparray)
                self.finalString = ops
                return
            else:
                #self.oparray.pop()
                #print("Target not found (max depth reached): " + str(self.target))
                return
        elif self.found:
            return
        else:

            plus = ops + "+"
            times = ops + "*"

            #op = op + "+" + str(self.nums[i])
            #print ("current value: " + str(currentValue))
            self.leftToRight(i + 1, self.add(currentValue, self.nums[i]), plus)

            #op = op + "*" + str(self.nums[i])
            #print ("current value: " + str(currentValue))
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

    count = 0 # tracks whether a line is even or odd
    numSequence = []

    for line in sys.stdin:

        if count % 2 == 0:
            for numberString in line.strip().split(" "):
                numSequence.append(int(numberString)) #numSequence is now the list of ints to be parsed

        else:
            constraints = line.strip().split(" ")
            target = int(constraints[0]) #target is the first input on the second line and is in integer form
            order = constraints[1].capitalize()
            # orderOfOperations = constraints[1]
            myLine = Line(numSequence, target) #order...
            '''print("Depth:", myLine.depth)
            print("Found:", myLine.found)
            print("nums:", myLine.nums)
            print("Target:", myLine.target)'''

            if (order != 'L' and order != 'N'):
                print('Invalid input for order')
                print(order)
                return
            elif (order == 'L'):
                myLine.leftToRight(1, numSequence[0], "")

                if myLine.found:

                    #print(myLine.finalString)
                    #print(myLine.finalString)
                    result = str(numSequence[0])
                    for i in range(len(myLine.finalString)):
                        result = result + " " + myLine.finalString[i] + " " + str(myLine.nums[i+1])
                    #result = result + " = " + str(target)
                    print("L", myLine.target, result)
                else:
                    #print(myLine.nums)
                    print("L", myLine.target, "Impossible")

            else:
                myLine.normalOrder(1, "")

                print("N", myLine.target, myLine.finalString)

            numSequence = [] # reset the array for the next input

        count +=1 # increment for even/odd lines



if __name__ == "__main__":
    main()
