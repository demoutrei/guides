Circular Linked List
====================

A **circular linked list** is a variation of a `linked list <../>`_ where the last node points back to the first node, forming a closed loop. Unlike `regular linked lists <../singly>`_, it does not contain any ``Null`` pointers at the end.


.. toctree::
    :maxdepth: 2
    :caption: Core Variations

    singly
    doubly


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