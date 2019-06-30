import java.util.ArrayList;

public class Board {
    private final int[][] blocks;
    private final int n;
    private final int manhattan;

    // create a board from an n-by-n array of tiles,
    // where tiles[row][col] = tile at (row, col)
    public Board(int[][] tiles) {
        n = tiles.length;
        blocks = copy2dArray(tiles);
        manhattan = man();
    }

    private int[][] copy2dArray(int[][] a) {
        int[][] copy = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                copy[i][j] = a[i][j];
            }
        }
        return copy;
    }

    private int man() {
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int tile = blocks[i][j];
                if (tile != 0) {
                    result += distanceToGoal(tile, i, j);
                }
            }
        }
        return result;
    }

    private int distanceToGoal(int tile, int i, int j) {
        int iGoal = (tile - 1) / n;
        int jGoal = (tile - 1) % n;
        return Math.abs(i - iGoal) + Math.abs(j - jGoal);
    }

    // string representation of this board
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append(n + "\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                s.append(String.format("%2d ", blocks[i][j]));
            }
            s.append("\n");
        }
        return s.toString();
    }

    // board dimension n
    public int dimension() {
        return n;
    }

    // number of tiles out of place
    public int hamming() {
        int result = 0;
        int count = 1;
        for (int[] line : blocks) {
            for (int tile : line) {
                if (!(tile == count++) && (tile != 0))
                    result++;
            }
        }
        return result;
    }

    // sum of Manhattan distances between tiles and goal
    public int manhattan() {
        return this.manhattan;
    }

    // is this board the goal board?
    public boolean isGoal() {
        return this.manhattan == 0;
    }

    // does this board equal y?
    public boolean equals(Object y) {
        if (y == this)
            return true;
        if (y == null)
            return false;
        if (y.getClass() != this.getClass())
            return false;

        Board that = (Board) y;

        if (this.dimension() != that.dimension())
            return false;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (this.blocks[i][j] != that.blocks[i][j])
                    return false;
            }
        }
        return true;
    }

    // all neighboring boards
    public Iterable<Board> neighbors() {
        ArrayList<Board> neighbors = new ArrayList<Board>();

        int iZero = 0;
        int jZero = 0;
        boolean foundZero = false;
        outherloop: for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (blocks[i][j] == 0) {
                    foundZero = true;
                    iZero = i;
                    jZero = j;
                    break outherloop;
                }
            }
        }

        assert foundZero;

        addNeighbor(iZero, jZero, iZero + 1, jZero, neighbors);
        addNeighbor(iZero, jZero, iZero, jZero + 1, neighbors);
        addNeighbor(iZero, jZero, iZero - 1, jZero, neighbors);
        addNeighbor(iZero, jZero, iZero, jZero - 1, neighbors);

        return neighbors;
    }

    private void addNeighbor(int iFrom, int jFrom, int iTo, int jTo, ArrayList<Board> neighbors) {
        if ((iTo < 0) || (jTo < 0) || (iTo >= n) || (jTo >= n))
            return;
        int[][] neighborBlocks = copy2dArray(blocks);
        swap(iFrom, jFrom, iTo, jTo, neighborBlocks);
        neighbors.add(new Board(neighborBlocks));
    }

    private void swap(int iFrom, int jFrom, int iTo, int jTo, int[][] a) {
        int temp = a[iFrom][jFrom];
        a[iFrom][jFrom] = a[iTo][jTo];
        a[iTo][jTo] = temp;
    }

    // a board that is obtained by exchanging any pair of blocks
    public Board twin() {
        if (n <= 1)
            throw new IllegalArgumentException("size 1 board don't have twin");
        int[][] twinBolocks = copy2dArray(blocks);
        if (zeroInFirstTwo()) {
            swap(1, 0, 1, 1, twinBolocks);
        } else {
            swap(0, 0, 0, 1, twinBolocks);
        }
        return new Board(twinBolocks);
    }

    private boolean zeroInFirstTwo() {
        for (int j = 0; j < 2; j++) {
            if (blocks[0][j] == 0)
                return true;
        }
        return false;
    }

    // unit testing (not graded)
    public static void main(String[] args) {
        int[][] blocks = { { 8, 1, 3 }, { 4, 0, 2 }, { 7, 6, 5 } };
        Board b = new Board(blocks);
        System.out.println(b.toString());

        for (Board neighbor : b.neighbors()) {
            System.out.println(neighbor.toString());
        }
    }

}