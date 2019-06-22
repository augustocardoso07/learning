import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private int n;
    private Node first;
    private Node last;

    // helper linked list data
    private class Node {
        private Item item;
        private Node next;
        private Node previus;
    }
    // construct an empty deque

    public Deque() {
        n = 0;
        first = null;
        last = null;
    }

    // is the deque empty?
    public boolean isEmpty() {
        return n == 0;
    }

    // return the number of items on the deque
    public int size() {
        return n;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null)
            throw new java.lang.IllegalArgumentException();

        Node newFirst = new Node();
        newFirst.item = item;
        newFirst.next = first;
        if (first != null)
            first.previus = newFirst;
        first = newFirst;
        if (isEmpty())
            last = first;
        n++;
    }

    // add the item to the end
    public void addLast(Item item) {
        if (item == null)
            throw new java.lang.IllegalArgumentException();

        Node newLast = new Node();
        newLast.item = item;
        newLast.previus = last;
        if (last != null)
            last.next = newLast;
        last = newLast;
        if (isEmpty())
            first = last;
        n++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty())
            throw new NoSuchElementException();
        Item item = first.item;
        Node newFirst = first.next;
        if (newFirst != null)
            newFirst.previus = null;
        first = newFirst;
        n--;
        if (isEmpty()) {
            first = null;
            last = null;
        }
        return item;
    }

    // remove and return the item from the end
    public Item removeLast() {
        if (isEmpty())
            throw new NoSuchElementException();
        Item item = last.item;
        Node newLast = last.previus;
        if (newLast != null)
            newLast.next = null;
        last = newLast;
        n--;
        if (isEmpty()) {
            first = null;
            last = null;
        }
        return item;
    }

    // return an iterator over items in order from front to end
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    // an iterator, doesn't implement remove() since it's optional
    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext())
                throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    // unit testing (optional)
    public static void main(String[] args) {
        Deque<Integer> d = new Deque<Integer>();
        
        d.addFirst(1);
        d.removeLast();

        System.out.println("Tamanho do Deque: " + d.size());
        for (Integer var : d) {
            System.out.println(var);
        }

    }
}