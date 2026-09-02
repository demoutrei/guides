Binary Search
=============

Binary Search is an efficient divide-and-conquer algorithm designed to locate a target value within a sorted `array <../data_structures/array>`_ or `list <../data_structures/linked_list>`_. By repeatedly halving the search space, it avoids checking every element individually, making it exponentially faster than `linear search <./linear_search>`_ for large datasets.


.. admonition:: Key Characteristics
    :class: tip

    Sorted Data Requirement
      The input collection **must be sorted** beforehand. The algorithm relies on ordering to eliminate incorrect data sections.

    Constant-Time Indexing
      It requires random access data structures. It works perfectly with `arrays <../data_structures/array>`_ but is highly inefficient with `linked lists <../data_structures/linked_list>`_.

    Three-Pointer Mechanic
      It tracks data intervals using three primary markers: a low boundary pointer, a high boundary pointer, and a calculated midpoint pointer.

    Search Space Halving:
      Each comparison eliminates exactly half of the remaining items. If the target is smaller than the midpoint, the right half is discarded, and vice versa.


.. admonition:: Time and Space Complexity
    :class: tip

    Best-Case Time Complexity: :math:`O(1)`
      Occurs when the target element matches the very first middle element checked.

    Average-Case Time Complexity: :math:`O(log n)`
      Occurs because the algorithm halves the search space with every comparison step.

    Worst-Case Time Complexity: :math:`O(log n)`
      Occurs when the target element is at the extreme ends of the array, or not present at all. The maximum number of comparisons needed is :math:`log2(n)`.

    Space Complexity
      Iterative Approach: :math:`O(1)`
        It uses a standard loop with a few pointers (``low``, ``high``, and ``mid``), requiring constant extra space.

      Recursive Approach: :math:`O(log n)`
        Each split creates a new function call that gets added to the system call stack.


How It Works
^^^^^^^^^^^^

1. Set two pointers to define your initial search boundaries.
2. Find the middle index of the current boundaries.
3. Compare the value at ``array[midpoint]`` with the ``target`` value.
4. Repeat steps 2 and 3 as long as ``low <= high``. If ``low`` becomes greater than ``high``, the search boundaries have closed completely without finding the target. The algorithm terminates and returns ``-1`` (indicating the item is not present).


Visualization
~~~~~~~~~~~~~

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20210216221243/20210216221148.gif
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/javascript/binary-search-visualization-using-javascript/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        template <int size>
        int binarySearch(int (&array)[size], int target) {
          if (size == 0) return -1;
          int low { 0 }, high { size - 1 };
          while (low <= high) {
            int midpoint { low + (high - low) / 2 };
            if (array[midpoint] == target) return midpoint;
            if (array[midpoint] < target) {
              low = midpoint + 1;
            } else {
              high = midpoint - 1;
            }
          }
          return -1;
        }

        int main() {
          int array[] { 2, 5, 8, 12, 16, 23, 38, 56, 72, 91 };
          binarySearch(array, 23); // 5
        }


    .. code-tab:: py

        def binary_search(array: list[int], /, *, target: int) -> int:
          if not array: return -1
          size: int = len(array)
          low: int = 0
          high: int = size - 1
          while low <= high:
            midpoint: int = low + (high - low) // 2
            if array[midpoint] == target:
              return midpoint
            if array[midpoint] < target:
              low: int = midpoint + 1
            else:
              high: int = midpoint - 1
          return -1


        array: list[int] = [ 2, 5, 8, 12, 16, 23, 38, 56, 72, 91 ]
        index: int = binary_search(array, target = 23) # 5