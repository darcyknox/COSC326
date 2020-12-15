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

public class CordlessPhones{
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
    List<Point> points = new ArrayList<>();
    for(int x = 0; x < sites.size(); x++){
        Site xSite = sites.get(x);
        points.add(new Point(xSite.east, xSite.north));
   }
    
    /*
     For every site in sites array, find the 11th furthest away site
     */
    Double r = Double.POSITIVE_INFINITY; // Start off with the radius being Infinity
    
    for (int point1Index=0; point1Index < points.size()-1; point1Index++){
      for (int point2Index=0; point2Index < points.size(); point2Index++){
        List<Point> twoPoints = new ArrayList<>();
        twoPoints.add(points.get(point1Index));
        twoPoints.add(points.get(point2Index));
        Circle possible = SmallestEnclosingCircle.makeCircle(twoPoints);
        boolean twoPointsBad = false;
        int twoPointCount=0;
        if (possible.r > r){   // This is the smallest circle that can have these two points on the boundary.
            continue;               // Go to the next iteration of the loop (next point2)
        }
        for (int point3Index=0; point3Index < points.size(); point3Index++){
          if (possible.contains(points.get(point3Index))){
            twoPointCount++;
              if (twoPointCount >= 12){   // Too many points in the circle
              twoPointsBad = true;    // We know that it's bad
              break;                  // Don't check any more point 3s
            }
          }
          List<Point> threePoints = new ArrayList<>();
          threePoints.add(points.get(point1Index));
          threePoints.add(points.get(point2Index));
          threePoints.add(points.get(point3Index));
          Circle possible2 = SmallestEnclosingCircle.makeCircle(threePoints);
          if (possible2.r > r){  // This circle is too big
            continue;               // go to the next point3
          }
          boolean threePointsBad = false;
          int threePointCount = 0;
          for (int point4Index=0; point4Index < sites.size(); 
               point4Index++){
                 if (possible2.contains(points.get(point3Index))){
                   threePointCount++;
                   if (threePointCount >= 12){     // Too many points in the circle
                       threePointsBad = true;      // We know that it's bad
                       break;                      // Don't check any more point 4s
                   }
                 }
               }
               if (threePointsBad){                // If it's bad no bigger circle will work
                   if (possible2.r < r){
                   r = possible2.r;           // The target circle is at most the size of this circle
                 }
                 continue;                           // Go to the next iteration of the loop (next point3)
               }
        }
        if (twoPointsBad){              // If it's bad no bigger circle will work
            if (possible.r < r){
              r = possible.r;    // The target circle is at most the size of this circle
            }
          continue;                   // Go to the next iteration of the loop (next point2)
        }
      }
    }
    
    
    
    System.out.println("Smallest" + r);
    
    Double smallestDouble = Math.floor(r * 100.0) / 100.0;
    System.out.println("Smallest double " + smallestDouble);
    
    
    return r;
    
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