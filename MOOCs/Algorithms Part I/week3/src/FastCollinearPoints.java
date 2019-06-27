import java.util.Arrays;
import java.util.ArrayList;


public class FastCollinearPoints {
    private int nOfSegments;
    private ArrayList<LineSegment> segments;
    private ArrayList<Double> segmentsSlopes;
    // finds all line segments containing 4 points
    public FastCollinearPoints(Point[] points) {
        if (invalid(points)) throw new java.lang.IllegalArgumentException();
        nOfSegments = 0;
        segments = new ArrayList<>();
        segmentsSlopes = new ArrayList<>();
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
        boolean findCollinear = false;
        Point p = reordedPoins[0];
        for (int i = 3; i < reordedPoins.length; i++) {
            Point q = reordedPoins[i - 2];
            Point r = reordedPoins[i - 1];
            Point s = reordedPoins[i];
            Point last = null;
            while (isCollinear(p, q, r, s) && i < reordedPoins.length) {
                last = s;
                i++;
                if (i < reordedPoins.length) s = reordedPoins[i];
                findCollinear = true;
            }

            if (findCollinear) {
                findCollinear = false;
                if (!segmentsSlopes.contains(p.slopeTo(last))) {
                    segments.add(new LineSegment(p, last));
                    segmentsSlopes.add(p.slopeTo(last));
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
        for (int i = 0; i <= n - 2; i++) {
            if (points[i] == null) return true;
            for (int j = i + 1; j <= n - 1; j++) {
                if (points[j] == null) return true;
                if (points[i] == points[j]) return true;
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