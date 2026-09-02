Data Structures
===============

A **data structure** is a specialized format for organizing, processing, retrieving, and storing data in a computer system so it can be used efficiently. It provides a physical implementation for abstract concepts, ensuring that code can access and modify information quickly and accurately.


Core Classifications
^^^^^^^^^^^^^^^^^^^^

Data structures are generally divided into two main categories based on how the elements are arranged:

1. `Primitive Data Structures <#id1>`_
2. `Non-Primitive Data Structures <#id2>`_


Primitive Data Structures
~~~~~~~~~~~~~~~~~~~~~~~~~

Primitive data structures are the most basic and fundamental data types built directly into a programming language. They are **atomic**, meaning they hold a **single value** at a specific memory location and cannot be broken down into simpler data subtypes. Because they operate directly according to low-level machine instructions, they are highly optimized for memory speed.

.. admonition:: Key Characteristics
    :class: tip

    **Predefined**: Built straight into the programming language compiler or interpreter.

    **Direct Operation**: Handled by CPU machine instructions.

    **Fixed Size**: Occupy a predetermined, fixed amount of memory (e.g. 4 bytes for an integer).

    **Single-Value**: Designed to hold exactly one data point at a time.


.. admonition:: Examples
    :class: hint

    **Integer**: Stores positive or negative whole numbers without decimal points.

    **Floating-point**: Represents real numbers containing a fractional decimal component.

    **Character**: Holds a single letter, number, punctuation mark, or space symbol.

    **Boolean**: Represents a logical state consisting of only two possible values: ``true`` or ``false``.

    **Pointer**: Stores the exact memory address location of another variable.


Non-Primitive Data Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A non-primitive data structure is a complex, user-defined or language-derived data organization format built by combining one or more primitive data structures (such as integers, characters, booleans). Instead of storing a single basic value, non-primitive data structures organize, store, and manipulate collections of related data items. They provide advanced features like dynamic sizing, relationship tracking between entries, and reference-based memory management.

Non-primitive data structures are broadly split into two structural categories:

1. `Linear Data Structures <#id3>`_
2. `Non-Linear Data Structures <#id4>`_


Linear Data Structures
----------------------

A linear data structure is a data organization method where elements are arranged **sequentially** or **linearly**, one after another, so that each element connects to its unique predecessor and successor. Elements are ordered on a single level, allowing you to traverse the entire structure from start to finish in a single run.


.. admonition:: Key Characteristics
    :class: tip

    **Sequential Order**: Elements form a clear line or sequence.

    **Single-Level Traversing**: You can visit every element sequentially without splitting into different branches like trees or graphs.

    **Memory Management**: They can use continuous memory allocations or scattered memory nodes linked by pointers.


Non-Linear Data Structures
--------------------------

A non-linear data structure is an organization method where data items are not arranged in a sequential, one-by-one order. Instead, elements connect in hierarchical or network-like patterns. One node can link to multiple other nodes, meaning you cannot visit every piece of data in a single straightforward pass.


.. admonition:: Key Characteristics
    :class: tip

    **Multiple Paths**: Elements connect across multiple levels rather than a single flat line.
    
    **Many-to-many links**: One item can have relationships with several other items.

    **Complex Traversal**: Visiting all data requires special paths like depth-first or breadth-first search.

    **Flexible Memory**: Memory is allocated dynamically as nodes branch out.


Common Operations
^^^^^^^^^^^^^^^^^

Regardless of the type, software programs use data structures to perform six fundamental operations:

- **Searching**: Finding a specific element within the structure.
- **Sorting**: Arranging elements in a certain order (e.g. alphabetical, ascending numeric).
- **Insertion**: Adding a new item to the structure.
- **Deletion**: Removing an existing item from the structure.
- **Updating**: Modifying an existing data element.
- **Traversal**: Visiting every element in the structure exactly once to process it.


.. toctree::
    :maxdepth: 2
    :caption: Topics

    array
    linked_list/index
    stack