import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private enum Status { CLOSE, OPEN, CONECT_TO_TOP, CONECT_TO_BOTTOM};
    private static final byte CLOSE = 0;
    private static final byte OPEN = 1;
    private static final byte CONECT_TO_TOP = 2;
    private static final byte CONECT_TO_BOTTOM = 4;
    private static final byte OPEN_AND_CONECT_TO_TOP = OPEN | CONECT_TO_TOP;
    private static final byte OPEN_AND_CONECT_TO_BOTTOM = OPEN | CONECT_TO_BOTTOM;
    private static final byte PERCOLATION = OPEN_AND_CONECT_TO_TOP | OPEN_AND_CONECT_TO_BOTTOM;
    private final int n;
    private final WeightedQuickUnionUF uf;
    private byte[] arr;
    private int nOfOpenSites = 0;
    private boolean perco = false;


    public Percolation(int n) { 
        if (n <= 0) throw new java.lang.IllegalArgumentException();
        uf = new WeightedQuickUnionUF(n * n);
        arr = new byte[n * n];
        this.n = n;
        for (int i = 0; i < n * n; i++) {
            arr[i] = CLOSE;
        }
    }
    
    private int xyTo1d(int row, int col) {
        return ((row - 1) * this.n) + col - 1;
    }

    private void throwExceptionIfNotValid(int row, int col) {
        if (!isValid(row, col)) throw new java.lang.IllegalArgumentException();
    }

    public void open(int row, int col) {
        throwExceptionIfNotValid(row, col);
        if (isOpen(row, col)) return;
        nOfOpenSites++;

        byte status1 = CLOSE;
        byte status2 = CLOSE;
        byte status3 = CLOSE;
        byte status4 = CLOSE;

        int site = xyTo1d(row, col);

        if (isValid(row - 1, col) && isOpen(row - 1, col)) {
            int neib = xyTo1d(row - 1, col);
            status1 = arr[uf.find(neib)];
            uf.union(site, neib);
        }
        if (isValid(row + 1, col) && isOpen(row + 1, col)) {
            int neib = xyTo1d(row + 1, col);
            status2 = arr[uf.find(neib)];
            uf.union(site, neib);
        }
        if (isValid(row, col - 1) && isOpen(row, col - 1)) {
            int neib = xyTo1d(row, col - 1);
            status3 = arr[uf.find(neib)];
            uf.union(site, neib);
        }
        if (isValid(row, col + 1) && isOpen(row, col + 1)) {
            int neib = xyTo1d(row, col + 1);
            status4 = arr[uf.find(neib)];
            uf.union(site, neib);
        }

        byte result = (byte) (status1 | status2 | status3 | status4 | OPEN);

        if (row == 1) result = (byte) (result | CONECT_TO_TOP);
        if (row == this.n) result = (byte) (result | CONECT_TO_BOTTOM);

        if (result == PERCOLATION) {
            result = OPEN_AND_CONECT_TO_TOP;
            perco = true;
        }
        arr[uf.find(site)] = result;
        arr[site] = result;
    }

    private boolean isValid(int row, int col) {
        return (row >= 1 && col >= 1 && row <= this.n && col <= this.n);
    }

    public boolean isOpen(int row, int col) {
        throwExceptionIfNotValid(row, col);
        return arr[xyTo1d(row, col)] >= 1;
    }

    public boolean isFull(int row, int col) {
        throwExceptionIfNotValid(row, col);
        int status = arr[uf.find(xyTo1d(row, col))];
        return status == OPEN_AND_CONECT_TO_TOP;
    }

    public int numberOfOpenSites() {
        return nOfOpenSites;
    }

    public boolean percolates() {
        return perco;
    }
 
    public static void main(String[] args) {
        Percolation p = new Percolation(3);
        System.out.println(p.percolates());
        p.open(1, 1);
        p.open(2, 1);
        p.open(3, 1);
        p.open(1, 2);
        p.open(3, 3);
        System.out.println(p.percolates());

    }
 }