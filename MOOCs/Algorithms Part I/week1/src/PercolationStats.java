import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private static final double C = 1.96;
    private final double[] experimentScores;
    private final double mMean, mStd;

    public PercolationStats(int n, int trials) {
        int row, col;
        int i;

        if (n <= 0 || trials <= 0) throw new IllegalArgumentException();

        experimentScores = new double[trials];
        for (i = 0; i < trials; i++) {
            Percolation p = new Percolation(n);
            while (!p.percolates()) {
                row = StdRandom.uniform(1, n + 1);
                col = StdRandom.uniform(1, n + 1);
                p.open(row, col);
            }
            experimentScores[i] = 1.0 * p.numberOfOpenSites() / (n * n);
        }

        mMean = StdStats.mean(experimentScores);
        mStd = StdStats.stddev(experimentScores);
    }

    public double mean() {
        return mMean;
    }

    public double stddev() {
        return mStd;
    }

    public double confidenceLo() {
        return mean() - C * stddev() / Math.sqrt(experimentScores.length);
    }

    public double confidenceHi() {
        return mean() + C * stddev() / Math.sqrt(experimentScores.length);
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int t = Integer.parseInt(args[1]);
        PercolationStats percolationStats = new PercolationStats(n, t);

        StdOut.printf("mean                    = %f\n", percolationStats.mean());
        StdOut.printf("stddev                  = %f\n", percolationStats.stddev());
        StdOut.println("95% confidence interval = " + percolationStats.confidenceLo() + ", " + percolationStats.confidenceHi());
    }
}