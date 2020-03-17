import sys

class Line:
    """docstring for Line"""

    def __init__(self, nums, target):
        super(Line, self).__init__()
        self.nums = nums
        self.depth = len(nums)
        self.target = target
        self.found = False

    def add(self, x, y):
        return x + y


    def multiply(self, x, y):
        return x * y


# add the sign, and the nums[i]



    def left(self, i, currentValue):
        #print ("curr: " + str(currentValue), " i: " + str(i), "target: " + str(self.target))

        if (currentValue > self.target):
            #print("Target not found (values exceed target): " + str(self.target))
            #print (self.found)
            return
        elif (i == self.depth):
            if (currentValue == self.target):
                #print ("Found target: " + str(currentValue))
                self.found = True
                #print (self.found)
                return
            #print("Target not found (max depth reached): " + str(self.target))
            return
        elif self.found:
            return
        else:
            #print ("current value: " + str(currentValue))
            self.left(i + 1, self.add(currentValue, self.nums[i]))
            #print ("current value: " + str(currentValue))
            self.left(i + 1, self.multiply(currentValue, self.nums[i]))




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
        # apply the left function on the line instance
    # elif the order is N:
        # apply the normal function on the line instance

    count = 0
    numSequence = []

    for line in sys.stdin:

        if count % 2 == 0:
            for numberString in line.strip().split(" "):
                numSequence.append(int(numberString)) #numSequence is now the list of ints to be parsed

        else:
            constraints = line.strip().split(" ")
            target = int(constraints[0]) #target is the first input on the second line and is in integer form
            # orderOfOperations = constraints[1]
            myLine = Line(numSequence, target) #order...

            '''print("Depth:", myLine.depth)
            print("Found:", myLine.found)
            print("nums:", myLine.nums)
            print("Target:", myLine.target)'''

            myLine.left(1, 1)

            if myLine.found:
                print("Target found", myLine.nums, myLine.target)
            else:
                print("Impossible", myLine.nums, myLine.target)

            numSequence = []

        count +=1



if __name__ == "__main__":
    main()