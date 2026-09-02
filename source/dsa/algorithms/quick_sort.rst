Quick Sort
==========

**Quick Sort** is an efficient, comparison-based divide-and-conquer sorting algorithm that sorts an array by selecting a "pivot" element and partitioning the other elements into two sub-arrays based on whether they are smaller or larger than the pivot.


.. admonition:: Key Characteristics
    :class: tip

    In-Place Sorting
      It recognizes elements directly within the original array. It does not need to duplicate arrays into separate memory blocks like `Merge Sort <./merge_sort>`_.

    Unstable Sorting
      It is generally unstable. The swapping mechanism can disrupt the original relative order of duplicate elements.

    Cache-Friendly
      Its sequential memory access patterns take great advantage of hardware cache architectures, making it faster in practice than Heap Sort or `Merge Sort <./merge_sort>`_ on real systems.


.. admonition:: Time and Space Complexity
    :class: tip

    Best-Case Time Complexity: :math:`O(n log n)`
      When the chosen pivot always splits the array into two equal halves.

    Average-Case Time Complexity: :math:`O(n log n)`
      Occurs under typical randomized data distributions.

    Worst-Case Time Complexity: :math:`O(n ^ 2)`
      Occurs when the input array is already sorted/reversed and the boundary items (first/last) are picked as the pivot.

    Space Complexity: :math:`O(log n)`
      Memory required on the recursive call stack. It sorts in-place.

    Stability: Unstable
      Equal elements might have their relative order swapped during partitioning steps.


How It Works
^^^^^^^^^^^^

1. Choose an element from the array to act as the boundary tracker.
2. Rearrange the array. Move all elements smaller than the pivot to its left and all elements larger to its right. The pivot is now in its final, correctly sorted position.
3. Recursively apply the same logic to the left sub-array and the right sub-array.


Visualization
~~~~~~~~~~~~~

.. figure:: https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail_unscaled
    :align: center
    :width: 80%

    *Source*: `Wikimedia <https://en.wikipedia.org/wiki/File:Sorting_quicksort_anim.gif>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <utility>

        template <int size>
        int partition(int (&array)[size], int lowIndex, int highIndex) {
          int pivot { array[highIndex] };
          int i { lowIndex - 1 };
          for (int j = lowIndex; j < highIndex; ++j) {
            if (array[j] < pivot) {
              ++i;
              std::swap(array[i], array[j]);
            }
          }
          std::swap(array[i + 1], array[highIndex]);
          return i + 1;
        }

        template <int size>
        void quickSort(int (&array)[size], int lowIndex, int highIndex) {
          if (highIndex <= lowIndex) return;
          int pivotIndex = partition(array, lowIndex, highIndex);
          quickSort(array, lowIndex, pivotIndex - 1);
          quickSort(array, pivotIndex + 1, highIndex);
        }

        int main() {
          int array[5] { 2, 3, 1, 5, 4 };
          quickSort(array, 0, 4); // { 1, 2, 3, 4, 5 }
        }


    .. code-tab:: py

        def partition(array: list[int], /, *, low_index: int, high_index: int) -> :
          pivot: int = array[high_index]
          i: int = low_index - 1
          for j in range(low_index, high_index):
            if array[j] < pivot:
              i += 1
              array[i], array[j] = array[j], array[i]
          array[i + 1], array[high_index] = array[high_index], array[i + 1]
          return i + 1

        def quick_sort(array: list[int], /, *, low_index: int = 0, high_index: int = -1) -> None:
          if high_index < 0:
            high_index: int += len(array)
          if high_index <= low_index: return
          pivot_index: int = partition(array, low_index = low_index, high_index = high_index)
          quick_sort(array, low_index, pivot_index - 1)
          quick_sort(array, pivot_index + 1, high_index)

        array: list[int] = [ 2, 3, 1, 5, 4 ]
        quick_sort(array) # [ 1, 2, 3, 4, 5 ]