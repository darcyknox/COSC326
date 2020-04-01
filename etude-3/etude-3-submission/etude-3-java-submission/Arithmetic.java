import java.util.*;
import java.lang.Math;
import java.lang.String;
import java.lang.Character;

public class Arithmetic {

  private static int[] nums;
  private static int depth;
  public int target;
  private static Boolean found = false;
  public String finalString;
  public static char order;

  Arithmetic(int[] nums, int target, char order) {
    this.nums = nums;
    this.target = target;
    this.order = order;
    this.depth = nums.length;
  }

  public int getTarget() {
    return target;
  }

  public int add(int x, int y) {
    return x + y;
  }

  public int multiply(int x, int y) {
    return x * y;
  }

  /** Recurses through an abstract of a binary tree while tracking the current value at each step
    */
  private void calculateLeft(int i, String expressionString, int currentValue) {

    if (this.found == true || currentValue > this.target) {
      return;
    } else if (i == this.depth) {
      if (currentValue == this.target) {
        this.found = true;
        this.finalString = this.order + " " + this.target + " " + expressionString;
        return;
      } else if (!(this.found)) {
        return;
      }
    } else {
      this.calculateLeft(i + 1, expressionString + " + " + Integer.toString(this.nums[i]), add(currentValue, this.nums[i]));
      this.calculateLeft(i + 1, expressionString + " * " + Integer.toString(this.nums[i]), multiply(currentValue, this.nums[i]));
    }
  }

  /** Treats the expression as the sum of many chunks of products.
    * @param sum is the sum of the products before the current number.
    * - if the operation is multiplication, the sum stays the same as the chunk we are operating
    *   upon, as it does not yet have a final value that we can add to the sum.
    * - a chunk is everything in-between addition signs '+'
    * @param last tracks the value of the current chunk.
    */
  private void calculateNormal(int i, int sum, int last, int currentValue, String expressionString) {

    if (this.found == true || currentValue > this.target) {
      return;
    } else if (i == this.depth) {
      if (currentValue == this.target) {
          this.found = true;
          this.finalString = this.order + " " + this.target + " " + expressionString;
          return;
      } else if (!(this.found)) {
        return;
      }
    } else {
      this.calculateNormal(i + 1, sum + last, this.nums[i], currentValue + this.nums[i], expressionString + " + " + Integer.toString(this.nums[i]));
      this.calculateNormal(i + 1, sum, last * this.nums[i], (last * this.nums[i]) + sum, expressionString + " * " + Integer.toString(this.nums[i]));
    }
  }


  public static void main(String[] args) {

    // Tracks lines
    int count = 0;

    Scanner stdin = new Scanner(System.in);

    // Buffer array
    ArrayList<Integer> numsArrayList = new ArrayList<Integer>();

    while (stdin.hasNextLine()) {

      String line = stdin.nextLine();

      if (count % 2 == 0) {
        String[] numberString = line.split(" ");
        int i = 0;
        for (String n : numberString) {
          numsArrayList.add(Integer.parseInt(n));
        }

      } else {

        String[] constraints = line.split(" ");

        // Validate number of constraints
        if (constraints.length != 2) {
          System.out.println("Error: invalid constraints");
        }

        // Validate target
        for (int k = 0; k < constraints[0].length(); k++) {
          if (!Character.isDigit(constraints[0].charAt(k))) {
            System.out.println("Invalid target");
            return;
          }
        }

        int target = Integer.parseInt(constraints[0]);
        char order = constraints[1].charAt(0);
        order = Character.toUpperCase(order);

        // Validate order
        if (!(order == 'L' | order == 'N')) {
          System.out.println("Invalid order");
          return;
        }

        // Create numSequence from inputs
        int[] numSequence = new int[numsArrayList.size()];

        for (int i = 0; i < numsArrayList.size(); i ++) {
          numSequence[i] = numsArrayList.get(i);
        }

        // Clear the input buffer array
        numsArrayList.clear();

        // Set up test object
        Arithmetic test = new Arithmetic(numSequence, target, order);
        test.found = false;
        test.finalString = order + " " + Integer.toString(target) + " " + "impossible";
        //final long start = System.nanoTime();

        // Execute by order argument
        if (order == 'L') {
          test.calculateLeft(1, Integer.toString(nums[0]), numSequence[0]);
        } else if (order == 'N') {
          test.calculateNormal(1, 0, numSequence[0], numSequence[0], Integer.toString(numSequence[0]));
        }

        //final long end = System.nanoTime();
        System.out.println(test.finalString);
        //System.out.println((end - start)/ Math.pow(10, 9));
      }
      count++;
    }
  }
}
