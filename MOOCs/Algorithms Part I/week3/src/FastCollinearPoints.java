import java.util.Arrays;

import edu.princeton.cs.algs4.StdDraw;

import java.util.ArrayList;


public class FastCollinearPoints {
    private final int nOfSegments;
    private final ArrayList<LineSegment> segments;
    // finds all line segments containing 4 points
    public FastCollinearPoints(Point[] points) {
        if (invalid(points)) throw new java.lang.IllegalArgumentException();
        segments = new ArrayList<>();
        
        for (Point p : points) {
            Arrays.sort(points, p.slopeOrder());
            checkSlope(points);
        }
        nOfSegments = segments.size();
    }

    private void checkSlope(Point[] reordedPoins) {
        boolean findCollinear;
        Point p = reordedPoins[0];
        int i = 3;
        Point q, r, s;
        Point start = new Point(Integer.MAX_VALUE, Integer.MAX_VALUE);
        Point end = new Point(Integer.MIN_VALUE, Integer.MIN_VALUE);
        while (i < reordedPoins.length) {
            q = reordedPoins[i - 2];
            r = reordedPoins[i - 1];
            s = reordedPoins[i];
            findCollinear = false;
            while (isCollinear(p, q, r, s) && i < reordedPoins.length) {
                start = mimPoint(p, q, r, s, start);
                end = maxPoint(p, q, r, s, end);
                i++;
                if (i < reordedPoins.length) s = reordedPoins[i];
                findCollinear = true;
            }

            if (findCollinear) {
                LineSegment line = new LineSegment(start, end);
                if (lineNotIn(segments, line)) {
                    segments.add(line);
                    line.draw();
                    StdDraw.show();
                }
            } else {
                i++;
            }
        }
    }

    private boolean lineNotIn(ArrayList<LineSegment> segments, LineSegment line) {
        for (LineSegment seg : segments) {
            if (seg.toString().equals(line.toString())) return false;
        }
        return true;
    }

    private Point maxPoint(Point p, Point q, Point r, Point s, Point t) {
        return maxMimPoint(p, q, r, s, t, true);
    }

    private Point maxPoint(Point p, Point q) {
        if (p.compareTo(q) > 0) {
            return p;
        } else {
            return q;
        }
    }

    private Point mimPoint(Point p, Point q, Point r, Point s, Point t) {
        return maxMimPoint(p, q, r, s, t, false);
    }

    private Point mimPoint(Point p, Point q) {
        if (p.compareTo(q) < 0) {
            return p;
        } else {
            return q;
        }
    }

    private Point maxMimPoint(Point p, Point q, Point r, Point s, Point t, boolean max) {
        Point[] a = {p, q, r, s, t};
        Arrays.sort(a);
        if (max) return a[4];
        return a[0];
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