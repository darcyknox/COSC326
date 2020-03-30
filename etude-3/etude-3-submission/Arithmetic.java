import java.util.*;
import java.lang.Math;
import java.lang.String;

public class Arithmetic {

  private static int[] nums;
  private static int depth;
  public int target;
  private static Boolean found = false;
  public String finalString = "";
  public static ArrayList<String> opsPermutations = new ArrayList<String>();
  public static char order;
  public String operations = "+*";

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

  // Works for left to right

  private void calculate(int i, String ops, int currentValue) {

    /**
    System.out.println("depth = " + this.depth);
    System.out.println("i = " + i);
    System.out.println("ops = " + ops);
    System.out.println("currentValue = " + Integer.toString(currentValue));
    */

    if (this.found == true) {
      //System.out.println("First if");
      return;
    } else if (i == this.depth) {
      //System.out.println("At max depth");
      String possiblePermutation = "";

      for (int j = 0; j < ops.length(); j++) {
        possiblePermutation += ops.charAt(j);
      }
      this.opsPermutations.add(possiblePermutation);

      String expressionString = Integer.toString(this.nums[0]);

      for (int j = 0; j < this.depth - 1; j++) {
        expressionString += " " + possiblePermutation.charAt(j) + " ";
        expressionString += Integer.toString(this.nums[j + 1]);
      }

      int result = 0;

      if (this.order == 'L') {
        result = currentValue;
      }

      if (result == this.target) {
        System.out.println("Found target");
        this.found = true;
        this.finalString = expressionString;
        return;
      } else if (!(this.found) & this.opsPermutations.size() >= Math.pow(2, this.depth - 1)) {
        this.finalString = "Impossible";
        return;
      }

    } else if (currentValue >= this.target) {
      return;
    } else {
      this.calculate(i + 1, ops + "+", add(currentValue, this.nums[i]));
      this.calculate(i + 1, ops + "*", multiply(currentValue, this.nums[i]));
    }


  }

  private static int eval(String evalString) {
    String[] result = evalString.split("+*");
    System.out.println(result);
    return 0;
  }

  public static void main(String[] args) {

    int count = 0;

    Scanner stdin = new Scanner(System.in);
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
        if (constraints.length != 2) {
          System.out.println("Error: invalid constraints");
        }
        // Try catch to make sure target is an integer
        int target = Integer.parseInt(constraints[0]);
        char order = constraints[1].charAt(0);

        if (!(order == 'L' | order == 'N')) {
          System.out.println("Invalid order");
        }

        int[] numSequence = new int[numsArrayList.size()];
        for (int i = 0; i < numsArrayList.size(); i ++) {
          numSequence[i] = numsArrayList.get(i);
        }
        numsArrayList.clear();
        System.out.println(Arrays.toString(numSequence));

        Arithmetic test = new Arithmetic(numSequence, target, order);
        test.found = false; // understand static, public, private etc.
        System.out.println("Target: " + test.getTarget());
        final double startTime = System.currentTimeMillis();
        test.calculate(1, "", numSequence[0]);
        final double endTime = System.currentTimeMillis();
        System.out.println(test.finalString);
        System.out.println("Execution time: " + (endTime - startTime));
      }
      count++;
    }



  }

}
