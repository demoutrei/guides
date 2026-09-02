Merge Sort
==========

**Merge Sort** is an efficient, comparison-based, divide-and-conquer sorting algorithm invented by John von Neumann in 1945. It works by recursively breaking down an array into smaller sub-arrays until they contain only one element each, and then merging those sub-arrays back together in sorted order.


.. admonition:: Key Characteristics
    :class: tip

    Divide and Conquer Strategy
      The algorithm slits the input array into two halves recursively until individual element sub-arrays are reached (the base case), then combines them using a structured merge process.

    Strict Performance Consistency
      Unlike `Quick Sort <./quick_sort>`_, its time complexity remains exactly :math:`O(n log n)` across all inputs. The structural dividing pattern is completely unaffected by how ordered the initial data is.

    Stable Sorting Mechanism
      It naturally preserves the original relative ordering of identical keys. When two elements are equal during the merge phase, the element originating from the left sub-array is consistently favored.

    Out-of-Place Execution
      Standard array-based implementations are not in-place. The algorithm allocates :math:`O(n)` temporary auxiliary space to hold elements during the comparison and merging operations.

    Sequential Access Optimization
      Because it processes items in linear sequences during the merging phase, it is exceptionally efficient for sorting sequential access structures like `linked lists <../data_structures/linked_list>`_ and for external sorting involving slow secondary storage media.


.. admonition:: Time and Space Complexity
    :class: tip

    Best-Case Time Complexity: :math:`O(n log n)`
      Splits the array evenly regardless of its intial layout.

    Average-Case Time Complexity: :math:`O(n log n)`
      Consistent logarithmic behavior across arbitrary data.

    Worst-Case Time Complexity: :math:`O(n log n)`
      Guarantees performance limits even on reversed inputs.

    Space Complexity: :math:`O(n)`
      Requires auxiliary memory arrays to build out merged subsets.

    Stability: Stable
      Preserves original sequence order for duplicates.


How It Works
^^^^^^^^^^^^

1. Find the midpoint of the array and split it into two smaller subarrays. Repeat this recursively until you are left with individual elements (which are sorted by default).
2. Process the sub-arrays recursively through the merge sort logic.
3. Merge the smaller, sorted sub-arrays back together into a single, fully sorted array.


Visualization
~~~~~~~~~~~~~

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20250923102849709166/arr_.webp
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/dsa/merge-sort/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <vector>

        void merge(std::vector<int>& array, int left, int midpoint, int right) {
          int size1 { midpoint - left + 1 };
          int size2 { right - midpoint };
          std::vector<int> L(size1), R(size2);
          for (int i = 0; i < size1; i++) {
            L[i] = array[left + i];
          }
          for (int j = 0; j < size2; j++) {
            R[j] = array[midpoint + 1 + j];
          }
          int i { 0 }, j { 0 };
          int k { left };
          while (i < size1 && j < size2) {
            if (L[i] <= R[j]) {
              array[k] = L[i];
              i++;
            } else {
              array[k] = R[j];
              j++;
            }
            k++;
          }
          while (i < size1) {
            array[k] = L[i];
            i++;
            k++;
          }
          while (j < size2) {
            array[k] = R[j];
            j++;
            k++;
          }
        }

        void mergeSort(std::vector<int>& array, int left, int right) {
          if (right <= left) return;
          int midpoint { left + (right - left) / 2 };
          mergeSort(array, left, midpoint);
          mergeSort(array, midpoint + 1, right);
          merge(array, left, midpoint, right);
        }

        int main() {
          std::vector<int> array = { 38, 27, 43, 10 };
          int size = array.size();
          mergeSort(array, 0, size - 1); // { 10, 27, 38, 43 }
        }
    

    .. code-tab:: py

        def merge(array: list[int], left: int, midpoint: int, right: int, /) -> None:
          size1: int = midpoint - left + 1
          size2: int = right - midpoint
          L: list[int] = [0] * size1
          R: list[int] = [0] * size2
          for i in range(size1):
            L[i]: int = array[left + i]
          for j in range(size2):
            R[j]: int = array[midpoint + 1 + j]
          i = j = 0
          k: int = left
          while i < size1 and j < size2:
            if L[i] <= R[j]:
              array[k]: int = L[i]
              i += 1
            else:
              array[k]: int = R[j]
              j += 1
            k += 1
          while i < size1:
            array[k]: int = L[i]
            i += 1
            k += 1
          while j < size2:
            array[k]: int = R[j]
            j += 1
            k += 1

        def merge_sort(array: list[int], left: int = 0, right: int = -1, /) -> None:
          size: int = len(array)
          if right < 0:
            right += size
          if right <= left: return
          midpoint: int = left + (right - left) // 2
          merge_sort(array, left, midpoint)
          merge_sort(array, midpoint + 1, right)
          merge(array, left, midpoint, right)

        array: list[int] = [ 38, 27, 43, 10 ]
        merge_sort(array) # [ 10, 27, 38, 43 ]