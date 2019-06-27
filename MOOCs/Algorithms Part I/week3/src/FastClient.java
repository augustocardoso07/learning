import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class FastClient {
    public static void main(String[] args) {
        String file = "input/input8.txt";
        if (args.length > 0) file = args[0];
        In in = new In(file);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(-100, 32768);
        StdDraw.setYscale(-100, 32768);
        StdDraw.setPenRadius(0.01);
        
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        StdDraw.setPenRadius(0.005);
        StdDraw.setPenColor(StdDraw.MAGENTA);
        int red = 0;
        int green = 0;
        int blue = 0;
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
            StdDraw.show();
            StdDraw.pause(2000);
            StdDraw.setPenColor(red % 255, green % 255, blue % 255);
            red += 170;
            green += 31;
            blue += 41;
        }
        
    }
}