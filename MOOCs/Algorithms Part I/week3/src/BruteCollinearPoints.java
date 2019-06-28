import java.util.Arrays;
import java.util.ArrayList;


public class BruteCollinearPoints {
    private final int nOfSegments;
    private final ArrayList<LineSegment> segments;
    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points) {
        if (invalide(points)) throw new IllegalArgumentException();
        int count = 0;
        segments = new ArrayList<>();
        int n = points.length;
        for (int i = 0; i <= n - 4; i++) {
            for (int j = i + 1; j <= n - 3; j++) {
                for (int k = j + 1; k <= n - 2; k++) {
                    if (isCollinear(points[i], points[j], points[k])) {
                        for (int m = k + 1; m <= n - 1; m++) {
                            if (isCollinear(points[i], points[j], points[m])) {
                                Point[] collinearPoints = {points[i], points[j], points[k], points[m]};
                                Arrays.sort(collinearPoints);
                                Point start = collinearPoints[0];
                                Point end = collinearPoints[3];
                                LineSegment line = new LineSegment(start, end);
                                count++;
                                segments.add(line);
                            }
                        }
                    }
                }
            }
        }
        nOfSegments = count;
    }

    private boolean isCollinear(Point p, Point q, Point r) {
        return p.slopeTo(q) == q.slopeTo(r);
    }

    private boolean invalide(Point[] points) {
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