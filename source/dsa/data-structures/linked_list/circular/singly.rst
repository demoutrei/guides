Circular Singly Linked List
===========================

A **circular singly linked list** is a linear data structure where the last node points back to the first node (head) instead of pointing to ``Null``. Each node contains a single ``data`` field and a single ``next`` pointer, forming a continuous, closed loop.


.. admonition:: Key Characteristics
    :class: tip

    No Null Pointers
      Traversal does not terminate automatically; it cycles indefinitely unless explicitly stopped.

    Tail Optimization
      Keeping a pointer to the ``Tail`` (last node) instead of the ``Head`` allows :math:`O(1)` constant time access to both the first node (``Tail->next``) nad the last node (``Tail``).

    Memory Efficiency
      It consumes less memory per node than a `circular doubly linked list <./doubly>`_ because it only stores one address pointer instead of two.


Advantages and Disadvantages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3

    
    .. grid-item-card:: Advantages

        Infinite Looping
          Smooth continuous interation without hitting a null-pointer error.

        Any-Node Traversal
          You can start traversing from any arbitrary node and still access every element in the list.

        Fast Edge Operations
          :math:`O(1)` insertions/deletions at both ends when using a tail pointer.

        
    .. grid-item-card:: Disadvantages

        Infinite Loop Risk
          Code errors can easily cause infinite traversal loops if the termination logic is incorrectly handled.

        Complex Management
          Harder to reverse or implement safely compared to standard `Singly Linked Lists`_.

        No Backward Traversal
          Unidirectional layout requires a full look traversal just to see the previous node.


Time Complexities of Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Insertion at Beginning: :math:`O(n)`; :math:`O(1)` with ``Tail`` pointer
  Point new node to head, update tail's ``next`` to new node.

Insertion at End: :math:`O(n)`; :math:`O(1)` with ``Tail`` pointer
  Point tail's ``next`` to new node, update tail pointer.

Deletion at Beginning: :math:`O(n)`; :math:`O(1)` with ``Tail`` pointer
  Update tail's ``next`` to point to the second node.

Deletion at End: :math:`O(n)`
  Requires traversing to the second-to-last node.

Traversal/Search: :math:`O(n)`
  Loop sequentially until returning to the starting node.


Visualization
^^^^^^^^^^^^^

.. figure:: https://www.scaler.com/topics/images/circular-linked-list-in-the-data-structure-2.webp
    :align: center
    :width: 80%

    *Source*: `Scaler Topics <https://www.scaler.com/topics/types-of-linked-list-in-data-structure/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <format>
        #include <iostream>

        struct Node {
          int data;
          Node *next;

          Node(int data) : data(data), next(nullptr) {}
        };

        class LinkedList {
          private:
            Node *head;

          public:
            LinkedList() : head(nullptr) {}
          
            void append(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                node->next = head;
                return;
              }
              Node *current = head;
              while (current->next != head) {
                current = current->next;
              }
              current->next = node;
              node->next = head;
            }

            void deleteNode(int data) {
              if (head == nullptr) return;
              Node *current = head;
              Node *previous = nullptr;
              if (current->data == data) {
                if (current->next == head) {
                  head = nullptr;
                  delete current;
                  return;
                }
                while (current->next != head) {
                  current = current->next;
                }
                Node *node = current->next;
                current->next = head->next;
                head = head->next;
                delete node;
                return;
              }
              current = head;
              while (current->next != head) {
                previous = current;
                current = current->next;
                if (current->data == data) {
                  previous->next = current->next;
                  delete current;
                  return;
                }
              }
            }

            void display() {
              if (head == nullptr) return;
              Node *current = head;
              while (true) {
                std::cout << current->data << " -> ";
                current = current->next;
                if (current == head) break;
              }
              std::cout << std::format("(Back to Head: {})", head->data) << std::endl;
            }

            void prepend(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                node->next = head;
                return;
              }
              Node *current = head;
              while (current->next != head) {
                current = current->next;
              }
              node->next = head;
              current->next = node;
              head = node;
            }
        };
  

    .. code-tab:: py

        class Node[T]:
          def __init__(self, data: T) -> None:
            self.data: T = data
            self.next: Optional[Node[T]] = None

        class LinkedList[T]:
          def __init__(self) -> None:
            self.head: Optional[Node[T]] = None

          def append(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              node.next: Node[T] = self.head
              return
            current: Node[T] = self.head
            while current.next != self.head:
              current: Node[T] = current.next
            current.next: Node[T] = node
            node.next: Node[T] = self.head

          def delete(self, data: T) -> None:
            if not self.head: return
            current: Node[T] = self.head
            previous: Optional[Node[T]] = None
            if current.data == data:
              if current.next == self.head:
                self.head: Optional[Node[T]] = None
                return
              while current.next != self.head:
                current: Node[T] = current.next
              current.next: Node[T] = self.head.next
              self.head: Node[T] = self.head.next
              return
            current: Node[T] = self.head
            while current.next != self.head:
              previous: Node[T] = current
              current: Node[T] = current.next
              if current.data == data:
                previous.next: Node[T] = current.next
                return

          def display(self) -> None:
            if not self.head: return
            elements: list[str[T]] = list()
            current: Node[T] = self.head
            while True:
              elements.append(str(current.data))
              if (current := current.next) == self.head: break
            print(" -> ".join(elements) + f" -> (Back to Head: {self.head.data})")

          def prepend(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              node.next: Node[T] = self.head
              return
            current: Node[T] = self.head
            while current.next != self.head:
              current: Node[T] = current.next
            node.next: Node[T] = self.head
            current.next: Node[T] = node
            self.head: Node[T] = node


.. _Singly Linked Lists: ../singly