:description: A linked list is a linear data structure where elements are not stored in contiguous memory locations. Instead, they are represented as individual objects called nodes, which are chained together using pointers or references.


Linked List
===========

A **linked list** is a linear data structure where elements are not stored in contiguous memory locations. Instead, they are represented as individual objects called **nodes**, which are chained together using pointers or references.


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

.. grid:: 1
    :gutter: 3


    .. grid-item-card:: Singly Linked List
        :link: ./singly
        :link-type: url

        A **singly linked list** is a linear data structure where elements are stored in individual objects called **nodes**, and each node points to the next consecutive node via a reference pointer. Unlike `arrays <../array>`_, elements are not stored in contiguous memory locations, allowing for dynamic memory allocation.


    .. grid-item-card:: Doubly Linked List
        :link: ./doubly
        :link-type: url

        A **doubly linked list** is a linear data structure where each element (called a **node**) contains a data field and two pointers: one pointing to the next node, and another pointing to the previous node. This structure enabled bidirectional traversal, allowing you to move both forward and backward through the sequence.


    .. grid-item-card:: Circular Linked List
        :link: ./circular/
        :link-type: url

        A circular linked list is a variation of a linked list where the last node points back to the first node, forming a closed loop. Unlike regular linked lists, it does not contain any Null pointers at the end.


.. toctree::
    :hidden:
    :maxdepth: 2

    singly
    doubly
    circular/index