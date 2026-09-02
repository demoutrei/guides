Counting Sort
=============

**Counting Sort** is a non-comparison-based integer sorting algorithm that runs in linear time. It works by counting the occurrences of each distinct value in the input array. It then uses arithmetic (prefix sums) to calculate the exact starting positions of those values in the sorted output array.

Because it maps element values directly to array indices, it avoids the :math:`O(n log n)` minimum runtime threshold required by comparison-based algorithms like `Merge Sort <./merge_sort>`_ or `Quick Sort <./quick_sort>`_.


.. admonition:: Key Characteristics
    :class: tip

    Non-Comparison-Based
      It never compares two elements against each other.

    Stable
      It maintains the relative order of duplicate elements from the original input.

    Not In-Place
      It requires separate auxiliary arrays to count frequencies and store output.

    Input Restricted
      It is only effective for non-negative integers within a known, small range.


.. admonition:: Time and Space Complexity
    :class: tip

    Time Complexity: :math:`O(N + K)`
      For Best, Average, and Worst cases.

      - :math:`N` is the number of elements in the array.
      - :math:`K` is the range of the input values (``maximum value - minimum value + 1``)

    Space Complexity: :math:`O(N + K)`
      Auxiliary space to hold the count array and the output array.


How It Works
^^^^^^^^^^^^

1. Identify the maximum element to determine the size of the count array.
2. Create an array of zeros and count how many times each value appears.
3. Modify the count array by adding the previous indices. This transforms frequencies into exact starting index boundaries.
4. Traverse the original array from right to left (to preserve stability). Look up the element's value in the cumulative count array to find its index in the final output array, place it there, and decrement the count value.


Visualization
~~~~~~~~~~~~~

.. figure:: https://c.tenor.com/zswbYsLbYqEAAAAd/counting-sort.gif
    :align: center
    :width: 80%

    *Source*: `CodeCrucks <https://codecrucks.com/counting-sort/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <vector>

        std::vector<int> countingSort(std::vector<int> &array) {
          int size = array.size();
          int maximum = 0;
          for (int i = 0; i < size; ++i) {
            maximum = std::max(maximum, array[i]);
          }
          std::vector<int> countArray(maximum + 1, 0);
          std::vector<int> outputArray(size);
          for (const int item : array) {
            ++countArray[item];
          }
          for (int i = 1; i < (maximum + 1); ++i) {
            countArray[i] += countArray[i - 1];
          }
          for (int i = size - 1; -1 < i; --i) {
            outputArray[countArray[array[i]] - 1] = array[i];
            --countArray[array[i]];
          }
          return outputArray;
        }

        int main() {
          std::vector<int> array { 2, 5, 3, 0, 2, 3, 0, 2 };
          countingSort(array); // { 0, 0, 2, 2, 3, 3, 3, 5 }
        }


    .. code-tab:: py

        def counting_sort(array: list[int]) -> list[int]:
          if not array: return array
          size: int = len(array)
          count_array: list[int] = [0] * (max(array) + 1)
          output_array: list[int] = [0] * size
          for item in array:
            count_array[item] += 1
          for i in range(1, max(array) + 1):
            count_array[i] += count_array[i - 1]
          for i in range(size - 1, -1, -1):
            output_array[count_array[array[i]] - 1]: int = array[i]
            count_array[array[i]] -= 1
          return output_array

        array: list[int] = [ 2, 5, 3, 0, 2, 3, 0, 3 ]
        counting_sort(array) # [ 0, 0, 2, 2, 3, 3, 3, 5 ]