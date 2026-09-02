Circular Doubly Linked List
===========================

A **circular doubly linked list** is a complex linear data structure where each node contains a data field and two pointers (``next`` and ``previous``), and the list forms a continuous loop. Specifically, the ``next`` pointer of the last node points back to the first node, and the ``previous`` pointer of the first node points back to the last node.


.. admonition:: Key Characteristics
    :class: tip

    Bidirectional Traversal
      The concurrent presence of ``next`` and ``previous`` pointers allows you to seamlessly traverse the structure both forward and backward.

    Perfect Circularity
      The ``next`` pointer of the final node links directly back to the first node (head). Conversely, the ``previous`` pointer of the head node references the final node.

    Absence of Null References
      Unlike `linear linked lists <../>`_, this data structure completely eliminates null markers. Every pointer constantly resolves to a valid node address.

    Instant Endpoint Access
      Because the head node holds a direct path to the tail via its ``previous`` pointer, you can access or modify either end of the list in :math:`O(1)` constant time without performing sequential lookups.

    Memory Overhead
      This flexibility requires a higher memory allocation footprint because each node must accommodate two distinct pointer variables alongside the user data.

    Infinite Looping Risks
      Code loops can execute infinitely if exit conditions do not explicitly watch for the recurrence of the initial starting node.


Advantages and Disadvantages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Advantages

        Full Bidirectional Traversal
          You can seamlessly step forward (``next``) or backward (``previous``) through the data pool from any starting node.

        Instant Back-and-Forth Loops
          You can jump from the first item to the last item (and vise versa) in a single step (:math:`O(1)` time).
        
        No Null Pointer Exceptions
          The continuous loop structure eliminates code errors caused by accidentally dereferencing an unmapped boundary pointer.


    .. grid-item-card:: Disadvantages

        Higher Memory Footprint
          Every item must store two dedicated pointer addresses alongside its actual payload data.

        Complicated Pointer Management
          Implementation logic is prone to bugs. Modifying or removing a single node requires changing four distinct pointer references.

        Tricky Termination Conditions
          Traditional loops checking for ``while(current != nullptr)`` will result in infinite loops. Code must check if ``current == head`` to safely stop.


Time Complexities of Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Insertion at Beginning/End: :math:`O(1)`
  You can instantly grab the last node using ``Head->prev`` and adjust the 4 boundary pointers to bridge the new node into the loop.

Insertion at Specific Position: :math:`O(n)`
  Requires traversing to the target index before adjusting pointers.

Deletion from Beginning/End: :math:`O(1)`
  Modifying the connections between the head and tail takes constant time since no linear scanning is required.

Deletion of a Specific Node: :math:`O(n)`
  Requires a linear search to find the value before splicing it out.

Traversal: :math:`O(n)`
  Because there are no ``Null`` pointers, a traversal loop must stop when the iterator pointer circles back and equals the ``Head`` pointer.


Visualization
^^^^^^^^^^^^^

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20220830114920/doubly-660x177.jpg
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/dsa/introduction-to-circular-doubly-linked-list/>`_


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

          public:
            LinkedList() : head(nullptr) {}
          
            void append(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                node->next = head;
                node->previous = head;
                return;
              }
              Node *tail = head->previous;
              tail->next = node;
              node->previous = tail;
              node->next = head;
              head->previous = node;
            }

            void prepend(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                node->next = head;
                node->previous = head;
                return;
              }
              Node *tail = head->previous;
              node->next = head;
              node->previous = tail;
              tail->next = node;
              head->previous = node;
              head = node;
            }

            void deleteNode(int data) {
              if (head == nullptr) return;
              Node *current = head;
              while (true) {
                if (current->data == data) {
                  if (current->next == head && current->previous == head) {
                    head = nullptr;
                    delete current;
                    return;
                  }
                  current->previous->next = current->next;
                  current->next->previous = current->previous;
                  if (current == head) {
                    head = current->next;
                  }
                  delete current;
                  return;
                }
                current = current->next;
                if (current == head) break;
              }
            }

            void displayForward() {
              if (head == nullptr) return;
              Node *current = head;
              while (true) {
                std::cout << current->data << " -> ";
                current = current->next;
                if (current == head) break;
              }
              std::cout << "(loops back to head)" << std::endl;
            }

            void displayBackward() {
              if (head == nullptr) return;
              Node *current = head->previous;
              while (true) {
                std::cout << current->data << " -> ";
                current = current-> previous;
                if (current == head->previous) break;
              }
              std::cout << "(loops back to tail)" << std::endl;
            }
        };


    .. code-tab:: py

        class Node[T]:
          def __init__(self, data: T) -> None:
            self.data: T = data
            self.next: Optional[Node[T]] = None
            self.previous: Optional[Node[T]] = None

        class LinkedList[T]:
          def __init__(self) -> None:
            self.head: Optional[Node[T]] = None

          def append(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              node.next: Node[T] = self.head
              node.previous: Node[T] = self.head
              return
            tail: Node[T] = self.head.previous
            tail.next: Node[T] = node
            node.previous: Node[T] = tail
            node.next: Node[T] = self.head
            self.head.previous: Node[T] = node

          def prepend(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              node.next: Node[T] = self.head
              node.previous: Node[T] = self.head
              return
            tail: Node[T] = self.head.previous
            node.next: Node[T] = self.head
            node.previous: Node[T] = tail
            tail.next: Node[T] = node
            self.head.previous: Node[T] = node
            self.head: Node[T] = node

          def delete(self, data: T) -> None:
            if not self.head: return
            current: Node[T] = self.head
            while True:
              if current.data == data:
                if current.next == self.head == current.previous:
                  self.head: Optional[Node[T]] = None
                  return
                current.previous.next: Node[T] = current.next
                current.next.previous: Node[T] = current.previous
                if current == self.head:
                  self.head: Node[T] = current.next
                return
              current: Node[T] = current.next
              if current == self.head: break

          def display_forward(self) -> None:
            if not self.head: return
            current: Node[T] = self.head
            elements: list[str[T]] = list()
            while True:
              elements.append(str(current.data))
              current: Node[T] = current.next
              if current == self.head: break
            print(f"{" -> ".join(elements)} -> (loops back to head")

          def display_backward(self) -> None:
            if not self.head: return
            current: Node[T] = self.head.previous
            elements: list[str[T]] = list()
            while True:
              elements.append(str(current.data))
              current: Node[T] = current.previous
              if current == self.head.previous: break
            print(f"{" -> ".join(elements)} (loops back to tail)")