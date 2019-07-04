import java.util.ArrayList;

import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class KdTree {
    private static final boolean VERTICAL = true;
    private int n;
    private Node root;
    private Point2D nearest;

    private static class Node {
        private final Point2D p;      // the point
        private final RectHV rect;    // the axis-aligned rectangle corresponding to this node
        private Node lb;        // the left/bottom subtree
        private Node rt;        // the right/top subtree

        public Node(Point2D p, double a, double b, double c, double d) {
            this.rect = new RectHV(a, b, c, d);
            this.p = p;
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
                if (p.y() == node.p.y()) {
                    return true;
                } else {
                    return get(node.rt, p, !division);
                }
            }
        } else {
            if (p.y() < node.p.y()) {
                return get(node.lb, p, !division);
            } else if (p.y() > node.p.y()) {
                return get(node.rt, p, !division);
            } else {
                if (p.x() == node.p.x()) {
                    return true;
                } else {
                    return get(node.rt, p, !division);
                }
            }
        }
    }

    // draw all points to standard draw 
    public void draw() {
        draw(root, VERTICAL);
    }

    private void draw(Node node, boolean division) {
        if (node == null) return;

        StdDraw.setPenColor(StdDraw.BLACK);
        // StdDraw.setPenRadius(0.02);
        node.p.draw();
        // StdDraw.pause(2000);
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
        // Point2D a = new Point2D(0.75, 0.5);
        // Point2D b = new Point2D(1.0, 0.25);
        // Point2D c = new Point2D(0.75, 0.75);
        // Point2D d = new Point2D(1.0, 1.0);
        // Point2D e = new Point2D(0.5, 0.0);
        // Point2D f = new Point2D(0.25, 0.0);
        // Point2D g = new Point2D(0.0, 0.75);
        // Point2D h = new Point2D(0.25, 1.0);
        // Point2D i = new Point2D(0.5, 0.75);
        // Point2D j = new Point2D(0.5, 0.5);

        Point2D a1 = new Point2D(0.0, 0.75);
        Point2D b1 = new Point2D(0.75, 1.0);
        Point2D c1 = new Point2D(0.5, 1.0);
        Point2D d1 = new Point2D(0.0, 0.5);
        Point2D e1 = new Point2D(1.0, 0.5);
        Point2D f1 = new Point2D(0.5, 0.25);
        Point2D g1 = new Point2D(0.5, 0.75);
        Point2D h1 = new Point2D(1.0, 0.25);
        Point2D i1 = new Point2D(1.0, 0.75);
        Point2D j1 = new Point2D(0.5, 0.0);
        
        KdTree set = new KdTree();
        set.insert(a1);
        set.insert(b1);
        set.insert(c1);
        set.insert(d1);
        set.insert(e1);
        set.insert(f1);
        set.insert(g1);
        set.insert(h1);
        set.insert(i1);
        set.insert(j1);
        // set.draw();
        
        StdOut.println(set.contains(c1));

    }
}