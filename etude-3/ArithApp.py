import sys
import Line


def calculate(arr, target):

    ops = [add, multiply]

    # This only works for an array of 3 numbers
    for i in range(2):
        for j in range(2):
            result = (ops[j](arr[2], (ops[i](arr[0], arr[1]))))
            if result == target:
                print (str(arr) + " " + ops[i].__name__ + " " + ops[j].__name__)
                return




def main():

    # User Input
    '''count = 0
    for line in sys.stdin:
        if count % 2 == 0:
            print("Order & target ")'''

    calculate([1, 2, 3], 5)
    calculate([1, 2, 3], 9)

    line1 = Line([1, 2, 3], 5)

    #line1.left(1, nums[i])



if __name__ == "__main__":
    main()
