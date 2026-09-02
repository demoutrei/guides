Singly Linked List
==================

A **singly linked list** is a linear data structure where elements are stored in individual objects called **nodes**, and each node points to the next consecutive node via a reference pointer. Unlike `arrays <../array>`_, elements are not stored in contiguous memory locations, allowing for dynamic memory allocation.


Advantages and Limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Advantages

        Dynamic Size
          Memory grows and shrinks on demand during runtime without needing pre-allocation.

        Cheap Insert/Delete
          Modifying items at known locations only changes pointer connections rather than shifting memory.


    .. grid-item-card:: Disadvantages

        No Random Access
          You cannot query elements directly by index (like ``array[4]``); you must iterate sequentially.

        Memory Overhead
          Every node requires extra storage space strictly to house its pointer address.

        Forward-Only
          You cannot traverse backward without building copmlex reversal logic.


Node Structure
^^^^^^^^^^^^^^

Every node in a singly linked list contains exactly two components:

Data
  The actual value or information being stored.

Next Pointer
  A reference variable storing the memory address of the next node.


To control and exit the structure, three main anchors are used:

Head
  A reference pointer pointing to the first node, serving as the list's entry point.

Tail
  An optional pointer referencing the final node to enable quick appending.

Null Terminator
  The ``Next`` pointer of the final node points to ``Null``, marking the end of the sequence.


Time Complexity of Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The unidirectional design significantly impacts the performance of common manipulations.

Access/Search: :math:`O(n)`
  Must traverse linearly from the head node.

Prepend (Insert Front): :math:`O(1)`
  Update head pointer; no element shifting required.

Append (Insert Back): :math:`O(1)` or :math:`O(n)`
  :math:`O(1)` if a tail pointer exists; :math:`O(n)` if you must traverse to find the end.

Delete Front: :math:`O(1)`
  Advance the head pointer to the second node.

Delete Back: :math:`O(n)`
  Requires traversing to the second-to-last node to clear its link.


Visualization
^^^^^^^^^^^^^

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20250619155958124670/Linked-list.webp
    :align: center
    :width: 80%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/dsa/linked-list-data-structure/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

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

            ~LinkedList() {
              clear();
            }

            void append(int data) {
              Node *node = new Node(data);
              if (head == nullptr) {
                head = node;
                return;
              }
              Node *current = head;
              while (current->next != nullptr) {
                current = current->next;
              }
              current->next = node;
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
              if (head == nullptr) return;
              if (head->data == data) {
                Node *current = head;
                haed = head->next;
                delete current;
                return;
              }
              Node *current = head;
              while (current->next != nullptr && current->next->data != data) {
                current = current->next;
              }
              if (current->next != nullptr) {
                Node *node = current->next;
                current->next = current->next->next;
                delete node;
              }
            }

            void display() {
              Node *current = head;
              while (current != nullptr) {
                std::cout << current->data << " -> ";
                current = current->next;
              }
              std::cout << "nullptr" << std::endl;
            }
            
            void prepend(int data) {
              Node *node = new Node(data);
              node->next = head;
              head = node;
            }

            bool search(int data) {
              Node *current = head;
              while (current != nullptr) {
                if (current->data == data) return true;
                current = current->next;
              }
              return false;
            }
        };


    .. code-tab:: py

        class Node[T]:
          def __init__(self, data: T) -> None:
            self.data: T = data
            self.next: Node[T] = None

        class LinkedList[T]:
          def __init__(self) -> None:
            self.head: Optional[Node[T]] = None

          def append(self, data: T) -> None:
            node: Node[T] = Node(data)
            if not self.head:
              self.head: Node[T] = node
              return
            current: Optional[Node[T]] = self.head
            while current.next:
              current: Optional[Node[T]] = current.next
            current.next: Node[T] = node

          def delete(self, data: T) -> None:
            current: Optional[Node[T]] = self.head
            if current and current.data == data:
              self.head: Node[T] = current.next
              current: Optional[Node[T]] = None
              return
            previous: Optional[Node[T]] = None
            while current and current.data != data:
              previous: Node[T] = current
              current: Optional[Node[T]] = current.next
            if not current:
              print(f"IndexError: {index}")
              return
            previous.next: Optional[Node[T]] = current.next
            current: Optional[Node[T]] = None

          def display(self) -> None:
            elements: list[str[T]] = list()
            current: Optional[Node[T]] = self.head
            while current:
              elements.append(str(current.data))
              current: Optional[Node[T]] = current.next
            print(f" -> ".join(elements) + " -> None")

          def prepend(self, data: T) -> None:
            node: Node[T] = Node(data)
            node.next: Node[T] = self.head
            self.head: Node[T] = node

          def search(self, data: T) -> bool:
            current: Optional[Node[T]] = self.head
            while current:
              if current.data == data: return True
              current: Optional[Node[T]] = current.next
            return False