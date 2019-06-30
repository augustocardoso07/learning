import static org.junit.Assert.assertEquals;
import org.junit.Test;

// usage for Coursera Algorithms I
// javac-algs4 -cp .:junit-4.12.jar BoardTest.java
// java-algs4 -cp .:junit-4.12.jar:hamcrest-core-1.3.jar org.junit.runner.JUnitCore BoardTest
// Is not necessary compile Board.java for test BoardTest,
//      I think that junit compile Board.java automatic

public class BoardTest {
    
    @Test
    public void evaluatesExpression() {
        assertEquals(6, 6);
    }

    @Test
    public void dimensionTest() {
        Board b = new Board(new int[3][3]);
        assertEquals(b.dimension(), 3);
    }

    @Test
    public void hammingExist() {
        int[][] blocks = {
                           {1, 2, 3},
                           {4, 5, 6},
                           {7, 8, 0}
                         };
        Board b = new Board(blocks);
        assertEquals(0, b.hamming());
    }

    @Test
    public void hammingCompute() {
        int[][] blocks = {
                           {1, 2, 3},
                           {4, 5, 6},
                           {7, 0, 8}
                         };
        Board b = new Board(blocks);
        assertEquals(1, b.hamming());
    }

    @Test
    public void hammingAllWrong() {
        int[][] blocks = {
                           {0, 3, 6},
                           {1, 4, 7},
                           {2, 5, 8}
                         };
        Board b = new Board(blocks);
        assertEquals(8, b.hamming());
    }

    @Test
    public void hammingFirst0() {
        int[][] blocks = {
                           {0, 1, 2},
                           {3, 4, 5},
                           {6, 7, 8}
                         };
        Board b = new Board(blocks);
        assertEquals(8, b.hamming());
    }

    @Test
    public void hammingMiddle0() {
        int[][] blocks = {
                           {4, 1, 2},
                           {3, 0, 5},
                           {6, 7, 8}
                         };
        Board b = new Board(blocks);
        assertEquals(8, b.hamming());
    }

    @Test
    public void hammingMiddle0with3moves() {
        int[][] blocks = {
                           {1, 2, 3},
                           {4, 0, 6},
                           {7, 5, 8}
                         };
        Board b = new Board(blocks);
        assertEquals(2, b.hamming());
    }

    @Test
    public void isGoalFalse3n() {
        int[][] blocks = {
                           {1, 2, 3},
                           {4, 5, 6},
                           {7, 0, 8}
                         };
        Board b = new Board(blocks);
        assertEquals(false, b.isGoal());
    }

    @Test
    public void isGoalTrue3n() {
        int[][] blocks = {
                           {1, 2, 3},
                           {4, 5, 6},
                           {7, 8, 0}
                         };
        Board b = new Board(blocks);
        assertEquals(true, b.isGoal());
    }

    @Test
    public void isGoalTrue3nwith0first() {
        int[][] blocks = {
                           {0, 2, 3},
                           {4, 5, 6},
                           {7, 8, 1}
                         };
        Board b = new Board(blocks);
        assertEquals(false, b.isGoal());
    }

    @Test
    public void manhattan10() {
        int[][] blocks = {
                           {8, 1, 3},
                           {4, 0, 2},
                           {7, 6, 5}
                         };
        Board b = new Board(blocks);
        assertEquals(10, b.manhattan());
    }

    @Test
    public void manhattan2() {
        int[][] blocks = {
                           {1, 2},
                           {0, 3},
                         };
        Board b = new Board(blocks);
        assertEquals(1, b.manhattan());
    }

    @Test
    public void twin() {
        int[][] blocks = {
                           {1, 2},
                           {0, 3},
                         };
        Board b = new Board(blocks);
        int[][] blocks2 = {
                           {2, 1},
                           {0, 3},
                         };
        Board b2 = new Board(blocks2);

        assertEquals(b2, b.twin());
    }

    @Test
    public void twin2() {
        int[][] blocks = {
                           {0, 2},
                           {1, 3},
                         };
        Board b = new Board(blocks);
        int[][] blocks2 = {
                           {0, 2},
                           {3, 1},
                         };
        Board b2 = new Board(blocks2);

        assertEquals(b2, b.twin());
    }
}