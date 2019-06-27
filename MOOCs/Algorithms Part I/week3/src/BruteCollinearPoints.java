import java.util.Arrays;
import java.util.ArrayList;


public class BruteCollinearPoints {
    private int nOfSegments;
    private final ArrayList<LineSegment> segments;
    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points) {
        if (invalide(points)) throw new java.lang.IllegalArgumentException();
        nOfSegments = 0;
        segments = new ArrayList<>();
        int n = points.length;
        for (int i = 0; i <= n - 4; i++) {
            for (int j = i + 1; j <= n - 3; j++) {
                for (int k = j + 1; k <= n - 2; k++) {
                    if (isCollinear(points[i], points[j], points[k])) {
                        for (int l = k + 1; l <= n - 1; l++) {
                            if (isCollinear(points[i], points[j], points[l])) {
                                Point[] collinearPoints = {points[i], points[j], points[k], points[l]};
                                Arrays.sort(collinearPoints);
                                Point mim = collinearPoints[0];
                                Point max = collinearPoints[3];
                                LineSegment line = new LineSegment(mim, max);
                                nOfSegments++;
                                segments.add(line);
                            }
                        }
                    }
                }
            }
        }
    }

    private boolean isCollinear(Point p, Point q, Point r) {
        return p.slopeTo(q) == q.slopeTo(r);
    }

    private boolean invalide(Point[] points) {
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