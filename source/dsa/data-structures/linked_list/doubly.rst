Doubly Linked List
==================

A **doubly linked list** is a linear data structure where each element (called a **node**) contains a data field and two pointers: one opinting to the next node, and another pointing to the previous node. This structure enabled bidirectional traversal, allowing you to move both forward and backward through the sequence.


Advantages and Disadvantages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Advantages

        Bidirectional Deletion
          The list can be iterated from head-to-tail or tail-to-head seamlessly.

        Efficient Deletion
          Removing a node is faster than a `singly linked list <./singly>`_ if you already have a pointer to it, as you do not need to look up its predecessor.

        Dynamic Allocation
          Memory grows and shrinks at runtime without needing costly resizes like arrays.

    
    .. grid-item-card:: Disadvantages

        Memory Overhead
          Every node consumes extra memory to store the additional pointer.

        Complex Bookkeeping
          Insertion and deletion operations require adjusting up to four pointers, increasing the risk of code bugs.

        No Random Access
          Elements cannot be instanly reached via an index like `arrays <../array>`_.


Node Structure
^^^^^^^^^^^^^^

Every node in a doubly linked list consists of three distinct parts:

Previous Pointer
  Stores the memory address of the preceding node.

Data
  Holds the actual value or payload.

Next Pointer
  Stores the memory address of the succeeding node.

The ``previous`` pointer of the first node (head) and the ``next`` pointer of the last node (tail) point to ``Null`` to signify the boundaries of the list.


Time Complexity of Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Access/Search: :math:`O(n)`
  Must traverse nodes sequentially.

Insertion at Head/Tail: :math:`O(1)`
  Immediate insertion if pointers are maintained.

Insertion in Middle: :math:`O(n)`
  Requires finding the target location first.

Deletion of Given Node: :math:`O(1)`
  No sequential lookup needed to find the preceding node.


Visualization
^^^^^^^^^^^^^

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20240318150717/Doubly-Linked-List-in-Data-Structure.webp
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/dsa/what-are-real-life-examples-of-double-linked-list/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <iostream>

        struct Node {
          int data;
          Node *next;
          Node *previous;

          Node(int data) : data(data), next(nullptr), previous(nullptr) {}
        };

        class LinkedList {
          private:
            Node *head;
            Node *tail;

          public:
            LinkedList() : head(nullptr), tail(nullptr) {}

            ~LinkedList() {
              clear();
            }

            void append(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                tail = node;
                return;
              }
              tail->next = node;
              node->previous = tail;
              tail = node;
            }

            void clear() {
              Node *current = head;
              while (current != nullptr) {
                Node *next = current->next;
                delete current;
                current = next;
              }
              head = nullptr;
            }

            void deleteNode(int data) {
              Node *current = head;
              while (current != nullptr) {
                if (current->data != data) {
                  current = current->next;
                  continue;
                }
                if (current == head) {
                  head = current->next;
                  if (head != nullptr) {
                    head->previous = nullptr;
                  } else {
                    tail = nullptr;
                  }
                } else if (current == tail) {
                  tail = current->previous;
                  tail->next = nullptr;
                } else {
                  current->previous->next = current->next;
                  current->next->previous = current->previous;
                }
                delete current;
                return;
              }
            }

            void displayBackward() {
              Node *current = tail;
              while (current != nullptr) {
                std::cout << current->data << " <-> ";
                current = current->previous;
              }
              std::cout << "nullptr" << std::endl;
            }

            void displayForward() {
              Node *current = head;
              while (current != nullptr) {
                std::cout << current->data << " <-> ";
                current = current->next;
              }
              std::cout << "nullptr" << std::endl;
            }

            void prepend(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                tail = node;
                return;
              }
              head->previous = node;
              node->next = head;
              head = node;
            }
        };
  

    .. code-tab:: python

        class Node[T]:
          def __init__(self, data: T) -> None:
            self.data: T = data
            self.next: Optional[Node[T]] = None
            self.previous: Optional[Node[T]] = None

        class LinkedList[T]:
          def __init__(self) -> None:
            self.head: Optional[Node[T]] = None
            self.tail: Optional[Node[T]] = None

          def append(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              self.tail: Node[T] = node
              return
            self.tail.next: Node[T] = node
            node.previous: Node[T] = self.tail
            self.tail: Node[T] = node

          def delete(self, data: T) -> None:
            current: Optional[Node[T]] = self.head
            while current:
              if current.data != data:
                current: Optional[Node[T]] = current.next
                continue
              if current == self.head:
                self.head: Optional[Node[T]] = current.next
                if self.head: self.head.previous: Optional[Node[T]] = None
                else: self.tail: Optional[Node[T]] = None
              elif current == self.tail:
                self.tail: Node[T] = current.previous
                self.tail.next: Optional[Node[T]] = None
              else:
                current.previous.next: Node[T] = current.next
                current.next.previous: Node[T] = current.previous

          def display_backward(self) -> None:
            elements: list[str[T]] = list()
            current: Optional[Node[T]] = self.tail
            while current:
              elements.append(str(current.data))
              current: Optional[Node[T]] = current.previous
            print(" <-> ".join(elements) if elements else "Empty")

          def display_forward(self) -> None:
            elements: list[str[T]] = list()
            current: Optional[Node[T]] = self.head
            while current:
              elements.append(str(current.data))
              current: Optional[Node[T]] = current.next
            print(" <-> ".join(elements) if elements else "Empty")

          def prepend(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              self.tail: Node[T] = node
              return
            self.head.prev: Node[T] = node
            node.next: Node[T] = self.head
            self.head: Node[T] = node