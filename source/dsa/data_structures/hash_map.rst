Hash Map
========

A **hash map** (also known as a **hash table**, **dictionary**, or **associative array**) is a fundamental data structure designed to store key-value pairs. It provides an incredibly fast average time complexity of :math:`O(1)` for insertion, lookup, and deletion, making it one of the most efficient tools for data retrieval.

.. admonition:: How It Works
    :class: tip

    1. **The Hash Function**: When you pass a key into the map, it goes through a **hash function**. This function translates the key (which could be a string, integer, or object) into a numeric hash code.

    2. **Bucket Mapping**: The map converts this hash code into a valid array index (often using the modulo operator relative to the array's size).

    3. **Direct Storage**: The key-value pair is stored inside that specific index, known as a **bucket** or **slot**. When you lookup a key later, the map recalculates the index and jumps straight to it, skipping the need to iterate through the entire dataset.

.. admonition:: Key Characteristics
    :class: tip

    Key-Value Pair Storage
      Data is stored in entries consisting of a **key** (a unique identifier) and a **value** (the data associated with that key).

    Unordered Collection
      Hash maps do not guarantee any specific order of their elements. The insertion order is typically lost because elements are positioned based on their hash codes rather than a sequential sequence.

    Unique Keys
      Every key in a hash map **must be unique**. If you attempt to insert a duplicate key, the map will typically overwrite the existing value associated with that key. Values, however, can be duplicated across different keys.

    Constant :math:`O(1)` Time Complexity
      Under optimal conditions, basic operations like insertion, deletion, and lookup take :math:`O(1)` constant time. This means the time to find an element remains the same regardless of how large the dataset grows.

    Dependency on a Hash Function
      A hash map uses a mathematical hash function to convert the key into a numeric hash code, which is then mapped to an array index (or bucket) where the value is stored.

    Collision Handling
      Because multiple unique keys can theoretically generate the same array index (a **collission**), hash maps rely on internal resolution mechanisms like **chaining** (using linked lists or trees within buckets) or **open addressing** (searching for the next empty bucket).

    Dynamic Resizing and Load Factor
      Performance drops if the map gets too full. Hash maps track a **load factor** (the ratio of occupied slots to total capacity) and will automatically double their array size and rehash all entries once a threshold (commonly 0.75) is crossed.


Advantages and Disadvantages
++++++++++++++++++++++++++++

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Advantages

        Near-Instance Search, Insertion, and Deletion
          Operations run at an average time complexity of :math:`O(1)`. A hash function calculates the exact memory index of a key directly, eliminating the need to iterate through elements or search down balanced trees.

        High Flexibility
          Keys are not restricted to sequential integers like array indices. You can use strings, objects, or other data types to model real-world relationships natively (e.g. mapping a username to a profile object).

        Enforced Key Uniqueness
          Hash maps naturally prevent duplicate keys. Attempting to insert an existing key simply overwrites the old value, which makes deduplication straightforward.

        Dynamic Resizing
          Most modern programming languages implement built-in hash maps that automatically scale their inner capacity outward once data density triggers a certain threshold.

    .. grid-item-card:: Disadvantages

        Worst-Case Performance Degradation
          If multiple keys generate the identical hash index (a conflict known as a **hash collision**), the map must fall back to collision resolution strategies like linked list chaining or open addressing. In server scenarios---such as a malicious "Hash DoS" exploit targeting data patterns---lookups can collapse to an inefficient worst-case time complexity of :math:`O(n)`.

        No Element Ordering
          Hash maps are inherently **unordered**. The placement of entries fluctuates based on the hash function's output rather than insertion order or value weight. If your workflow demands sorted data or predictable iterations, alternative structures like Tree Map or Linked Hash Map are required.

        Higher Memory Footprint
          Hash maps sacrifice spatial efficiency to maintain oeprational speed. They require spare, unoccupied memory slots (buckets) to prevent collision bottlenecks, resulting in larger memory requirements than packed arrays or linked lists.

        Costly Resizing Overhead
          While resizing ensures long-term operational speed, the transition itself is computationally expensive. The entire array must expand, and every existing key must be systematically rehashed and repositioned into new buckets.


Core Operations
+++++++++++++++

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Insertion

        Adds a new key-value pair to the map. If the key already exists, its value is updated.

        **Average Time**: :math:`O(1)`

        **Worst-Case Time**: :math:`O(n)` or :math:`O(log n)`

    .. grid-item-card:: Lookup

        Retrieves the value associated with a specific key.

        **Average Time**: :math:`O(1)`

        **Worst-Case Time**: :math:`O(n)` or :math:`O(log n)`

    .. grid-item-card:: Deletion

        Deletes a key-value pair from the map based on the provided key.

        **Average Time**: :math:`O(1)`

        **Worst-Case Time**: :math:`O(n)` or :math:`O(log n)`


Visualization
+++++++++++++

.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20251025124952963087/hashmap.webp
    :align: center
    :width: 80%


Implementation
++++++++++++++

.. tabs::

    .. code-tab:: c++

        #include <iostream>
        #include <list>
        #include <string>
        #include <stdexcept>
        #include <utility>
        #include <vector>

        template <typename K, typename V>
        class HashMap {
          private:
            struct Node {
              K key; V value;
              Node(K k, V v) : key(k), value(v) {}
            };
            std::vector<std::list<Node>> buckets;
            size_t totalElements;
            const double MAX_LOAD_FACTOR = 0.75;

            size_t getBucketIndex(const K& key) const {
              std::hash<K> hasher;
              return hasher(key) % buckets.size();
            }

            void rehash() {
              size_t oldCapacity = buckets.size();
              auto oldBuckets = std::move(buckets);
              buckets.resize(old_capacity * 2);
              totalElements = 0;
              for (auto& chain : oldBuckets) {
                for (auto& node : chain) {
                  insert(node.key, node.value);
                }
              }
            }

          public:
            HashMap(size_t initialCapacity = 16) : totalElements(0) {
              buckets.resize(initialCapacity);
            }

            void insert(const K& key, const V& value) {
              size_t index = getBucketIndex(key);
              for (auto& node : buckets[index]) {
                if (node.key == key) {
                  node.value = value;
                  return;
                }
              }
              buckets[index].emplace_back(key, value);
              totalElements++;
              if (MAX_LOAD_FACTOR < static_cast<double>(totalElements) / buckets.size()) {
                rehash();
              }
            }

            V get(const K& key) const {
              size_t index = getBucketIndex(key);
              for (const auto& node : buckets[index]) {
                if (node.key == key) {
                  return node.value;
                }
              }
              throw std::out_of_range("Key not found in hash map.");
            }

            bool remove(const K& key) {
              size_t index = getBucketIndex(key);
              auto& chain = buckets[index];
              for (auto it = chain.begin(); it != chain.end(); ++it) {
                if (it->key == key) {
                  chain.erase(it);
                  totalElements--;
                  return true;
                }
              }
              return false;
            }

            bool contains(const K& key) {
              size_t index = getBucketIndex(key);
              for (const auto& node : buckets[index]) {
                if (node.key == key) return true;
              }
              return false;
            }

            size_t size() const {
              return totalElements;
            }

            size_t capacity() const {
              return buckets.size();
            }

            bool isEmpty() const {
              return totalElements == 0;
            }
        };

    .. code-tab:: python

        from copy import deepcopy

        class Node[K, V]:
          def __init__(self, key: K, value: V, /) -> None:
            self.key: K = key
            self.value: V = value

        class HashMap[K, V]:
          def __init__(self, initial_capacity: int = 16, /) -> None:
            self.__initial_capacity: int = initial_capacity
            self.__buckets: list[list[Node]] = [list() for _ in range(initial_capacity)]
            self.__total_elements: int = 0
            self.__MAX_LOAD_FACTOR: float = 0.75

          def __get_bucket_index(self, key: K, /) -> int:
            return hash(key) % len(self.__buckets)

          def __rehash(self) -> None:
            old_capacity: int = len(self.__buckets)
            old_buckets: list[list[Node]] = deepcopy(self.__buckets)
            self.__buckets: list[list[Node]] = [list() for _ in range(old_capacity * 2)]
            self.__total_elements: int = 0
            for chain in old_buckets:
              for node in chain:
                self.insert(node.key, node.value)

          def insert(self, key: K, value: V, /) -> None:
            index: int = self.__get_bucket_index(key)
            for node in self.__buckets[index]:
              if node.key is key:
                node.value = value
                return
            self.__buckets[index].append(Node(key, value))
            self.__total_elements += 1
            if self.__MAX_LOAD_FACTOR < (self.__total_elements / len(self.__buckets)):
              self.__rehash()

          def get(self, key: K, /) -> V:
            index: int = self.__get_bucket_index(key)
            for node in self.__buckets[index]:
              if node.key is key:
                return node.value
            raise IndexError("Key not found in hash map")

          def remove(self, key: K, /) -> bool:
            index: int = self.__get_bucket_index(key)
            chain: list[Node] = self.__buckets[index]
            for index, node in enumerate(chain):
              if node.key is key:
                chain.pop(index)
                return True
            return False

          def contains(self, key: K, /) -> bool:
            index: int = self.__get_bucket_index(key)
            for node in buckets[index]:
              if node.key is key:
                return True
            return False

          @property
          def size(self) -> int:
            return self.__total_elements

          @property
          def capacity(self) -> int:
            return len(self.__buckets)

          def is_empty(self) -> bool:
            return self.__total_elements == 0