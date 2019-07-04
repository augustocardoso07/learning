import java.util.ArrayList;

import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.SET;
import edu.princeton.cs.algs4.StdOut;

public class PointSET {

    private SET<Point2D> set;
    // construct an empty set of points 
    public PointSET() {
        //set = new SET<Point2D>();
        set = new SET<>();
    }

    // is the set empty? 
    public boolean isEmpty() {
        return set.isEmpty();
    }

    // number of points in the set 
    public int size() {
        return set.size();
    }

    // add the point to the set (if it is not already in the set)
    public void insert(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        set.add(p);
    }

    // does the set contain point p? 
    public boolean contains(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        return set.contains(p);
    }

    // draw all points to standard draw 
    public void draw() {
        for (Point2D p : set) {
            p.draw();
        }
    }

    // all points that are inside the rectangle (or on the boundary) 
    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) throw new IllegalArgumentException();
        ArrayList<Point2D> allPointsInside = new ArrayList<>();
        for (Point2D p: set) {
            if (rect.contains(p)) allPointsInside.add(p);
        }
        return allPointsInside;
    }

    // a nearest neighbor in the set to point p; null if the set is empty 
    public Point2D nearest(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        Point2D nearest = null;
        double distance = Double.POSITIVE_INFINITY;
        for (Point2D that : set) {
            if (p.distanceTo(that) < distance) {
                nearest = that;
                distance = p.distanceTo(that);
            }
        }
        return nearest;
    }

    // unit testing of the methods (optional) 
    public static void main(String[] args) {
        PointSET set = new PointSET();
        set.insert(new Point2D(2, 2));
        set.insert(new Point2D(3, 3));
        set.insert(new Point2D(1, 2));
        set.insert(new Point2D(4, 2));

        StdOut.println(set.contains(new Point2D(2, 2)));
    }
 }