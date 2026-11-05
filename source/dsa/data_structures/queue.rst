Queue
=====

A **queue** is a fundamental linear data structure that operates on the **First In, First Out (FIFO) principle**. This means that the first element added to the queue will be the first one to be removed, much like a real-world line of people waiting at a grocery store counter.

Unlike a `stack <../stack>`_ (which only allows access at one end), a queue is open at both ends: elements are added at the back (tail), and removed from the front (head).

.. admonition:: Key Characteristics
    :class: hint

    Two Open Ends
      Unlike a stack (which is open at only one end), a queue keeps its entry and exit points separate.

    Asymmetric Operations
      Data manipulation is restricted by posiiton. Elements are only inserted at the Tail and removed from the Head.

    Sequential Order
      Elements maintain a strict temporal order based on their time of arrival.

    Dynamic or Static Size
      Depending on the implementation, a queue can have a fixed capacity (bounded, typically array-based) or a dynamic capacity (unbounded, typically linked-list based).


Advantages and Disadvantages
++++++++++++++++++++++++++++

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Advantages

        Ordered Processing
          It automatically maintains the exact order of data arrival, making it highly effective for handling temporal data sequences.

        Efficient Operations
          Basic operations like adding an element (``enqueue``) and removing an element (``dequeue``) run in constant :math:`O(1)` time complexity.

        Resource Decoupling
          It acts as an excellent asynchronous buffer between devices or processes running at different speeds (e.g. a fast CPU and a slow keyboard or printer).

        Fairness in Shared Access
          It effortlessly manages multiple consumers competing for a single shared resource by setting up a fair waiting list.

        Versatility
          It serves as a foundational component to implement other complex algorithms and data structures, such as Breadth-First Search.

    .. grid-item-card:: Disadvantages

        No Random Access
          You cannot access elements directly by their index. You must look at or remove the elements in front of them first.

        Slow Searching
          Finding a specific element within a queue requires a linear search, which takes :math:`O(n)` time complexity.

        Inefficient Mid-Structure Editing
          Modifying, inserting, or deleting items from the middle of a queue is a highly complex and time-consuming operation.

        Memory Constraints (Array Implementation)
          If a classical queue is built using a standard static array, it has a fixed maxium size that must be declared upfront.

        Wasted Space / Memory Drift
          In a basic linear array queue, once elements are deleted from the head, the physical space they occupied cannot be reused. This can flag the queue as "full" even when memory slots are sitting empty.


Core Operations
+++++++++++++++

In a standard Queue data structure, the core operations run in :math:`O(1)` constant time. However, the exact time complexity can vary depending on the underlying implementation (arrays versus linked lists) and the specific variant of the queue.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Enqueue

        Adds an element to the tail of the queue.

    .. grid-item-card:: Dequeue

        Removes an element from the head of the queue.

    .. grid-item-card:: Peek

        Returns the element at the head without removing it.

    .. grid-item-card:: isEmpty

        Checks if the queue is empty.


Visualization
+++++++++++++

.. figure:: https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221213113312/Queue-Data-Structures.png
    :align: center
    :width: 80%


Implementation
++++++++++++++

.. tabs::

    .. code-tab:: c++

        #include <iostream>

        class Queue {
          private:
            int* array;
            int headIndex, tailIndex, capacity, currentSize;

          public:
            Queue(int size) {
              capacity = size;
              array = new int[capacity];
              headIndex = 0;
              tailIndex = -1;
              currentSize = 0;
            }

            ~Queue() {
              delete[] array;
            }

            bool isFull() {
              return currentSize == capacity;
            }

            bool isEmpty() {
              return currentSize == 0;
            }

            void enqueue(int value) {
              if (isFull()) {
                std::cout << "Queue overflow. Cannot enqueue " << value <<std::endl;
                return;
              }
              tailIndex = (tailIndex + 1) % capacity;
              array[tailIndex] = value;
              currentSize++;
            }

            void dequeue() {
              if (isEmpty()) {
                std::cout << "Queue undeflow. Nothing to dequeue" << std::endl;
                return;
              }
              headIndex = (headIndex + 1) % capacity;
              currentSize--;
            }

            int peek() {
              if (isEmpty()) {
                std::cout << "Queue is empty" << std::endl;
                return;
              }
            }

            int size() {
              return currentSize;
            }
        };

    .. code-tab:: python

        class Queue[T]:
          def __init__(self, size: int, /) -> None:
            self.__array: list[T] = list()
            self.__size: int = size

          def is_full(self) -> bool:
            return self.__size <= len(self.__array)

          def is_empty(self) -> bool:
            return len(self.__array) == 0

          def enqueue(self, value: T, /) -> None:
            if self.is_full():
              print("Queue overflow. Cannot enqueue")
              return
            self.__array.append(value)

          def dequeue(self) -> None:
            if self.is_empty():
              print("Queue underflow. Nothing to dequeue")
              return
            self.__array: list[T] = self.__array[1:]

          def peek(self) -> T:
            if self.is_empty():
              print("Queue is empty")
              return
            return self.__array[0]

          @property
          def size(self) -> int:
            return len(self.__array)