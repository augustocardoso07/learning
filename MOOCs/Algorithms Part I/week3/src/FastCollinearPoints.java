import java.util.Arrays;
import java.util.ArrayList;


public class FastCollinearPoints {
    private final int nOfSegments;
    private final ArrayList<LineSegment> segments;
    // finds all line segments containing 4 points
    public FastCollinearPoints(Point[] points) {
        if (invalid(points)) throw new IllegalArgumentException();
        segments = new ArrayList<>();
        
        Arrays.sort(points);
        Point[] reordedPoins = Arrays.copyOf(points, points.length);
        for (Point p : points) {
            Arrays.sort(reordedPoins);
            Arrays.sort(reordedPoins, p.slopeOrder());
            checkSlope(reordedPoins);
        }
        nOfSegments = segments.size();
    }

    private void checkSlope(Point[] reordedPoins) {
        boolean findCollinear;
        Point p = reordedPoins[0];
        int i = 3;
        Point q, r, s, last;
        while (i < reordedPoins.length) {
            q = reordedPoins[i - 2];
            r = reordedPoins[i - 1];
            s = reordedPoins[i];
            findCollinear = false;
            last = null;
            while (isCollinear(p, q, r, s) && i < reordedPoins.length) {
                last = s;
                i += 1;
                if (i < reordedPoins.length) s = reordedPoins[i];
                findCollinear = true;
            }

            if (findCollinear && p.compareTo(q) < 0) {
                LineSegment line = new LineSegment(p, last);
                segments.add(line);
            } else {
                i++;
            }
        }
    }

    private boolean isCollinear(Point p, Point q, Point r, Point s) {
        double slope = p.slopeTo(q);
        return slope == q.slopeTo(r) && r.slopeTo(s) == slope;
        // return p.slopeTo(q) == q.slopeTo(r) && p.slopeTo(r) == r.slopeTo(s);
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