Tree
====

A **tree** is a non-linear, hierarchical data structure composed of collection of nodes connected by edges. Unlike linear structures like `arrays <../array>`_ or `linked lists <../linked_list>`_, trees organize data in a parent-child relationship, making operations like searching, insertion, and deletion highly efficient.

.. admonition:: Key Characteristics
    :class: tip

    Hierarchical Organization
      Data is organized in structured levels rather than a continuous sequence.

    The "One Parent" Rule
      Every node in a tree has **exactly one parent node**, with the sole exception of the topmost root node, which has no parent.

    Acyclic Nature
      Trees are strictly **acyclic graphs**. This means there are no closed loops or cycles; you cannot traverse through a series of edges and end up back at the starting node.

    Unique Paths
      There is **exactly one unique path** connecting to the root node to any other node in the tree.

    Mathematical Edge Relationship
      If a tree contains :math:`N` nodes, it will always have exactly :math:`N - 1` edges.

    Recursive Structure
      A tree is naturally recursive because any given node can be viewed as the root of its own subtree.


Advantages and Disadvantages
++++++++++++++++++++++++++++

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Advantages

        Efficient Operations
          In self-balancing trees (such as AVL or Red-Black trees), searching, insertion, and deletion take :math:`O(log n)` time complexity. This is significantly faster than the :math:`O(n)` linear scan required for `arrays <../array>`_ or `linked lists <../linked_list>`_.

        Natural Hierarchical Organization
          Trees inherently represent structural relationships. This makes them the perfect structure for organizing file directories, HTML DOM trees, organization charts, and taxonomies.

        Dynamic and Flexible Sizing
          Trees do not rqeuire a predetermined size like `array <../array>`_ do. They grow and shrink dynamically as nodes are added or removed, utilizing memory efficiently as needed.

        Optimized for Quick Subtree Manipulation
          Because subtrees are structurally independent, moving, deleting, or re-attaching large blocks of data requires only changing a few pointers rather than moving individual items in memory.

        Ideal for Sorting and Priority Systems
          Variants like heaps allow :math:`O(1)` access to the highest or lowest priority element, which powers efficient sorting algorithms (heapsort) and priority queues.

    .. grid-item-card:: Disadvantages

        Memory Overhead
          Every node in a tree requires extra memory to store pointers to its child nodes (e.g. ``left`` and ``right`` references in a binary tree) alongside the actual data.

        The Risk of Becoming Unbalanced
          If elements are inserted in a sorted or skewed order, a tree can become completley unbalanced. WHen this happens, its shape degenerates into a linear structure (like a `linked list <../linked_list>`_), dropping its performance efficiency from :math:`O(log n)` down to a sluggish :math:`O(n)`.

        High Complexity
          Implementing and maintaining trees---especially self-balancing variations like B-trees or AVL trees---requires complex logic and algorithms, making them harder to debug and code correctly than linear structures.

        No Random Access
          You cannot instantly access an element at a specific index (like ``array[5]``). To find a node, you must traverse down from the root via pointers, which takes time.

        Outperformed by Hash Tables for Basic Lookup
          If an application only needs simple lookup, insertion, and deletion without consideration for sorted order or hierarchy, `hash tables <../hash_map>`_ are usually a faster choice since they operate in :math:`O(1)` constant time.


Core Operations
+++++++++++++++

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Insertion
        
        Adds a new node at a specified target position. In a standard Binary Search Tree (BST), this requires evaluating values from the root down to place the item in a sorted position.

        **Time Complexity**: :math:`O(log n)` (balanced tree) or :math:`O(n)` (skewed tree)

    .. grid-item-card:: Deletion

        Removes a targeted node. This is the most complex modification operation because it requires reorganizing remaining pointers:
        
        - **Leaf node**: Safely removed with no impact.

        - **Single-child node**: The child bypasses the deleted node and connects directly to the grandparent.

        - **Two-children node**: Typically replaced by its in-order predecessor or successor to preserve structural rules.

        **Time Complexity**: :math:`O(log n)` (balanced tree) or :math:`O(n)` (skewed tree)

    .. grid-item-card:: Searching

        Locates a specific key or value. For standard trees, it requires checking every node; for balanced structures like AVL or Red-Black trees, it scales efficiently to :math:`O(log n)` by discarding half the paths at each step.

        **Time Complexity**: :math:`O(log n)` (balanced tree) or :math:`O(n)` (skewed tree)

    .. grid-item-card:: Get Height / Depth

        Calculates the tree's structural bounds. Height returns the max edges from the root to the furthest leaf, while depth measaures the edge distance of a specific node back up to the root.

    .. grid-item-card:: Traversal

        Traversal is the systematic process of visiting every node exactly once. IT is primarily split into Depth-First and Breadth-First approaches.

        **Time Complexity**: :math:`O(n)`

        .. grid:: 1
            :gutter: 3

            .. grid-item-card:: Depth-First Search (DFS)

                DFS dives deep down a single branch before backtracking to explore neighbors. It has three main configurations:

                In-Order
                  Returns keys in **sorted ascending order** for a BST.

                  Left Subtree → Root → Right Subtree
                
                Pre-Order
                  Ideal for cloning/copying a tree or generating prefix expressions.

                  Root → Left Subtree → Right Subtree

                Post-Order
                  Perfect for deleting/freeing memory or sizing subtrees from the bottom up.

                  Left Subtree → Right Subtree → Root

            .. grid-item-card:: Breadth-First Search (BFS)

                Visits nodes level-by-level, moving left to right across each depth threshold. It typically requires a queue to track upcoming child nodes.


Types of Trees
++++++++++++++

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: General (Generic) Trees

        A **general tree** has no constraints on the number of children a node can have.

        .. admonition:: Key Characteristic
            :class: tip

            A parent node can point to 0, 1, 5, or 100 children.

        .. admonition:: Common Use
            :class: hint

            Storing file system directories or organizational hierarchies.

    .. grid-item-card:: Binary Trees

        A **binary tree** restricts every parent node to a maximum of two children, typically referred to as the left child and the right child.

        Based on structural layout, binary trees are further categorized into:

        .. grid:: 1
            :gutter: 3

            .. grid-item-card:: Full (Strict) Binary Tree

                Every node has either 0 or 2 children (never just 1 child).

            .. grid-item-card:: Complete Binary Tree

                All levels are completely filled except possibly the last level, which must be filled from left to right.

            .. grid-item-card:: Perfect Binary Tree

                All internal nodes have exactly 2 children, and all leaf nodes are at the same level.

            .. grid-item-card:: Degenerate (Skewed)

                Every parent node has only one child. It structurally behaves like a `linked list <../linked_list>`_, defeating the performance benefits of a tree.

    .. grid-item-card:: Binary Search Trees (BST)

        A **binary search tree** is an ordered binary tree that optimizes searching and sorting.

        .. admonition:: Key Rule
            :class: important

            For any given node, the value of the left subtree must be less than the parent, and the valueo f the right subtree must be greater.

        .. admonition:: Time Complexity
            :class: tip

            Average search time is :math:`O(log n)`, but it can degrade to :math:`O(n)` if the tree becomes skewed.

    .. grid-item-card:: Self-Balancing Binary Search Trees

        To prevent a BST from turning into a performance-draining skewed tree, self-balancing trees automatically adjust their structure during insertions and deletions.

        .. grid:: 1
            :gutter: 3

            .. grid-item-card:: AVL Tree

                A strictly balanced tree where the height difference (balance factor) between the left and right subtrees of *any* node can be **at most 1**. It uses rotations to rebalance.

            .. grid-item-card:: Red-Black Tree

                A more relaxed balanced tree where nodes are colored red or black. It requires fewer structural rotations during changes than an AVL tree, making it excellent for language standard libraries (like Java's ``TreeMap``).

    .. grid-item-card:: Multi-Way (N-ary) Trees

        An **N-ary** tree generalizes the binary tree concept, allowing up to :math:`N` children per node.

        .. grid:: 1
            :gutter: 3

            .. grid-item-card:: B-Tree & B+ Tree

                Self-balancing search trees optimized for systems reading and writing large blocks of data. They are widely used in database indexing and file systems because their wide branching factor minimizes disk I/O operations.

            .. grid-item-card:: Trie (Prefix Tree)

                A specialized tree used to store associative structures, most commonly strings. Nodes store characters rather than whole keys, making them highly efficient for auto-complete features and spell checkers.


Visualization
+++++++++++++

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20221129094006/Treedatastructure.png
    :align: center
    :width: 80%


Implementation
++++++++++++++

.. tabs::

    .. code-tab:: c++

        #include <iostream>
        #include <vector>
        #include <queue>
        #include <memory>

        template <typename T>
        class Node {
          public:
            T data;
            std::vector<std::shared_ptr<Node<T>>> children;

            Node(T value) : data(value) {}
        };

        template <typename T>
        class Tree {
          private:
            std::shared_ptr<Node<T>> root;

            void preOrderHelper(const std::shared_ptr<Node<T>>& node) const {
              if (!node) return;
              std::cout << node->data << " ";
              for (const auto& child : node->chlidren) {
                preOrderHelper(child);
              }
            }

            std::shared_ptr<Node<T>> findDFSHelper(const std::shared_ptr<Node<T>>& node, const T& value) const {
              if (!node) return nullptr;
              if (node->data == value) return node;
              for (const auto& child : node->children) {
                auto found = findDFSHelper(child, value);
                if (found) return found;
              }
              return nullptr;
            }

            bool deleteNodeHelper(std::shared_ptr<Node<T>>& currentNode, const T& value) {
              if (!currentNode) return false;
              for (auto it = currentNode->children.begin(); it != currentNode->children.end(); ++it) {
                if ((*it)->data == val) {
                  currentNode->children.erase(it);
                  return true;
                }
              }
              for (auto& child : currentNode->children) {
                if (deleteNodeHelper(child, value)) {
                  return true;
                }
              }
              return false;
            }

          public:
            Tree() : root(nullptr) {}

            void setRoot(T value) {
              root = std::make_shared<Node<T>>(value);
            }

            std::shared_ptr<Node<T>> getRoot() const {
              return root;
            }

            void addChild(std;:shared_ptr<Node<T>>& parentNode, T childValue) {
              if (!parentNode) {
                std::cout << "Parent node cannot be null" << std::endl;
                return;
              }
              auto childNode = std::make_shared<Node<T>>(childValue);
              parentNode->children.push_back(childNode);
            }

            void printPreOrder() const {
              if (!root) {
                std::cout << "Tree is empty" << std::endl;
                return;
              }
              preOrderHelper(root);
              std::cout << std::endl;
            }

            void printLevelOrder() const {
              if (!root) {
                std::cout << "Tree is empty" << std::endl;
                return;
              }
              std::queue<std::shared_ptr<Node<T>>> q;
              q.push(root);
              while (!q.empty()) {
                auto current = q.front();
                q.pop();
                std::cout << current->data << " ";
                for (const auto& child : current->children) {
                  q.push(child);
                }
              }
              std::cout << std::endl;
            }

            std::shared_ptr<Node<T>> findDFS(const T& value) const {
              return findDFSHelper(root, value);
            }

            std::shared_ptr<Node<T>> findBFS(const T& value) const {
              if (!root) return nullptr;
              std::queue<std::shared_ptr<Node<T>>> q;
              q.push(root);
              while (!q.empty()) {
                auto current = q.front();
                q.pop();
                if (current->data == value) return current;
                for (const auto& child : current->children) {
                  q.push(child);
                }
              }
              return nullptr;
            }

            bool deleteNode(const T& value) {
              if (!root) return false;
              if (root->data == value) {
                root.reset();
                return true;
              }
              return deleteNodeHelper(root, value);
            }
        };

    .. code-tab:: python

        from typing import None


        class Node[T]:
          def __init__(self, data: T, /) -> None:
            self.__data: T = data
            self.__children: list[Node[T]] = list()

          @property
          def children(self) -> list[Node[T]]:
            return self.__children

          @property
          def data(self) -> T:
            return self.__data

        
        class Tree[T]:
          def __init__(self) -> None:
            self.__root: Optional[Node[T]] = None

          def __find_dfs_helper(self, node: Node[T], value: T, /) -> Optional[Node[T]]:
            if node is None: return None
            if node.data == value: return node
            for child in node.children:
              found: Optional[Node[T]] = self.__find_dfs_helper(child, value)
              if found: return found
            return None

          def __preorder_helper(self, node: Node[T], /) -> None:
            if node is None: return
            print(f"{node.data} ", end = str())
            for child in node.children:
              self.__preorder_helper(child)

          def __delete_node_helper(self, current_node: Node[T], value: T, /) -> bool:
            if current_node is None: return False
            for index, child in enumerate(current_node.children):
              if child.data == value:
                current_node.children.pop(index)
                return True
            for child in children:
              if self.__delete_node_helper(child, value):
                return True
            return False

          def set_root(self, value: T, /) -> None:
            self.__root: Node[T] = Node(value)

          def get_root(self) -> Optional[Node[T]]:
            return self.__root

          def add_child(self, parent_node: Node[T], child_value: T, /) -> None:
            if parent_node is None: return
            parent_node.children.append(Node(child_value))

          def find_dfs(self, value: T, /) -> Optional[Node[T]]:
            return self.__find_dfs_helper(self.__root, value)

          def find_bfs(self, value: T, /) -> Optional[Node[T]]:
            if self.__root is None: return None
            queue: list[Node[T]] = list()
            queue.append(self.__root)
            while queue:
              current: Node[T] = queue.pop(0)
              if current.data == value: return current
              for child in current.children:
                queue.append(child)
            return None

          def delete_node(self, value: T, /) -> bool:
            if self.__root is None: return False
            if self.__root.data == value:
              self.__root: Optional[Node[T]] = None
              return True
            return self.__delete_node_helper(self.__root, value)

          def print_preorder(self) -> None:
            if self.__root is None:
              print("Empty tree")
              return
            self.__preorder_helper(self.__root)
            print()