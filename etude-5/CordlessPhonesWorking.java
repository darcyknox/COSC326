import java.util.*;
import java.lang.Math;
import java.util.Arrays;

/**
 * Cordless Phones
 * Etude 5
 * Semester 1 2020
 *
 * Given a set of positions of telephones, it work out the maximum range that
 * guarantees that not more than eleven of the telephones are within range.
 *
 * Uses SmallestEnclosingCircle.java library
 *
 * @author: Hugo Baird
 * @author: Leon Hoogenraad
 * @author: Cedric Stephani
 * @author: Darcy Knox
 */

public class CordlessPhonesWorking{
  //For reading in input
  public static Scanner sc = new Scanner(System.in);
  //Array of telephone sites
  public static ArrayList<Site> sites = new ArrayList<>();
  //The value of pi hopefully - pretty sure this is redundant.
  public static double pi = Math.PI;
  public static void main(String[] args){
    ArrayList<Double> eastPoints = new ArrayList <>();
    ArrayList<Double> northPoints = new ArrayList <>();
    try{
      sc.nextLine();
      while(sc.hasNextDouble()){
        double east = sc.nextDouble();
        double north = sc.nextDouble();
        eastPoints.add(east);
        northPoints.add(north);
        sites.add(new Site(east, north));
      }
    }catch(NumberFormatException ne){
      System.out.println("Wrong input format found \nFormat: 'double' 'double'");
    }catch(Exception e){
      e.printStackTrace();
    }

    // Checks that there are equal amount of east and north points for each site.
    if(!(eastPoints.size()==northPoints.size())){
      System.out.println("Number of east points and north points aren't equal");
    }
    sc.close();
    if(sites.size() < 12){
      System.out.println(Double.POSITIVE_INFINITY);
    }
    else{
      double smallestDouble = calculatePoints();
      System.out.println(smallestDouble);
    }
  }


  /**
   * Generate points and add them to an array to create smallest enclosing circles of 11 points
   */
   public static double calculatePoints() {
    double[] eleventh_lens = new double[sites.size()];

    // List of circles from SmallestEnclosingCircle class
    ArrayList<Circle> circles = new ArrayList<>();
    ArrayList<Circle> usefulCircles = new ArrayList<>();
    int countUsefulCircles = 0;
    int biggestU12CirclePointCount = 0;
    int smallest12PlusCirclePointCount = 0;
    Circle biggestU12Circle = new Circle(new Point(0.0, 0.0), 0.0); // initialise with null circle
    Circle smallest12PlusCircle = new Circle(new Point(0.0, 0.0), Double.POSITIVE_INFINITY); // initialise with null circle
    double smallRadius = Double.POSITIVE_INFINITY;

    /*
     For every site in sites array, find the 11th furthest away site
     */
    long start = System.nanoTime();
    for(int i = 0; i < sites.size(); i++){
      // List of closest points to the current site
      List<Point> points = new ArrayList<>();
      List<Point> closestPoints = new ArrayList<>();
      // Our current site on our journey through this for loop
      Site currSite = sites.get(i);
      // This array will hold the distances from each site to currSite
      double[] lengths = new double[sites.size()];
      for(int x = 0; x < sites.size(); x++){
        Site xSite = sites.get(x);
        lengths[x] = distance(currSite.east, currSite.north, xSite.east, xSite.north);
        points.add(new Point(xSite.east, xSite.north));
      }
      // Makes a circle using each point to each other point as a diameter.
      // If a circle contains 12 points, it's deemed useful and we add it to the
      // usefulCircles ArrayList.
      // Also tracks the circle with the most inner points less than 12.

      Circle threePointCircle;
        if (i < points.size() - 2) {
          for (int j = i + 1; j < points.size() - 1; j++) {
            for (int k = j + 1; k < points.size(); k++) {
              List<Point> threePoints = new ArrayList<>();
              threePoints.add(points.get(i));
              threePoints.add(points.get(j));
              threePoints.add(points.get(k));
              threePointCircle = SmallestEnclosingCircle.makeCircle(threePoints);
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
              if (innerPoints >= 12) { // we want the smallest of these circles
                if (threePointCircle.r < smallest12PlusCircle.r) {
                  smallest12PlusCircle = threePointCircle;
                  smallest12PlusCirclePointCount = innerPoints;
                }
              }
            }
          }
        }
      }

      long end = System.nanoTime();
      System.out.println((end - start)/ Math.pow(10, 9));


      System.out.println("Smallest 12 Plus Circle: " + smallest12PlusCirclePointCount);
      System.out.println("Smallest 12 Plus Circle radius: " + smallest12PlusCircle.r);
      System.out.println("Biggest U12 Circle: " + biggestU12CirclePointCount);
      System.out.println("Biggest U12 Circle radius: " + biggestU12Circle.r);

      // Assigns smallest either:
      // 1. The value of the smallest circles that contains 12 points.
      // 2. The largest circle that contains less than 12 points.
      Circle smallest;
      if (usefulCircles.size() > 0) {
        smallest = getSmallestCircle(usefulCircles);
      } else {
        smallest = biggestU12Circle;
      }

      if (smallest.r > smallest12PlusCircle.r) {
        smallest = smallest12PlusCircle;
      }

      //Circle smallest = getSmallestCircle(circles);

      Double smallestDouble = Math.floor(smallest.r * 100.0) / 100.0;

      System.out.println("------------------------");

      System.out.println("Selected circle: " + smallest.toString());

      return smallestDouble;

    }


    // Returns the straight line distance between two points.
    // Takes two East, North -> (x,y) co-ordinates as arguments.
    private static double distance(double x1, double y1, double x2, double y2) {
      return Math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1));
    }

    // Returns the smallest circle by radius
    private static Circle getSmallestCircle(ArrayList<Circle> circles) {
      int minRadiusIndex = 0;
      double minRadius = circles.get(0).r;
      for (int z = 1; z < circles.size(); z++) {
        if (circles.get(z).r < minRadius) {
          minRadius = circles.get(z).r;
          minRadiusIndex = z;
        }
      }
      //System.out.println("Min radius: " + Double.toString(minRadius));
      //System.out.println("Smallest circle: " + circles.get(minRadiusIndex));
      //System.out.println("-----------------------------------");
      return circles.get(minRadiusIndex);
    }

    // Returns the biggest circle by radius
    private static Circle getBiggestCircle(ArrayList<Circle> circles) {
      int maxRadiusIndex = 0;
      double maxRadius = circles.get(0).r;
      for (int z = 1; z < circles.size(); z++) {
        if (circles.get(z).r > maxRadius) {
          maxRadius = circles.get(z).r;
          maxRadiusIndex = z;
        }
      }
      return circles.get(maxRadiusIndex);
    }

    // Counts the number of points within the circle
    private static int containingPoints(Circle c, List <Point> points) {
      int count = 0;
      for (Point p: points) {
        if (c.contains(p)) {
          count++;
        }
      }
      return count;
    }

    /**
     * This method will return true if the given 3 points are in a line.
     * It computes this by checking if either the x or y values of all 3 points
     * are equal. If they are, this means the points are in a line.
     */
    private static boolean isInLine(Point p1, Point p2, Point p3){
      /*
       * We might be able to remove the p2.x == p3.x (as with the y check as well)
       * because if p1.x == p2.x and p3.x then p2.x must be == p3.x.
       */
      if((p1.x == p2.x && p1.x == p3.x && p2.x == p3.x)||
         (p1.y == p2.y && p1.y == p3.y && p2.y == p3.y)){
        return true;
      }
      return false;
    }
  }
