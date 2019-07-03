import java.util.ArrayList;

import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdOut;

public class KdTree {
    private int n;
    private Node root;
    private static final boolean VERTICAL = true;

    private static class Node {
        private Point2D p;      // the point
        private RectHV rect;    // the axis-aligned rectangle corresponding to this node
        private Node lb;        // the left/bottom subtree
        private Node rt;        // the right/top subtree

        public Node(Point2D p) {
            this. p = p;
        }
     }
    // construct an empty set of points 
    public KdTree() {
        n = 0;
        root = null;
    }

    // is the set empty? 
    public boolean isEmpty() {
        return n == 0;
    }

    // number of points in the set 
    public int size() {
        return n;
    }

    // add the point to the set (if it is not already in the set)
    public void insert(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        root = put(root, p, VERTICAL);
    }

    private Node put(Node node, Point2D p, boolean division) {
        if (node == null) {
            n++;
            return new Node(p);
        }

        if (p.equals(node.p)) {
            return node;
        }
        if (division == VERTICAL) {
            if (p.x() <= node.p.x()) {
                node.lb = put(node.lb, p, !division);
            } else {
                node.rt = put(node.rt, p, !division);
            }
        } else {
            if (p.y() <= node.p.y()) {
                node.lb = put(node.lb, p, !division);
            } else {
                node.rt = put(node.rt, p, !division);
            }
        }
        return node;
    }

    // does the set contain point p? 
    public boolean contains(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        return get(root, p, VERTICAL);
    }

    private boolean get(Node node, Point2D p, boolean division) {
        if (node == null) return false;
        if (division == VERTICAL) {
            if (p.x() < node.p.x()) {
                return get(node.lb, p, !division);
            } else if (p.x() > node.p.x()) {
                return get(node.rt, p, !division);
            } else {
                return p.y() == node.p.y();
            }
        } else {
            if (p.y() < node.p.y()) {
                return get(node.lb, p, !division);
            } else if (p.y() > node.p.y()) {
                return get(node.rt, p, !division);
            } else {
                return p.x() == node.p.x();
            }
        }
    }

    // draw all points to standard draw 
    public void draw() {
    }

    // all points that are inside the rectangle (or on the boundary) 
    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) throw new IllegalArgumentException();
        ArrayList<Point2D> allPointsInside = new ArrayList<>();
        return allPointsInside;
    }

    // a nearest neighbor in the set to point p; null if the set is empty 
    public Point2D nearest(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        Point2D nearest = null;
        return nearest;
    }

    // unit testing of the methods (optional) 
    public static void main(String[] args) {
        KdTree set = new KdTree();
        set.insert(new Point2D(0.7, 0.2));
        set.insert(new Point2D(0.7, 0.2));
        set.insert(new Point2D(0.2, 0.3));
        set.insert(new Point2D(0.4, 0.7));
        set.insert(new Point2D(0.9, 0.6));
        
        StdOut.println(set.contains(new Point2D(0.7, 0.2)));
        
        StdOut.println(set.contains(new Point2D(0.2, 0.3)));
        StdOut.println(set.contains(new Point2D(0.4, 0.7)));
        StdOut.println(set.contains(new Point2D(0.9, 0.6)));
        
        StdOut.println(set.size());
        StdOut.println("================================");
        StdOut.println(set.contains(new Point2D(0.5, 0.4)));
        StdOut.println(set.contains(new Point2D(0.1, 0.1)));
        StdOut.println(set.contains(new Point2D(0.2, 0.2)));
        StdOut.println(set.contains(new Point2D(0.3, 0.3)));
        StdOut.println(set.contains(new Point2D(0.4, 0.4)));
        StdOut.println(set.contains(new Point2D(0.5, 0.5)));
    }
}