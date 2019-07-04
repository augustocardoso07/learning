import java.util.ArrayList;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class KdTree {
    private int n;
    private Node root;
    private static final boolean VERTICAL = true;
    private Point2D nearest;

    private static class Node {
        private Point2D p;      // the point
        private RectHV rect;    // the axis-aligned rectangle corresponding to this node
        private Node lb;        // the left/bottom subtree
        private Node rt;        // the right/top subtree

        public Node(Point2D p, double a, double b, double c, double d) {
            this.rect = new RectHV(a, b, c, d);
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
        root = put(root, p, VERTICAL, 0, 0, 1, 1);
    }

    private Node put(Node node, Point2D p, boolean division, double a, double b, double c, double d) {
        if (node == null) {
            n++;
            return new Node(p, a, b, c, d);
        }

        if (p.equals(node.p)) {
            return node;
        }
        if (division == VERTICAL) {
            if (p.x() < node.p.x()) {
                node.lb = put(node.lb, p, !division, node.rect.xmin(), node.rect.ymin(), node.p.x(), node.rect.ymax());
            } else {
                node.rt = put(node.rt, p, !division, node.p.x(), node.rect.ymin(), node.rect.xmax(), node.rect.ymax());
            }
        } else {
            if (p.y() < node.p.y()) {
                node.lb = put(node.lb, p, !division, node.rect.xmin(), node.rect.ymin(), node.rect.xmax(), node.p.y());
            } else {
                node.rt = put(node.rt, p, !division, node.rect.xmin(), node.p.y(), node.rect.xmax(), node.rect.ymax());
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
        draw(root, VERTICAL);
    }

    private void draw(Node node, boolean division) {
        if (node == null) return;
        if (division == VERTICAL) {
            StdDraw.setPenRadius();
            StdDraw.setPenColor(StdDraw.RED);
            StdDraw.line(node.p.x(), node.rect.ymin(), node.p.x(), node.rect.ymax());
            draw(node.lb, !division);
            draw(node.rt, !division);
        } else {
            StdDraw.setPenRadius();
            StdDraw.setPenColor(StdDraw.BLUE);
            StdDraw.line(node.rect.xmin(), node.p.y(), node.rect.xmax(), node.p.y());
            draw(node.lb, !division);
            draw(node.rt, !division);
        }
        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.setPenRadius(0.02);
        node.p.draw();
    }

    // all points that are inside the rectangle (or on the boundary) 
    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) throw new IllegalArgumentException();
        ArrayList<Point2D> allPointsInside = new ArrayList<>();
        find(root, rect, allPointsInside);
        return allPointsInside;
    }

    private void find(Node node, RectHV rect, ArrayList<Point2D> points) {
        if (node == null) return;
        if (!rect.intersects(node.rect)) return;
        if (rect.contains(node.p)) points.add(node.p);
        find(node.lb, rect, points);
        find(node.rt, rect, points);

    }

    // a nearest neighbor in the set to point p; null if the set is empty 
    public Point2D nearest(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        if (root == null) return null;
        nearest = root.p;
        closest(root, p, VERTICAL);
        return nearest;
    }

    private void closest(Node node, Point2D p, boolean division) {
        if (node == null) return;
        if (nearest.distanceSquaredTo(p) < node.rect.distanceSquaredTo(p)) return;
        if (node.p.distanceSquaredTo(p) < nearest.distanceSquaredTo(p)) nearest = node.p;
        if (division == VERTICAL) {
            if (p.x() < node.p.x()) {
                closest(node.lb, p, !division);
                closest(node.rt, p, !division);
            } else {
                closest(node.rt, p, !division);
                closest(node.lb, p, !division);
            }
        } else {
            if (p.y() < node.p.y()) {
                closest(node.lb, p, !division);
                closest(node.rt, p, !division);
            } else {
                closest(node.rt, p, !division);
                closest(node.lb, p, !division);
            }
        }
    }

    // unit testing of the methods (optional) 
    public static void main(String[] args) {
        RectHV r = new RectHV(0, 0, 1, 1);
        StdOut.println(r);
        KdTree set = new KdTree();
        set.insert(new Point2D(0.7, 0.2));
        set.insert(new Point2D(0.5, 0.4));
        set.insert(new Point2D(0.2, 0.3));
        set.insert(new Point2D(0.4, 0.7));
        set.insert(new Point2D(0.9, 0.6));
        
        StdOut.println(set.contains(new Point2D(0.7, 0.2)));
        StdOut.println(set.contains(new Point2D(0.5, 0.4)));
        StdOut.println(set.contains(new Point2D(0.2, 0.3)));
        StdOut.println(set.contains(new Point2D(0.4, 0.7)));
        StdOut.println(set.contains(new Point2D(0.9, 0.6)));
        
        StdOut.println(set.size());
        StdOut.println("================================");
        StdOut.println(set.contains(new Point2D(0.1, 0.1)));
        StdOut.println(set.contains(new Point2D(0.2, 0.2)));
        StdOut.println(set.contains(new Point2D(0.3, 0.3)));
        StdOut.println(set.contains(new Point2D(0.4, 0.4)));
        StdOut.println(set.contains(new Point2D(0.5, 0.5)));

        String filename = "input/input10K.txt";
        if (args.length > 0) filename = args[0];
        In in = new In(filename);
        KdTree kdtree = new KdTree();
        while (!in.isEmpty()) {
            double x = in.readDouble();
            double y = in.readDouble();
            Point2D p = new Point2D(x, y);
            kdtree.insert(p);
        }
        kdtree.draw();

        Point2D p = new Point2D(0.2, 0.2);
        StdOut.println(set.root.p.distanceSquaredTo(p));
        StdOut.println(set.root.rect.distanceSquaredTo(p));
    }
}