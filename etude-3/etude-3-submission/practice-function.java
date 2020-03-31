private void calculate(int i, String expressionString, int currentValue) {

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
    String possiblePermutation = "";

    for (int j = 0; j < ops.length(); j++) {
      possiblePermutation += ops.charAt(j);
    }
    this.opsPermutations.add(possiblePermutation);

    // L SUCCESS
    if (this.order == 'L' & currentValue == this.target) {
      System.out.println("Found target");
      this.found = true;

      this.finalString = expressionString;
      return;

    } else if (this.order == 'N') {

      // N SUCCESS
      if (eval(expressionString) == this.target) {
        System.out.println("Found target");
        this.found = true;
        this.finalString = expressionString;
        return;
      }

    } else if (!(this.found) & this.opsPermutations.size() >= Math.pow(2, this.depth - 1)) {
      // Only works on 'L'
      this.finalString = "Impossible";
      return;
    }
  } else {
    this.calculate(i + 1, expressionString + "+" + Integer.toString(this.nums[i]), add(currentValue, this.nums[i]));
    this.calculate(i + 1, expressionString + "*" + Integer.toString(this.nums[i]), multiply(currentValue, this.nums[i]));
  }


}
