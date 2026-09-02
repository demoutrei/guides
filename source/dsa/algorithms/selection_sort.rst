Selection Sort
==============

**Selection Sort** is an in-place, comparison-based sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion of an array and swapping it with the first unsorted element. This shifts the boundary between the sorted and unsorted sections oen step to the right until the entire dataset is ordered.


.. admonition:: Key Characteristics
    :class: tip

    In-Place Sorting
      It modifies the original array directly without requiring extra storage structures.

    Unstable by Default
      It can change the relative order of duplicate elements during long-distance swaps.

    Non-Adaptive Behavior
      The algorithm executes the exact same number of steps regardless of initial order.

    Brute-Force Mechanism
      It scans the remaining unsorted list fully during every single iteration.

    Minimal Swapping Operations
      It performs a maximum of :math:`O(n)` swaps, making it highly efficient when memory write cycles are costly.


.. admonition:: Time and Space Complexity
    :class: tip

    Worst-Case Time Complexity: :math:`O(n^2)`
      When nested loops scan the data.

    Average-Case Time Complexity: :math:`O(n^2)`
      For typical, random arrays.

    Best-Case Time Complexity: :math:`O(n^2)`
      Even if the array is already sorted.

    Auxiliary Space Complexity: :math:`O(1)`
      Because it sorts memory in-place.


How It Works
^^^^^^^^^^^^

1. Treat the array as two parts: sorted (initially empty) and unsorted (the entire array).
2. Search the unsorted part to locate the smallest value.
3. Swap this minimum value with the leftmost element of the unsorted part.
4. Move the boundary line one position to the right.
5. Continue these steps until the unsorted part has only one element left.


Visualization
~~~~~~~~~~~~~

.. figure:: https://upload.wikimedia.org/wikipedia/commons/3/3e/Sorting_selection_sort_anim.gif?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original
    :align: center
    :width: 80%

    *Source*: `Wikimedia <https://commons.wikimedia.org/wiki/File:Sorting_selection_sort_anim.gif>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <utility>

        template <int size>
        void selectionSort(int (&array)[size]) {
          int minimum_index;
          for (int i = 0; i < (size - 1); ++i) {
            minimum_index = i;
            for (int j = i + 1; j < n; ++j) {
              if (array[j] < array[minimum_index]) {
                minimum_index = j;
              }
            }
            std::swap(array[i], array[minimum_index]);
          }
        }

        int main() {
          int array[5] { 3, 1, 5, 2, 4 };
          selectionSort(array); // { 1, 2, 3, 4, 5 }
        }
      

    .. code-tab:: py

        def selection_sort(array: list[int]) -> None:
          size: int = len(array)
          for i in range(size - 1):
            minimum_index: int = i
            for j in range(i + 1, n):
              if array[j] < array[minimum_index]:
                minimum_index: int = j
            array[i], array[minimum_index] = array[minimum_index], array[i]

        
        array: list[int] = [ 3, 1, 5, 2, 4 ]
        selection_sort(array) # [ 1, 2, 3, 4, 5 ]