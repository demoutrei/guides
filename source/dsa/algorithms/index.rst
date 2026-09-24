:description: An algorithm is a step-by-step set of rules or instructions used to solve a problem, perform a calculation, or complete a specific task.


Algorithms
==========

An **algorithm** is a step-by-step set of rules or instructions used to solve a problem, perform a calculation, or complete a specific task.


Searching Algorithms
++++++++++++++++++++

A **searching algorithm** is a step-by-step procedure designed to locate a specific target item (often called a key) or determine its presence within a collection of data stored in a data structure.


.. grid:: 1
    :gutter: 3


    .. grid-item-card:: Binary Search
        :link: ./binary_search
        :link-type: url

        **Binary Search** is an efficient divide-and-conquer algorithm designed to locate a target value within a sorted `array <../data_structures/array>`_ or `list <../data_structures/linked_list>`_. By repeatedly halving the search space, it avoids checking every element individually, making it exponentially faster than `linear search <./linear_search>`_ for large datasets.


    .. grid-item-card:: Linear Search
        :link: ./linear_search
        :link-type: url

        A **linear search** (also known as a **sequential search**) is a simple searching algorithm that checks every element in a data collection one by one in a sequential order until it finds the target value or reaches the end of the collection.


Sorting Algorithms
++++++++++++++++++

A **sorting algorithm** is a step-by-step procedure or set of instructions usde to rearrange a collection of data elements (such as an array or list) into a specific, orderly sequence.


.. grid:: 1
    :gutter: 3


    .. grid-item-card:: Bubble Sort
        :link: ./bubble_sort
        :link-type: url

        **Bubble Sort** is a simple, comparison-based sorting algorithm that works by repeatedly stepping through a list, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated for multiple passes until the entire list is completely sorted and no further swaps are required.

        The algorithm earns its name because larger elements gradually "bubble up" to the end of the list with each successive pass, much like air bubbles rising to the surface of water.


    .. grid-item-card:: Counting Sort
        :link: ./counting_sort
        :link-type: url

        **Counting Sort** is a non-comparison-based integer sorting algorithm that runs in linear time. It works by counting the occurrences of each distinct value in the input array. It then uses arithmetic (prefix sums) to calculate the exact starting positions of those values in the sorted output array.

        Because it maps element values directly to array indices, it avoids the :math:`O(n log n)` minimum runtime threshold required by comparison-based algorithms like `Merge Sort <./merge_sort>`_ or `Quick Sort <./quick_sort>`_.


    .. grid-item-card:: Insertion Sort
        :link: ./insertion_sort
        :link-type: url

        **Insertion Sort** is a simple, comparison-based sorting algorithm that builds a final sorted array one element at a time. It works exactly like sorting playing cards in your hands; you pick an unsorted card, compare it to the sorted cards in your hand, and slide it into its correct position.


    .. grid-item-card:: Merge Sort
        :link: ./merge_sort
        :link-type: url

        **Merge Sort** is an efficient, comparison-based, divide-and-conquer sorting algorithm invented by John von Neumann in 1945. It works by recursively breaking down an array into smaller sub-arrays until they contain only one element each, and then merging those sub-arrays back together in sorted order.


    .. grid-item-card:: Quick Sort
        :link: ./quick_sort
        :link-type: url

        **Quick Sort** is an efficient, comparison-based, divide-and-conquer sorting algorithm that sorts an array by selecting a "pivot" element and partitioning the other elements into two sub-arrays based on whether they are smaller or larger than the pivot.


    .. grid-item-card:: Radix Sort
        :link: ./radix_sort
        :link-type: url

        **Radix Sort** is a non-comparison-based sorting algorithm that organizes data with integer keys by grouping elements by their individual digits sharing the same significant position and value. Unlike comparison sorts like `Merge Sort <./merge_sort>`_ and `Quick Sort <./quick_sort>`_, Radix Sort utilizes a stable subroutine (typically `Counting Sort <./counting_sort>`_) to sort data iteratively from the least significant digit (LSD) to the most significant digit (MSD).


    .. grid-item-card:: Selection Sort
        :link: ./selection_sort
        :link-type: url

        **Selection Sort** is an in-place, comparison-based sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion of an array and swapping it with the first unsorted element. This shifts the boundary between the sorted and unsorted sections one step to the right until the entire dataset is ordered.


.. toctree::
    :hidden:
    :maxdepth: 1

    binary_search
    bubble_sort
    counting_sort
    insertion_sort
    linear_search
    merge_sort
    quick_sort
    radix_sort
    selection_sort