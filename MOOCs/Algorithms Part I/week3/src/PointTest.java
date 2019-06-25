import static org.junit.Assert.assertEquals;
import java.util.Arrays;

import org.junit.Test;

import edu.princeton.cs.algs4.StdOut;

public class PointTest {

    @Test
    public void testPoint() {
        Point p = new Point(0, 0);
        assertEquals("(0, 0)", p.toString());
    }

    @Test
    public void testArraySortBySlope() {
        Point a = new Point(0, 0);
        Point b = new Point(5, 1);
        Point c = new Point(3, 1);
        Point d = new Point(1, 1);
        Point e = new Point(1, 3);

        Point[] points = new Point[4];
        points[0] = e;
        points[1] = d;
        points[2] = c;
        points[3] = b;

        assertEquals("(1, 3)", points[0].toString());
        assertEquals("(1, 1)", points[1].toString());
        assertEquals("(3, 1)", points[2].toString());
        assertEquals("(5, 1)", points[3].toString());

        Arrays.sort(points, a.slopeOrder());

        for (Point p : points) {
            StdOut.println(p);
        }

        assertEquals("(5, 1)", points[0].toString());
        assertEquals("(3, 1)", points[1].toString());
        assertEquals("(1, 1)", points[2].toString());
        assertEquals("(1, 3)", points[3].toString());

    }

    @Test
    public void testArraySortBySlope1() {
        Point a = new Point(0, 0);
        Point b = new Point(5, 1);
        Point c = new Point(3, 1);
        Point d = new Point(1, 1);
        Point e = new Point(1, 3);

        Point[] points = new Point[5];
        points[0] = e;
        points[1] = a;
        points[2] = d;
        points[3] = c;
        points[4] = b;

        assertEquals("(1, 3)", points[0].toString());
        assertEquals("(0, 0)", points[1].toString());
        assertEquals("(1, 1)", points[2].toString());
        assertEquals("(3, 1)", points[3].toString());
        assertEquals("(5, 1)", points[4].toString());

        Arrays.sort(points, a.slopeOrder());

        for (Point p : points) {
            StdOut.println(p);
        }

        assertEquals("(0, 0)", points[0].toString());
        assertEquals("(5, 1)", points[1].toString());
        assertEquals("(3, 1)", points[2].toString());
        assertEquals("(1, 1)", points[3].toString());
        assertEquals("(1, 3)", points[4].toString());

    }
}