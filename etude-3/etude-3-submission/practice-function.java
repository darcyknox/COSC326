// Parses a string expression and returns the answer

private int eval(String expString) {
  // multiply the numbers that have a * between them and add them to and array.
  // then add everything else to the array and get the sum.
  String[] expArr = expString.replaceAll("\\s+", "").split("");
  int result = 0;
  int product;
  int j;
  //
  for (j = 0; j < expArr.length; j++) {
    if (expArr[j].matches("\\*")) {
      product = multiply(Integer.parseInt(expArr[j - 1]), Integer.parseInt(expArr[j + 1]));
      expArr[j - 1] = expArr[j] = "";
      expArr[j + 1] = Integer.toString(product);
    }
  }
  for (j = 0; j < expArr.length; j++) {
    if (expArr[j].matches("\\d+")) {
      result += Integer.parseInt(expArr[j]);
    }
  }
  return result;
}
