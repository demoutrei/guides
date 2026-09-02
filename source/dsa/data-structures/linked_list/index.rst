Linked List
===========

A **linked list** is a linear data structure where elmeents are not stored in contiguous memory locations. Instead, they are represented as individual objects called **nodes**, which are chained together using pointers or references.


.. admonition:: Key Characteristics
    :class: tip

    Dynamic Sizing
      Grows or shrinks at runtime without needing pre-allocated memory blocks.

    Non-Contiguous Allocation
      Nodes are placed anywhere in free memory space, reducing memory fragmentation.

    Sequential Access Only
      Lacks index-based direct access; traversing requires starting at the head.

    Efficient Insertion/Deletion
      Modifies adjacent node pointers without shifting remaining list elements.

    Memory Overhead
      Requires extra storage space per node to maintain the pointer addresses.

    Poor Cache Locality
      Scattered memory placement results in more CPU cache misses than arrays.


Anatomy of a Node
^^^^^^^^^^^^^^^^^

Each node in a linked list consists of two essential parts:

Data
  The actual value or information stored in the node.

Next
  A pointer or reference containing the memory address of the subsequent node.

The list begins at a reference point called the ``Head``. The final node points to ``Null``, indicating the end of the sequence.


Types of Linked Lists
^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 2

    singly
    doubly
    circular/index