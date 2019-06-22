import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Permutation {
    public static void main(String[] args) {
        int k = 1; // number of particles (default 20)
        if (args.length == 1) {
            k = Integer.parseInt(args[0]);
        }

        RandomizedQueue<String> q = new RandomizedQueue<String>();

        boolean s = StdIn.isEmpty();
        while (!s) {
            q.enqueue(StdIn.readString());
            s = StdIn.isEmpty();
        }

        for (int i = 0; i < k; i++) {
            StdOut.println(q.dequeue());
        }
    }
 }