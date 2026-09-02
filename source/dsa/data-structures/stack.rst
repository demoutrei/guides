Stack
=====

A **stack** is a linear data structure that follows the **Last In, First Out** (LIFO) principle, meaning the last element added is the first one to be removed. Think of it like a physical stack of plates---you can only add a new plate to the top, and you can only remove the plate that is currently on top.


.. admonition:: Key Characteristics
    :class: tip

    LIFO Structure
      Element access is restricted to the newest data point.
    
    Single Access Point
      All insertions and deletions occur exclusively at one end, called the **Top**.

    Linear Order
      Elements are organized sequentially in a straight line.

    Constant Time Complexity
      Core operations execute in :math:`O(1)` time.
    
    Dynamic or Static Sizes
      Can be built using fixed `arrays <./array>`_ or dynamic `linked lists <./linked_list>`_.

    Limited Direct Access
      Cannot read or modify elements in the middle without popping the top elements first.


.. admonition:: Last-In, First-Out Principle
    :class: tip

    The **LIFO principle** means that the last element added to a stack is the first one to be removed.
    - New elements are always pushed on top.
    - Removal (pop) always happens only from the top.
    - This ensures a strict order: last in → first out.


    .. admonition:: Examples
        :class: hint

        Stack of plates
          The last plate placed ontop is the first one you pick up.

        Stack of books
          Books are added and removed from the top, so the last book placed is the first one taken.


.. admonition:: Boundary Conditions
    :class: important
    
    Stack Overflow
      Occurs when trying to push an item onto an already full stack.

    Stack Underflow
      Occurs when trying to pop an item from an empty stack.


Advantages and Disadvantages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Advantages

        :math:`O(1)` Time Complexity
          Push, pop, and peek operations run in constant time.

        No Shifting Required
          Adding or removing data never requires shifting elements around.

        Memory Efficiency
          Requires minimal memory overhead because it only tracks a single top pointer.
        
        Inherent LIFO Management
          Perfectly models real-world undo/redo histories and browser back buttons.

        Automated Cleanup
          Automatically allocates and deallocates memory during function call execution.

        Algorithm Simplicity
          Simplifies implementations of backtracking, text parsing, and string reversals.


    .. grid-item-card:: Disadvantages

        No Random Access
          You cannot read or modify elements in the middle without popping the top.

        Risk of Overflow
          Fixed-size array implementations crash with a stack overflow error if filled past capacity.

        Risk of Underflow
          Attempting to pop elements from an entirely empty stack triggers an underflow error.

        Inflexible Resizing
          Static array variations cannot scale up dynamically if your data needs expand.

        Memory Wastage Potential
          Oversizing a static stack pre-allocates contiguous memory that may sit entirely unused.

        Poor Search/Sort Capability
          Searching for a specific value forces you to systematically destroy the structure.


Types of Stack
^^^^^^^^^^^^^^


Fixed-Size
~~~~~~~~~~

A fixed-size stack has a predefined capacity. Once it becomes full, no more elemnts can be added (this causes **overflow**). If the stack is empty and we try to remove an element, it causes **underflow**. Typically implemented using a static array.


.. admonition:: Example
    :class: hint

    Declaring a stack of size 10 using an array.


Dynamic Size
~~~~~~~~~~~~

A dynamic size stack can grow and shrinik automatically as needed. If the stack is full, its capacity expands to allow more elements. As elements are removed, memory usage can shrinik as well. Can be implemented using `linked list <./linked_list>`_ (grows/shrinks naturally), and dynamic `array <./array>`_ (like vector in C++ or ArrayList in Java).


.. admonition:: Example
    :class: hint

    Stack implementation using `linked list <./linked_list>`_ or resizable `array <./array>`_.


Core Operations
^^^^^^^^^^^^^^^

Every operation on a stack happens at a single point called the **Top of Stack** and runs in :math:`O(1)` time complexity.

Push
  Adds an item tothe top of the stack.

Pop
  Removes and returns the top item. Calling this on an empty stack causes a stack underflow error.

Peek or Top
  Returns the value of the top item without removing it.

isEmpty
  Checks if the stack is completely empty.

isFull
  Checks if a fixed-size stack has reached its maximum capacity (causes a stack overflow if exceeded).


Visualization
^^^^^^^^^^^^^

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20230116192305/stack-768.png
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/javascript/how-to-create-a-stack-visualizer-using-html-css-javascript/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <format>
        #include <iostream>

        class Stack {
          private:
            int *array;
            int capacity;
            int top;
            
          public:
            Stack(int cap) {
              array = new int[cap];
              top = -1;
              capacity = cap;
            };
            
            void display() {
              for (int i = 0; i < top + 1; ++i) {
                std::cout << array[i] << " ";
              }
              std::cout << std::endl;
            }
            
            int size() {
              return top + 1;
            }
            
            bool isFull() {
              return size() == capacity;
            }
            
            bool isEmpty() {
              return size() == 0;
            }
            
            int peek() {
              if (isEmpty()) {
                std::cout << "Empty Stack" << std::endl;
                return -1;
              }
              return array[top];
            }
            
            int pop() {
              if (isEmpty()) {
                std::cout << "Empty Stack" << std::endl;
                return -1;
              }
              return array[top--];
            }
            
            void push(int item) {
              if (capacity <= size()) {
                std::cout << "Stack Overflow" << std::endl;
                return;
              }
              array[++top] = item;
              std::cout << std::format("Item {} pushed to stack", item) << std::endl;
            }
        };


    .. code-tab:: py

        class Stack[T]:
          def __init__(self, *, capacity: Optional[int] = None) -> None:
            self.__capacity: Optional[int] = capacity
            self.__stack: list[T] = list()

          def is_empty(self) -> bool:
            return self.size == 0

          def peek(self) -> T:
            if self.is_empty():
              raise Exception("Empty Stack")
            return self.__stack[-1]

          def pop(self) -> T:
            if self.is_empty():
              raise Exception("Empty Stack")
            return self.__stack.pop()

          def push(self, item: T) -> None:
            if self.__capacity is not None and (self.__capacity <= self.size):
              raise Exception("Stack Overflow")
            self.__stack.append(item)

          @property
          def size(self) -> int:
            return len(self.__stack)


Glossary
^^^^^^^^

.. glossary::

    Top
      The position of the most recently inserted element. Insertions (push) and deletions (pop) are always performed at the top.

    Size
      Refers to the current number of elements present in the stack.