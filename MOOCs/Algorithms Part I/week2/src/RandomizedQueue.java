import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private int n;
    private Item[] a;

    // construct an empty randomized queue
    public RandomizedQueue() {
        n = 0;
        a = (Item[]) new Object[2];
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return n == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return n;
    }

    // resize the underlying array holding the elements
    private void resize(int capacity) {
        assert capacity >= n;

        // textbook implementation
        Item[] temp = (Item[]) new Object[capacity];
        for (int i = 0; i < n; i++) {
            temp[i] = a[i];
        }
        a = temp;

       // alternative implementation
       // a = java.util.Arrays.copyOf(a, capacity);
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) throw new java.lang.IllegalArgumentException();
        // double size of array if necessary
        if (n == a.length) resize(2*a.length); 
        // add item in the list
        a[n++] = item;

        // Swap last item;
        int r = StdRandom.uniform(n);
        Item temp = a[r];
        a[r] = item;
        a[n - 1] = temp;

        // Swap item with some other rando item in the list;
        // if (n == 0) {
        //     a[n++] = item;
        //     return;
        // }
        // int r = StdRandom.uniform(n);
        // Item temp = a[r];
        // a[r] = item;
        // a[n++] = temp;
    }

    // remove and return a random item
    public Item dequeue() {
        if (isEmpty()) throw new NoSuchElementException();
        Item item = a[n - 1];
        a[n - 1] = null;
        n--;
        // shrink size of array if necessary
        if (n > 0 && n == a.length/4) resize(a.length/2);
        return item;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (isEmpty()) throw new NoSuchElementException();
        return a[StdRandom.uniform(n)];
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new ArrayIterator();
    }

    // an iterator, doesn't implement remove() since it's optional
    private class ArrayIterator implements Iterator<Item> {
        private int i;
        private final Item[] arr;

        public ArrayIterator() {
            i = 0;

            arr = (Item[]) new Object[n]; 
            for (int ii = 0; ii < n; ii++) {
                arr[ii] = a[ii];
            }

            StdRandom.shuffle(arr);
        }

        public boolean hasNext() {
            return i < n;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            return arr[i++];
        }
    }
    public static void main(String[] args) {

        double a = 0;
        double b = 0;
        double c = 0;
        double d = 0;
        double e = 0;


        for (int i = 0; i < 1000000; i++) {
            RandomizedQueue<String> q = new RandomizedQueue<String>();

            q.enqueue("a");
            q.enqueue("b");
            q.enqueue("c");
            q.enqueue("d");
            q.enqueue("e");
            
            String result = q.dequeue();

            if (result.equals("a")) a++;
            if (result.equals("b")) b++;
            if (result.equals("c")) c++;
            if (result.equals("d")) d++;
            if (result.equals("e")) e++;
        }

        System.out.println(a/10000);
        System.out.println(b/10000);
        System.out.println(c/10000);
        System.out.println(d/10000);
        System.out.println(e/10000);

    }
 }