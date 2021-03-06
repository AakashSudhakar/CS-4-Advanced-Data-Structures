#!python


class BinaryMinHeap(object):
    """ BinaryMinHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its minimum item.\n
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1. """

    def __init__(self, items=None):
        """ Initializes heap and inserts given items, if any. """
        self.items = list()                         # Initializes empty list to store items
        if items:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """ Returns string representation of heap. """
        return "BinaryMinHeap({})".format(self.items)

    def is_empty(self):
        """ Returns True if heap is empty, otherwise returns False. """
        if len(self.items) == 0:                    # Checks if heap is empty based on how many items are in list
            return True
        return False

    def size(self):
        """ Returns number of items in heap. """
        return len(self.items)

    def insert(self, item):
        """ Inserts given item into heap.\n
        TODO: RUNTIME, BEST CASE:   O(?) -> ?\t
        TODO: RUNTIME, WORST CASE:  O(?) -> ? """
        self.items.append(item)                     # Inserts item at end and bubbles up to root
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def get_min(self):
        """ Returns minimum item at root of heap.\n
        RUNTIME: O(1) -> Min item is at root. """
        if self.size() == 0:
            raise ValueError("Heap is empty and has no minimum item.")
        assert self.size() > 0
        return self.items[0]

    def delete_min(self):
        """ Removes and returns minimum item at root of heap.\n
        TODO: RUNTIME, BEST CASE:   O(?) -> ?\t
        TODO: RUNTIME, WORST CASE:  O(?) -> ? """
        if self.size() == 0:
            raise ValueError("Heap is empty and has no minimum item.")
        elif self.size() == 1:
            return self.items.pop()                 # Removes and returns only item

        assert self.size() > 1
        min_item = self.items[0]
        last_item = self.items.pop()                # Moves last item to root and bubbles down to leaves
        self.items[0] = last_item

        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def replace_min(self, item):
        """ Removes and returns minimum item at root of this heap,
        and inserts given item into heap.\n
        This method is more efficient than calling delete_min and then inserting.\n
        TODO: RUNTIME, BEST CASE:   O(?) -> ?\t
        TODO: RUNTIME, WORST CASE:  O(?) -> ? """
        if self.size() == 0:
            raise ValueError("Heap is empty and has no minimum item.")

        assert self.size() > 0
        min_item = self.items[0]
        self.items[0] = item                        # Replaces root and bubbles down to leaves

        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def _bubble_up(self, index):
        """ Ensures heap ordering property is True above given index,
        swapping out-of-order items, or until root node is reached.\n
        RUNTIME, BEST CASE:     O(1) -> Parent item is smaller than current item.\t
        RUNTIME, WORST CASE:    O(log(n)) -> Items on path up to root node are
        out-of-order. Maximum path length in complete binary tree is log(n). """
        if index == 0:
            return  # This index is the root node (does not have a parent)
        if not (0 <= index <= self._last_index()):
            raise IndexError("Invalid index: {}".format(index))

        item = self.items[index]                    # Get item's value

        parent_index = self._parent_index(index)    # Get parent's index and value
        parent_item = self.items[parent_index]
        # TODO: Swap this item with parent item if values are out of order
        # ...
        # TODO: Recursively bubble up again if necessary
        # ...

    def _bubble_down(self, index):
        """Ensure the heap ordering property is true below the given index,
        swapping out of order items, or until a leaf node is reached.
        Best case running time: O(1) if item is smaller than both child items.
        Worst case running time: O(log n) if items on path down to a leaf are
        out of order. Maximum path length in complete binary tree is log n."""
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        # Get the index of the item's left and right children
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        if left_index > self._last_index():
            return  # This index is a leaf node (does not have any children)
        # Get the item's value
        item = self.items[index]
        # TODO: Determine which child item to compare this node's item to
        child_index = 0
        # ...
        # TODO: Swap this item with a child item if values are out of order
        child_item = self.items[child_index]
        # ...
        # TODO: Recursively bubble down again if necessary
        # ...

    def _last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self.items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index."""
        if index <= 0:
            raise IndexError('Heap index {} has no parent index'.format(index))
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        return (index << 1) + 1  # Shift left to multiply by 2

    def _right_child_index(self, index):
        """Return the right child index of the item at the given index."""
        return (index << 1) + 2  # Shift left to multiply by 2


def test_binary_min_heap():
    # Create a binary min heap of 7 items
    items = [9, 25, 86, 3, 29, 5, 55]
    heap = BinaryMinHeap()
    print('heap: {}'.format(heap))

    print('\nInserting items:')
    for index, item in enumerate(items):
        heap.insert(item)
        print('insert({})'.format(item))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))
        heap_min = heap.get_min()
        real_min = min(items[: index + 1])
        correct = heap_min == real_min
        print('get_min: {}, correct: {}'.format(heap_min, correct))

    print('\nDeleting items:')
    for item in sorted(items):
        heap_min = heap.delete_min()
        print('delete_min: {}'.format(heap_min))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))


if __name__ == '__main__':
    test_binary_min_heap()
