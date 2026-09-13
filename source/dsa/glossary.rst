:description: Data Structures & Algorithms Guidebook Glossary


Glossary
========


.. glossary::

    Algorithm
      A step-by-step set of rules or instructions used to solve a problem, perform a calculation, or complete a specific task.

    Array
      A fundamental, linear data structure that stores a collection of elements of the same data type in contiguous (adjacent) memory locations. Because elements are stored in a continuous block, each item can be directly identified and accessed using a numerical **index**, typically starting at 0.

    Big-Omega Notation
      Defines the asymptotic lower bound of an algorithm's time complexity. It represents absolute minimum time or steps an algorithm requires to run for large input sizes. In simpler terms, it answers the question: "*At the very least, how fast will this algorithm grow?*".

    Big-O Notation
      A mathematical metric used to describe the efficiency and performance of an algorithm. It measures how the execution time or space requirements grow relative to the input size (:math:`n`), specially representing the worse-case scenario (upper bound).

    Big-Theta Notation
      efines a tight asymptotic bound on the execution time of an algorithm. Unlike Big-O (which provides a maximum boundary) or Big-Omega (which provides a minimum boundary), Big-Theta bounds a function from both above and below. This means the algorithm's actual performance scales precisely at the rate indicated by the bounding function as input size grows toward infinity.

    Binary Search
      An efficient divide-and-conquer algorithm designed to locate a target value within a sorted array or list. By repeatedly halving the search space, it avoids checking every element individually, making it exponentially faster than Linear Search for large datasets.

    Bubble Sort
      A simple, comparison-based sorting algorithm that works by repeatedly stepping through a list, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated for multiple passes until the entire list is completely sorted and no further swaps are required.

    Circular Doubly Linked List
      A complex linear data structure where each node contains a data field and two pointers (``next`` and ``previous``), and the list forms a continuous loop. Specifically, the ``next`` pointer of the last node points back to the first node, and the ``previous`` pointer of the first node points back to the last node.

    Circular Linked List
      A variation of a Linked List where the last node points back to the first node, forming a closed loop. Unlike regular Linked List, it does not contain any ``Null`` pointers at the end.

    Circular Singly Linked List
      A linear data structure where the last node points back to the first node (head) instead of pointing to ``Null``. Each node contains a single ``data`` field and a single ``next`` pointer, forming a continuous, closed loop.

    Constant Space
      Memory stays exactly the same regardless of input size.

    Constant Time
      Execution time remains the same regardless of input size.

    Counting Sort
      A non-comparison-based integer sorting algorithm that runs in linear time. It works by counting the occurrences of each distinct value in the input array. It then uses arithmetic (prefix sums) to calculate the exact starting positions of those values in the sorted output array.

    Data Structure
      A specialized format for organizing, processing, retrieving, and storing data in a computer system so it can be used efficiently. It provides a physical implementation for abstract concepts, ensuring that code can access and modify information quickly and accurately.

    Data Structures and Algorithms
      Represents the foundational building blocks of computer science that enable efficient data organization and problem solving.

    Doubly Linked List
      A linear data structure where each element (called a **node**) contains a data field and two pointers: one pointing to the next node, and another pointing to the previous node. This structure enabled bidirectional traversal, allowing you to move both forward and backward through the sequence.

    Dynamic Size Stack
      Can grow and shrink automatically as needed. If the stack is full, its capacity expands to allow more elements. As elements are removed, memory usage can shrink as well.

    Exponential Time
      Growth doubles with each additional data unit; quickly becomes unrunnable.

    Factorial Time
      Grows incredibly fast; completely unusable for inputs larger than :math:`n ≈ 10`.

    Fixed-Size Stack
      Has a predefined capacity. Once it becomes full, no more elemnts can be added (this causes **overflow**). If the stack is empty and we try to remove an element, it causes **underflow**. Typically implemented using a static array.

    Insertion Sort
      A simple, comparison-based sorting algorithm that builds a final sorted array one element at a time. It works exactly like sorting playing cards in your hands; you pick an unsorted card, compare it to the sorted cards in your hand, and slide it into its correct position.

    Linear Data Structure
      A data organization method where elements are arranged **sequentially** or **linearly**, one after another, so that each element connects to its unique predecessor and successor. Elements are ordered on a single level, allowing you to traverse the entire structure from start to finish in a single run.

    Linear Search
      Also known as a **sequential search**; is a simple searching algorithm that checks every element in a data collection one by one in a sequential order until it finds the target value or reaches the end of the collection.

    Linear Space
      Memory grows at a direct 1:1 ratio with the input size.

    Linear Time
      Running time grows in direct proportion to the input size.

    Linearithmic Space
      Memory grows slightly faster than linear.

    Linearithmic Time
      Slightly worse than linear, typical for efficient sorting mechanisms.

    Linked List
      A linear data structure where elements are not stored in contiguous memory locations. Instead, they are represented as individual objects called **nodes**, which are chained together using pointers or references.

    Logarithmic Space
      Memory grows slowly, scaling with the height of balanced tree paths.

    Logarithmic Time
      The problem size is divided by a factor (usually halved) at each step.

    Merge Sort
      An efficient, comparison-based, divide-and-conquer sorting algorithm invented by John von Neumann in 1945. It works by recursively breaking down an array into smaller sub-arrays until they contain only one element each, and then merging those sub-arrays back together in sorted order.

    Non-Linear Data structure
      An organization method where data items are not arranged in a sequential, one-by-one order. Instead, elements connect in hierarchical or network-like patterns. One node can link to multiple other nodes, meaning you cannot visit every piece of data in a single straightforward pass.

    Non-Primitive Data Structure
      A complex, user-defined or language-derived data organization format built by combining one or more primitive data structures (such as integers, characters, booleans). Instead of storing a single basic value, non-primitive data structures organize, store, and manipulate collections of related data items. They provide advanced features like dynamic sizing, relationship tracking between entries, and reference-based memory management.

    Primitive Data Structure
      The most basic and fundamental data types built directly into a programming language. They are **atomic**, meaning they hold a **single value** at a specific memory location and cannot be broken down into simpler data subtypes. Because they operate directly according to low-level machine instructions, they are highly optimized for memory speed.

    Quadratic Space
      Memory scales by the square of input size.

    Quadratic Time
      Execution time scales non-linearly, squaring the input size growth.

    Quick Sort
      An efficient, comparison-based, divide-and-conquer sorting algorithm that sorts an array by selecting a "pivot" element and partitioning the other elements into two sub-arrays based on whether they are smaller or larger than the pivot.

    Radix Sort
      A non-comparison-based sorting algorithm that organizes data with integer keys by grouping elements by their individual digits sharing the same significant position and value. Unlike comparison sorts like Merge Sort and Quick Sort, Radix Sort utilizes a stable subroutine (typically Counting Sort) to sort data iteratively from the least significant digit (LSD) to the most significant digit (MSD).

    Selection Sort
      An in-place, comparison-based sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion of an array and swapping it with the first unsorted element. This shifts the boundary between the sorted and unsorted sections one step to the right until the entire dataset is ordered.

    Singly Linked List
      linear data structure where elements are stored in individual objects called **nodes**, and each node points to the next consecutive node via a reference pointer. Unlike arrays, elements are not stored in contiguous memory locations, allowing for dynamic memory allocation.

    Space Complexity
      A metric that quantifies the total memory space an algorithm or data structure requires to run to completion as a function of the input size (:math:`n`). It is expressed using Big O notation to define how memory requirements scale rather than measuring exact bytes, which vary by hardware.

    Stack
      A linear data structure that follows the **Last In, First Out** (LIFO) principle, meaning the last element added is the first one to be removed. Think of it like a physical stack of plates---you can only add a new plate to the top, and you can only remove the plate that is currently on top.

    Time Complexity
      A theoretical measure that quantifies the amount of time an algorithm takes to run as a function of the length of its input (:math:`n`). Instead of measuring actual seconds---which change based on hardware, compilers, and processors---time complexity counts the number of elementary operations or code statements executed.