import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Stack;

public class Solver {

    private final int moves;
    private final boolean isSolvable;
    private final Stack<Board> path = new Stack<>();

    private class Node implements Comparable<Node> {
        private final int priority;
        private final Board board;
        private final Node previus;
        private final int man;
        private final boolean goal;
        private final int moves;

        public Node(Board b, int moves, Node previus) {
            this.board = b;
            this.man = b.manhattan();
            this.priority = man + moves;
            this.previus = previus;
            this.goal = b.isGoal();
            this.moves = moves;
        }

        public int compareTo(Node that) {
            if (this.priority < that.priority)
                return -1;
            if (this.priority > that.priority)
                return 1;
            if (this.man < that.man)
                return -1;
            if (this.man > that.man)
                return 1;
            return 0;
        }

    }

    public Solver(Board initial) {
        if (initial == null)
            throw new IllegalArgumentException();
        Node init = new Node(initial, 0, null);
        Node twin = new Node(initial.twin(), 0, null);

        MinPQ<Node> pq1 = new MinPQ<>();
        MinPQ<Node> pq2 = new MinPQ<>();

        boolean tempIsSolvable = false;
        while (true) {
            if (init.goal) {
                tempIsSolvable = true;
                break;
            }
            if (twin.goal) {
                break;
            }

            for (Board neib : init.board.neighbors()) {
                if (init.previus != null && init.previus.board.equals(neib))
                    continue;
                pq1.insert(new Node(neib, init.moves + 1, init));
            }

            init = pq1.delMin();

            for (Board neib : twin.board.neighbors()) {
                if (twin.previus != null && twin.previus.board.equals(neib))
                    continue;
                pq2.insert(new Node(neib, twin.moves + 1, twin));
            }

            twin = pq2.delMin();
        }

        int tempMoves = -1;
        if (tempIsSolvable) {
            while (init != null) {
                path.push(init.board);
                init = init.previus;
                tempMoves++;
            }
        }
        isSolvable = tempIsSolvable;
        moves = tempMoves;

    }

    public boolean isSolvable() {
        return isSolvable;
    }

    public int moves() {
        return moves;
    }

    public Iterable<Board> solution() {
        if (!isSolvable())
            return null;
        return path;
    }

    public static void main(String[] args) {
        // create initial board from file
        String file = "input/puzzle3x3-unsolvable.txt";
        if (args.length > 0)
            file = args[0];
        In in = new In(file);
        int n = in.readInt();
        int[][] blocks = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
        StdOut.println("Moves =>> " + solver.moves());

        /*
         * int[][] blocks = { {1, 2}, {3, 0} };
         * 
         * Board b = new Board(blocks); Solver s = new Solver(b);
         * StdOut.println("1: true  = " + s.isSolvable()); StdOut.println("2: 0     = "
         * + s.moves());
         * 
         * int[][] blocks2 = { {2, 1}, {3, 0} };
         * 
         * for (Board p : s.solution()) { StdOut.println(p); }
         * 
         * b = new Board(blocks2); s = new Solver(b); StdOut.println("3: false  = " +
         * s.isSolvable()); StdOut.println("4: -1     = " + s.moves());
         * 
         * StdOut.println("-------------------------------");
         * 
         * int[][] blocks3 = { {1, 2}, {0, 3} };
         * 
         * b = new Board(blocks3); s = new Solver(b); StdOut.println("5: true  = " +
         * s.isSolvable()); StdOut.println("6: 1     = " + s.moves());
         * 
         * StdOut.println("Solution:"); for (Board p : s.solution()) {
         * StdOut.println(p); }
         */

    }
}