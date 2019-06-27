import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class BruteClient {
    public static void main(String[] args) {
        String file = "input/input1000.txt";
        if (args.length > 0) file = args[0];
        In in = new In(file);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        

        for (Point p : points) {
            p.draw();
            StdOut.println(p);
        }

        StdDraw.show();

        BruteCollinearPoints collinearPoints = new BruteCollinearPoints(points);

        for (LineSegment line : collinearPoints.segments()) {
            line.draw();
            StdOut.println(line);
        }

        StdDraw.show();
    }
}