:description: A circular linked list is a variation of a linked list where the last node points back to the first node, forming a closed loop. Unlike regular linked lists, it does not contain any Null pointers at the end.


Circular Linked List
====================

A **circular linked list** is a variation of a `linked list <../>`_ where the last node points back to the first node, forming a closed loop. Unlike `regular linked lists <../singly>`_, it does not contain any ``Null`` pointers at the end.


Core Variations
^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :gutter: 3

    
    .. grid-item-card:: Circular Singly Linked List
        :link: ./singly
        :link-type: url

        A circular singly linked list is a linear data structure where the last node points back to the first node (Head) instead of pointing to Null. Each node contains a single "data" field and a single Next pointer, forming a continuous, closed loop.


    .. grid-item-card:: Circular Doubly Linked List
        :link: ./doubly
        :link-type: url

        A circular doubly linked list is a complex linear data structure where each node contains a data field and two pointers (Next and Previous), and the list forms a continuous loop. Specifically the Next pointer of the last node points back to the first node, and the Previous pointer of the first node points back to the last node.


Advantages/Disadvantages
^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3

    .. grid-item-card:: Advantages

        Continuous Loop
          Ideal for lists that need to cycle repeatedly without resetting a pointer back to the start.

        Fast Insertions
          Instantaenous front and back operations (:math:`O(1)`) when maintaining a ``Tail`` pointer.

        No Null Pointer Errors
          Reduces specific boundary-check bugs.

    
    .. grid-item-card:: Disadvantages

        Infinite Loop Risk
          If the stopping condition (checking if you are back at the starting node) is written incorrectly, code will run forever.

        Complex Code
          Harder to reverse of split compared to a simple `linear list <../>`_.

.. toctree::
    :hidden:
    :maxdepth: 2

    singly
    doubly