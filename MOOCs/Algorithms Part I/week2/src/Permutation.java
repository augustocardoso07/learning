import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class Permutation {
    public static void main(String[] args) {
        int k = 0; 
        if (args.length == 1) {
            k = Integer.parseInt(args[0]);
        }

        RandomizedQueue<String> q = new RandomizedQueue<String>();

        double i = 0;
        while (!StdIn.isEmpty() && k != 0) {
            String word = StdIn.readString();
            if (q.size() == k) {
                i++;
                double p = StdRandom.uniform();
                if (p <= k/(k + i)) {
                    q.dequeue();
                    q.enqueue(word);
                }
            } else {
                q.enqueue(word);
            }

        }

        for (String var : q) {
            StdOut.println(var);
        }
    }
 }