import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class DequeTest {

    @Test
    public void testEmptyDeque() {
        Deque<Integer> d = new Deque<Integer>();
        assertEquals(0, d.size());
        assertTrue(d.isEmpty());
    }

    @Test
    public void testSizeWithAddFirst() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(1);
        assertEquals(1, d.size());
        assertFalse(d.isEmpty());
    }

    @Test
    public void testSizeWithAddLast() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(1);
        assertEquals(1, d.size());
        assertFalse(d.isEmpty());
    }

    @Test
    public void testSizeWithAddFirstAndRemove() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(1);
        d.removeFirst();
        assertEquals(0, d.size());
        assertTrue(d.isEmpty());
    }

    @Test
    public void testSizeWithAddLastAndRemove() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(1);
        d.removeLast();
        assertEquals(0, d.size());
        assertTrue(d.isEmpty());
    }

    @Test
    public void testSizeWithAddFirstAndRemoveInv() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(1);
        d.removeLast();
        assertEquals(0, d.size());
        assertTrue(d.isEmpty());
    }

    @Test
    public void testSizeWithAddLastAndRemoveInv() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(1);
        d.removeFirst();
        assertEquals(0, d.size());
        assertTrue(d.isEmpty());
    }

    @Test
    public void test1000AddFirst() {
        Deque<Integer> d = new Deque<Integer>();
        for (int i = 0; i < 1000; i++) {
            d.addFirst(i);
        }

        assertEquals(1000, d.size());

        for (int i = 0; i < 1000; i++) {
            Integer r = i;
            assertEquals(r, d.removeLast());
        }

        assertEquals(0, d.size());
    }

    @Test
    public void test1000AddLast() {
        Deque<Integer> d = new Deque<Integer>();
        for (int i = 0; i < 1000; i++) {
            d.addLast(i);
        }

        assertEquals(1000, d.size());

        for (int i = 999; i >= 0; i--) {
            Integer r = i;
            assertEquals(r, d.removeLast());
        }

        assertEquals(0, d.size());
    }

    @Test
    public void test1000AddFirst2times() {
        Deque<Integer> d = new Deque<Integer>();
        for (int i = 0; i < 1000; i++) {
            d.addFirst(i);
        }

        assertEquals(1000, d.size());

        for (int i = 0; i < 1000; i++) {
            Integer r = i;
            assertEquals(r, d.removeLast());
        }

        assertEquals(0, d.size());
        for (int i = 0; i < 1000; i++) {
            d.addFirst(i);
        }

        assertEquals(1000, d.size());

        for (int i = 0; i < 1000; i++) {
            Integer r = i;
            assertEquals(r, d.removeLast());
        }

        assertEquals(0, d.size());
    }

    @Test
    public void test1000AddLast2times() {
        Deque<Integer> d = new Deque<Integer>();
        for (int i = 0; i < 1000; i++) {
            d.addLast(i);
        }

        assertEquals(1000, d.size());

        for (int i = 999; i >= 0; i--) {
            Integer r = i;
            assertEquals(r, d.removeLast());
        }

        assertEquals(0, d.size());

        for (int i = 0; i < 1000; i++) {
            d.addLast(i);
        }

        assertEquals(1000, d.size());

        for (int i = 999; i >= 0; i--) {
            Integer r = i;
            assertEquals(r, d.removeLast());
        }

        assertEquals(0, d.size());
    }

    @Test
    public void randomAdd() {
        Deque<String> d = new Deque<String>();
        d.addFirst("a");
        d.addFirst("b");
        d.addFirst("c");
        assertEquals("c", d.removeFirst());
        assertEquals("a", d.removeLast());
        d.addFirst("d");
        d.addLast("e");
        d.addFirst("f");
        d.addLast("g");
        assertEquals("f", d.removeFirst());
        assertEquals("d", d.removeFirst());
        assertEquals("b", d.removeFirst());
        d.addFirst("h");
        d.addLast("i");
        d.addFirst("j");
        d.addLast("k");
        assertEquals("k", d.removeLast());
        assertEquals("i", d.removeLast());
        assertEquals("g", d.removeLast());
        assertEquals("e", d.removeLast());
        assertEquals("j", d.removeFirst());

    }

}