import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class Permutation {
    public static void main(String[] args) {
        int k = 1; // number of particles (default 20)
        if (args.length == 1) {
            k = Integer.parseInt(args[0]);
        }

        RandomizedQueue<String> q = new RandomizedQueue<String>();

        int n = 0;
        while (StdIn.isEmpty()) {
            String word = StdIn.readString();
            n++;
            if (q.size() == k) {
                Double p = StdRandom.uniform();
                if (p > 1/n) {
                    q.dequeue();
                    q.enqueue(word);
                }
            } else {
                q.enqueue(word);
            }

        }

        for (int i = 0; i < k; i++) {
            StdOut.println(q.dequeue());
        }
    }
 }