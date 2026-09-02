Bubble Sort
===========

**Bubble Sort** is a simple, comparison-based sorting algorithm that works by repeatedly stepping through a list, comparing adjacent elements, and swapping tehm if they are in the wrong order. This process is repeated for multiple passes until the entire list is completely sorted and no further swaps are required.

The algorithm earns its name because larger elements gradually "bubble up" to the end of the list with each successive pass, much like air bubbles rising to the surface of water.


.. admonition:: Key Characteristics
    :class: tip

    Adjacent Comparisons
      Checks only two neighboring items at a time.

    Sequential Swapping
      Swaps adjacent items to change their relative position.

    Iterative Passes
      Requires multiple full sweeps over the remaining unsorted items.

    Right-to-Left Settlement
      Locks the largest item into its final position after each pass.


.. admonition:: Time and Space Complexity
    :class: tip

    Worst-Case Time Complexity: :math:`O(n ^ 2)`
      Occurs when the input array is in reverse order, requiring nested loops to check every element pair.

    Average Time Complexity: :math:`O(n ^ 2)`
      Happens on average for randomly distributed arrays.

    Best-Case Time Complexity: :math:`O(n ^ 2)`
      Achieved only when the array is already sorted, as an optimized algorithm will stop after a single pass with zero swaps.

    Space Complexity: :math:`O(1)`
      It is an **in-place algorithm**, meaning it only manipulates the original array and uses a constant amount of extra memory.

    Stability: Yes
      It preserves the original relative order of equal elements (it does not swap them).


How It Works
^^^^^^^^^^^^

For an array of :math:`N` elements, the core logic relies on nested iterations:

1. Compare the first two adjacent elements.
2. If the left element is greater than the right element, swap their positions. 
3. Advance by one position to compare index ``i`` and ``i + 1``, repeating the swap logic. 
4. Continue this sequence until the end of the array is reached. By the end of this pass, the largest element is guaranteed to be in its final, correct position at the far right. 
5. Begin a new pass for the remaining unsorted elements. Repeat this entire cycle up to ``N-1`` times, or until a full pass completes without any swaps.


Visualization
~~~~~~~~~~~~~

.. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Sorting_bubblesort_anim.gif/250px-Sorting_bubblesort_anim.gif?utm_source=commons.wikimedia.org&utm_campaign=parser&utm_content=thumbnail
    :align: center
    :width: 80%

    *Source*: `Wikimedia <https://commons.wikimedia.org/wiki/Category:Bubble_sort>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <iostream>
        #include <utility>

        template <int size>
        void bubbleSort(int (&array)[size]) {
          bool swapped;
          for (int i = 0; i < size - 1; i++) {
            swapped = false;
            for (int j = 0; j < size - i - 1; j++) {
              if (array[j + 1] < array[j]) {
                std::swap(array[j], array[j + 1])
                swapped = true;
              }
            }
            if (!swapped) break;
          }
        }

        int main() {
          int array[5] { 3, 1, 5, 2, 4 };
          bubbleSort(array); // { 1, 2, 3, 4, 5 }
        }


    .. code-tab:: py
          
        def bubble_sort(array: list[int]) -> None:
          size: int = len(array)
          for i in range(size):
            swapped: bool = False
            for j in range(size - i - 1):
              if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped: bool = True
            if not swapped: break

        
        array: list[int] = [ 3, 1, 5, 2, 4 ]
        bubble_sort(array) # [ 1, 2, 3, 4, 5 ]