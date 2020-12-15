/*
if (i < points.size() - 1) {
  Circle twoPointCircle;
  for (int k = i + 1; k < points.size(); k++) {
    twoPointCircle = SmallestEnclosingCircle.makeCircleTwoPoints(points, points.get(i), points.get(k));
    System.out.println(twoPointCircle.toString());
    int innerPoints = containingPoints(twoPointCircle, points);
    if (innerPoints <= 12) {
      if (innerPoints == 12) {
        usefulCircles.add(twoPointCircle);
        countUsefulCircles++;
      } else if (innerPoints > biggestU12CirclePointCount) {
        biggestU12CirclePointCount = innerPoints;
        biggestU12Circle = twoPointCircle;
      } else if (innerPoints == biggestU12CirclePointCount) {
        if (twoPointCircle.r > biggestU12Circle.r) {
          biggestU12Circle = twoPointCircle;
          biggestU12CirclePointCount = innerPoints;
        }
      }
    }
  }
}
*/


/*
Circle threePointCircle;
if (i < points.size() - 2) {
  for (int j = i + 1; j < points.size() - 1; j++) {
    for (int k = j + 1; k < points.size(); k++) {
      threePointCircle = SmallestEnclosingCircle.makeCircumcircle(points.get(i), points.get(j), points.get(k));
      System.out.println(threePointCircle.toString());
      int innerPoints = containingPoints(threePointCircle, points);
      if (innerPoints <= 12) {
        if (innerPoints == 12) {
          usefulCircles.add(threePointCircle);
          countUsefulCircles++;
        } else if (innerPoints > biggestU12CirclePointCount) {
          biggestU12CirclePointCount = innerPoints;
          biggestU12Circle = threePointCircle;
        } else if (innerPoints == biggestU12CirclePointCount) {
          if (threePointCircle.r > biggestU12Circle.r) {
            biggestU12Circle = threePointCircle;
            biggestU12CirclePointCount = innerPoints;
          }
        }
      }
    }
  }
}
*/

/*
Circle threePointCircle = SmallestEnclosingCircle.makeCircumcircle(closestPoints.get(0), closestPoints.get(10), closestPoints.get(11));
System.out.print("Three point circle for above points: ");
System.out.println(threePointCircle.toString());
System.out.print("Points within this circle: ");
System.out.println(containingPoints(threePointCircle, closestPoints));
*/

//double decrement = ((Circle.MULTIPLICATIVE_EPSILON - 1) * (threePointCircle.r + .5));
//System.out.print("Circle radius reduced by ");
//System.out.println(decrement);

/*
System.out.println();
// take the 3 point circle dimensions and make a slightly smaller circle
Circle smallerCircle = new Circle(threePointCircle.c, threePointCircle.r - decrement);
System.out.print("Shrunk circle: ");
System.out.println(smallerCircle.toString());
System.out.print("Circle contains 12th point: ");
System.out.println(smallerCircle.contains(closestPoints.get(11))); // Should be false
System.out.print("Points within this circle: ");
System.out.println(containingPoints(smallerCircle, closestPoints));
*/

System.out.println();

/*
Circle twoPointCircle = SmallestEnclosingCircle.makeCircleTwoPoints(closestPoints, closestPoints.get(0), closestPoints.get(11));
System.out.print("Two point circle for above points: ");
System.out.println(twoPointCircle.toString());
System.out.print("Points within this circle: ");
System.out.println(containingPoints(twoPointCircle, closestPoints));
*/

Circle makeDiameterCircle = SmallestEnclosingCircle.makeDiameter(closestPoints.get(0), closestPoints.get(11));
System.out.print("Circle by diameter for above points: ");
System.out.println(makeDiameterCircle.toString());
System.out.print("Points within this circle: ");
System.out.println(containingPoints(makeDiameterCircle, closestPoints));

/*
double decrement = ((Circle.MULTIPLICATIVE_EPSILON - 1) * (makeDiameterCircle.r + .5));
System.out.print("Circle radius reduced by ");
System.out.println(decrement);

System.out.println();
// take the 3 point circle dimensions and make a slightly smaller circle
Circle smallerCircle2 = new Circle(makeDiameterCircle.c, makeDiameterCircle.r - decrement);
System.out.print("Shrunk circle: ");
System.out.println(smallerCircle2.toString());
System.out.print("Circle contains 12th point: ");
System.out.println(smallerCircle2.contains(closestPoints.get(11))); // Should be false
System.out.print("Points within this circle: ");
System.out.println(containingPoints(smallerCircle2, closestPoints));
*/
