Linear Search
=============

A **linear search** (also known as a **sequential search**) is a simple searching algorithm that checks every element in a data collection one by one in a sequential order until it finds the target value or reaches the end of the collection.


.. admonition:: Key Characteristics
    :class: tip

    No Sorting Required
      Unlike a `binary search <./binary_search>`_, it works perfectly on unsorted data collections.

    Data Independent
      It accommodates both numeric and non-numeric objects like strings.

    Inefficient for Scale
      The processing time grows linearly with the size of the data structure, making it impractical for massive databases.


.. admonition:: Time and Space Complexity
    :class: tip

    The performance of a linear search scales proportionally with the number of elements :math:`n` in the dataset.

    Best-Case Time Complexity: :math:`O(1)`
      The target element is located at the very first position.

    Worst-Case Time Complexity: :math:`O(n)`
      The target element is at the end of the list or does not exist at all.

    Average Time Complexity: :math:`O(n)`
      The target element is found somewhere in the middle.
      
    Space complexity: :math:`O(1)`
      It operates directly on the existing list without requiring extra memory allocation.


How It Works
^^^^^^^^^^^^

1. Start at the first element of the list.
2. Compare the current element with the target value.
3. If they match, return the index or position and stop.
4. If they do not match, move to the next element.
5. Repeat steps 2--4 until a match is found.
6. If the list ends without a match, return ``-1`` or a failure signal.


Visualization
~~~~~~~~~~~~~

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20210216221548/ezgifcomgifmaker7.gif
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/javascript/linear-search-visualization-using-javascript/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <iostream>

        template <int size>
        int linearSearch(int (&array)[size], int target) {
          for (int i = 0; i < size; i++) {
            if (array[i] == target) return i;
          }
          return -1;
        }

        int main() {
          int array[3] = { 1, 2, 3 };
          linearSearch(array, 2); // index 1
          linearSearch(array, 5); // -1; target not found
        }


    .. code-tab:: py

        def linear_search(array: list[int], /, *, target: int) -> int:
          for index, value in enumerate(array):
            if value == target:
              return index
          return -1

        
        array: list[int] = [ 1, 2, 3 ]
        linear_search(array, target = 2) # index 1
        linear_search(array, target = 5) # -1; target not found