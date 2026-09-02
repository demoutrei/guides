Radix Sort
==========

**Radix Sort** is a non-comparison-based sorting algorithm that organizes data with integer keys by grouping elements by their individual digits sharing the same significant position and value. Unlike comparison sorts like `Merge Sort <./merge_sort>`_ and `Quick Sort <./quick_sort>`_, Radix Sort utilizes a stable subroutine (typically `Counting Sort <./counting_sort>`_) to sort data iteratively from the least significant digit (LSD) to the most significant digit (MSD).


.. admonition:: Key Characteristics
    :class: tip

    Non-Comparison-Based
      It distributes keys into buckets based on positional values.

    Subroutine Dependence
      It relies heavily on another stable sorting algorithm---typically `Counting Sort <./counting_sort>`_---as a subroutine to sort the individual digits in each pass.

    LSD vs. MSD Variants
      It can process keys from Least Significant Digit (LSD) to Most Significant Digit (standard for integers), or from Most Significant Digit (MSD) downwards (often used for string sorting).

    Fixed-Length Requirement
      Elements must be breakable into identifiable digit or character places. Shorter values are padded with leading zeros or spaces to match the maximum length.


.. admonition:: Time and Space Complexity
    :class: tip

    Time Complexity: :math:`O(d * (n + k))`
      Runs :math:`d` times (digits) over :math:`n` elements using :math:`k` buckets.

    Space Complexity: :math:`O(n + k)`
      Requires temporary output arrays and a tracking bucket array.

    Stability: Stable
      Preserves relative order of duplicate elements using stable sorting subroutines.


How It Works
^^^^^^^^^^^^

1. Find the largest number in the array to determine the number of iterations (:math:`d`) required.
2. Start with the 1s place (:math:`10 ^ 0`). Group the numbers into 10 buckets (0-9) matching their active digit.
3. Collect numbers from the buckets back into the array, keeping the relative order intact.
4. Advance to the 10s place (:math:`10 ^ 1`), then 100s place (:math:`10 ^ 2`), repeating the process until all digits are exhausted.


Visualization
~~~~~~~~~~~~~

.. figure:: https://upload.wikimedia.org/wikipedia/commons/0/04/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F.gif?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail_unscaled
    :align: center
    :width: 80%

    *Source*: `Wikimedia Commons <https://commons.wikimedia.org/wiki/Category:Radix_sort>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <vector>

        template <int size>
        void countingSort(int (&array)[size], int exp) {
          int output[size];
          std::vector<int> count(11, 0);
          for (int i = 0; i < size; ++i) {
            int index { array[i] / exp };
            ++count[index % 10];
          }
          for (int i = 1; i < 10; ++i) {
            count[i] += count[i - 1];
          }
          for (int i = size - 1; -1 < i; --i) {
            int index { array[i] / exp };
            output[count[index % 10] - 1] = array[i];
            --count[index % 10];
          }
          for (int i = 0; i < size; ++i) {
            array[i] = output[i];
          }
        }

        template <int size>
        void radixSort(int (&array)[size]) {
          int maximum = 0;
          for (const int item : array) {
            maximum = std::max(maximum, item);
          }
          int exp { 1 };
          while (1 <= (maximum / exp)) {
            countingSort(array, exp);
            exp *= 10;
          }
        }

        int main() {
          int array[] { 170, 45, 75, 90, 802, 24, 2, 66 };
          radixSort(array); // { 2, 24, 45, 66, 75, 90, 170, 802 }
        }

    .. code-tab:: py

        def counting_sort(array: list[int], exp: int) -> None:
          size: int = len(array)
          output: list[int] = [0] * size
          count: list[int] = [0] * 10
          for i in range(size):
            index: int = array[i] // exp
            count[index % 10] += 1
          for i in range(1, 10):
            count[i] += count[i - 1]
          for i in range(size - 1, -1, -1):
            index: int = array[i] // exp
            output[count[index % 10] - 1]: int = array[i]
            count[index % 10] -= 1
          for i in range(size):
            array[i]: int = output[i]

        def radix_sort(array: list[int]) -> None:
          maximum: int = max(array)
          exp: int = 1
          while 1 <= (maximum / exp):
            counting_sort(array, exp)
            exp *= 10

        array: list[int] = [ 170, 45, 75, 90, 802, 24, 2, 66 ]
        radix_sort(array) # [ 2, 24, 45, 66, 75, 90, 170, 802 ]