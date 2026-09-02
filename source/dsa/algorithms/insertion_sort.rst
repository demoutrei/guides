Insertion Sort
==============

**Insertion Sort** is a simple, comparison-based sorting algorithm that builds a final sorted array one element at a time. It works exactly like sorting playing cards in your hands; you pick an unsorted card, compare it to the sorted cards in your hand, and slide it into its correct position.


.. admonition:: Key Characteristics
    :class: tip

    In-Place Sorting
      It modifies the original array directly without requiring extra temporary array copies, preserving valuable memory.

    Stable Sort
      It preserves the original reltaive order of equal elements, preventing unnecessary shifts for identical values.

    Adaptive Nature
      The algorithm runs significantly faster on data sets that are already partially or substantially sorted.

    Online Capability
      It can process and sort an incoming stream of numbers in real time as it receives them.

    High Local Efficiency
      It frequently outperforms structurally superior algorithms like `Quick Sort <./quick_sort>`_ or `Merge Sort <./merge_sort>`_ when managing very small datasets (typically under 10-20 elements).


.. admonition:: Time and Space Complexity
    :class: tip

    Best-Case Time Complexity: :math:`O(n)`
      Occurs when the input array is already completely sorted.

    Average-Case Time Complexity: :math:`O(n ^ 2)`
      Occurs with a randomly ordered list of elements.

    Worst-Case Time Complexity: :math:`O(n ^ 2)`
      Occurs when the array is sorted in exact reverse order.

    Space Complexity: :math:`O(1)`
      Auxiliary space; it sorts the elements directly in place.


How It Works
^^^^^^^^^^^^

1. Start with the second element, assuming the first element is already sorted.
2. Store the current element in a temporary variable.
3. Compare the current element with the elements in the sorted portion from right to left.
4. Shift any elements that are greater than the current element one position to the right to make space.
5. Insert the current element into its correct position once a smaller element (or the start of the array) is reached.
6. Repeat this process for all remaining unsorted elements.


Visualization
~~~~~~~~~~~~~

.. figure:: https://upload.wikimedia.org/wikipedia/commons/2/24/Sorting_insertion_sort_anim.gif?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original
    :align: center
    :width: 80%

    *Source*: `Wikimedia <https://commons.wikimedia.org/wiki/File:Sorting_insertion_sort_anim.gif>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <utility>

        template <int size>
        void insertionSort(int (&array)[size]) {
          for (int i = 1; i < size; ++i) {
            int j;
            int value = array[i];
            j = i - 1;
            while (0 <= j && value < array[j]) {
              std::swap(array[j], array[j + 1]);
              --j;
            }
          }
        }

        int main() {
          int array[5] { 3, 1, 5, 2, 4 };
          insertionSort(array); // { 1, 2, 3, 4, 5 }
        }


    .. code-tab:: py

        def insertion_sort(array: list[int]) -> None:
          size: int = len(array)
          for index in range(1, size):
            value: int = array[index]
            j: int = index - 1
            while 0 <= j and value < array[j]:
              array[j + 1], array[j] = array[j], array[j + 1]
              j -= 1


        array: list[int] = [ 3, 1, 5, 2, 4 ]
        insertion_sort(array) # [ 1, 2, 3, 4, 5 ]