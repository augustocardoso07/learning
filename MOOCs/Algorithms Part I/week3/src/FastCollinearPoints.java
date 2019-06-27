import java.util.Arrays;

import edu.princeton.cs.algs4.StdDraw;

import java.util.ArrayList;


public class FastCollinearPoints {
    private final int nOfSegments;
    private final ArrayList<LineSegment> segments;
    // finds all line segments containing 4 points
    public FastCollinearPoints(Point[] points) {
        if (invalid(points)) throw new java.lang.IllegalArgumentException();
        nOfSegments = 0;
        segments = new ArrayList<>();
        int n = points.length;

        Arrays.sort(points);
        for (Point p : points) {
            Point[] reordedPoins = Arrays.copyOf(points, n);
            Arrays.sort(reordedPoins);
            Arrays.sort(reordedPoins, p.slopeOrder());
            checkSlope(reordedPoins);
        }
    }

    private void checkSlope(Point[] reordedPoins) {
        boolean findCollinear;
        Point p = reordedPoins[0];
        for (int i = 3; i < reordedPoins.length; i++) {
            Point q = reordedPoins[i - 2];
            Point r = reordedPoins[i - 1];
            Point s = reordedPoins[i];
            Point last = null;
            findCollinear = false;
            while (isCollinear(p, q, r, s) && i < reordedPoins.length) {
                last = s;
                i++;
                if (i < reordedPoins.length) s = reordedPoins[i];
                findCollinear = true;
            }

            if (findCollinear) {
                LineSegment line = new LineSegment(p, last);
                LineSegment reverseLine = new LineSegment(last, p);
                if (!segments.contains(line) && !segments.contains(reverseLine)) {
                    int test = 0;
                    segments.add(line);
                    line.draw();
                    StdDraw.show();
                } 
            }
        }


    }

    private boolean isCollinear(Point p, Point q, Point r, Point s) {
        return p.slopeTo(q) == q.slopeTo(r) && p.slopeTo(r) == r.slopeTo(s);
    }

    private boolean invalid(Point[] points) {
        if (points == null) return true;
        int n = points.length;
        if (points[0] == null) return true;
        for (int i = 0; i <= n - 2; i++) {
            if (points[i] == null) return true;
            for (int j = i + 1; j <= n - 1; j++) {
                if (points[j] == null) return true;
                if (points[i].compareTo(points[j]) == 0) return true;
            }
        }
        return false;
    }

    // the number of line segments
    public int numberOfSegments() {
        return nOfSegments;
    }

    // the line segments
    public LineSegment[] segments() {
        return segments.toArray(new LineSegment[segments.size()]);
    }
 }