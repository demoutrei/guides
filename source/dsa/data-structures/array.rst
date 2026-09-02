Arrays
======

An array is a fundamental, linear data structure that stores a collection of elements of the same data type in contiguous (adjacent) memory locations. Because elements are stored in a continuous block, each item can be directly identified and accessed using a numerical **index**, typically starting at 0.

.. admonition:: Key Characteristics
    :class: hint

    Homogeneous Elements
      Every item in the array must be of the identical data type, meaning each element occupies the exact same number of bytes in memory.

    Contiguous Allocation
      Elements are physically arranged right next to each other in the system memory (RAM).

    Fixed Size
      Standard (static) arrays require their total size to be defined at the time of creation, and this total capacity cannot be dynamically changed later.


Advantages and Limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Advantages

        Fast Access
          Instant :math:`O(1)` random access to any element via its index.

        Cache Friendly
          Contiguous memory layout maximizes the system's spatial locality of reference.

        Low Overhead
          Requires no extra memory tracking pointers like linked lists do.


    .. grid-item-card:: Limitations

        Fixed Size
          Can result in wasted space if over-allocated, or running out of room if under-allocated.

        Costly Modifications
          Inserting or deleting elements from the middle is slow due to heavy element shifting.

        Memory Fragmentation
          Requires one large, unbroken chunk of memory, which might be blocked even if total free RAM exists.


Time Complexities
^^^^^^^^^^^^^^^^^

The structure of an array makes looking up specific locations incredibly fast, while modifying the structure itself remains highly inefficient.

Access (by index): :math:`O(1)`
  Constant time.

Search (by value): :math:`O(n)`
  Linear time for unsorted arrays, or :math:`O(log n)` for sorted arrays using binary search.

Insertion: :math:`O(n)`
  Linear time; inserting an item in the middle requires shifting all subsequent elements down.

Deletion: :math:`O(n)`
  Linear time; moving an item requires shifting all remaining elements up to fill the gap.


Visualization
^^^^^^^^^^^^^

.. figure:: https://i0.wp.com/studyalgorithms.com/wp-content/uploads/2020/12/Screenshot-2020-10-28-230925.png?resize=512%2C149&ssl=1
    :align: center
    :width: 80%

    *Source*: `Study Algorithms <https://studyalgorithms.com/array/array-data-structure/>`_


Implementation
^^^^^^^^^^^^^^

.. tabs::

    .. code-tab:: c++

        #include <iostream>
        #include <vector>
        
        void insert(int array[], int *size, int index, int value) {
          // Shift elements to the right
          for (int i = *size; index < i; i--) {
            array[i] = array[i - 1];
          }
          
          // Insert new element
          array[index] = value;

          // Increase active element count;
          (*size)++;
        }

        void remove(int array[], int *size, int index) {
          if (index < 0 || *size <= index) return;
          
          // Shift elements to the left
          for (int i = index; i < (*size - 1); ++i) {
            array[i] = array[i + 1];
          }

          // Reduce the active element count;
          (*size)--;
        }
        
        template <int size>
        int search(int (&array)[size], int target) {
          for (int i = 0; i < size; i++) {
            if (array[i] == target) return i; // target found
          }
          return -1; // target not found
        }
        
        int main() {
          // Declare and initialize
          int array[] = { 1, 2, 3 };
          int array_size { sizeof(array) / sizeof(array[0]) }; // 3

          // Access
          array[1]; // 2

          // Search
          search(array, 2); // 1

          // Insertion
          insert(array, &array_size, 3, 4); // { 1, 2, 3, 4 }

          // Deletion
          remove(array, &array_size, 3); // { 1, 2, 3 }
        }


    .. code-tab:: py

        class Array[T]:
          def __getitem__(self, index: int) -> tuple[T, ...]:
            if not isinstance(index, int):
              raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
            return self.__values[index]
        
          def __init__(self, *values: T) -> None:
            self.__values: tuple[T, ...] = tuple()
            for value in values:
              self.insert(value)

          def insert(self, value: T, /, *, index: int = -1) -> None:
            """Inserts a value in a specific index, defaults to the end of the array."""
            if value is None: return
            value_type: Optional[type] = None
            if self.__values:
              value_type: type = type(self.__values[0])
            if not isinstance(value, value_type):
              raise TypeError(f"value: Must be an instance of {value_type}; not {value.__class__}")
            if not isinstance(index, int):
              raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
            if index < 0:
              if (self.size + 1) < abs(index):
                index: int = -1
              index: int = self.size + index
            self.__values: tuple[T, ...] = (*self.__values[:index], value, *self.__values[index + 1:])

          def remove(self, index: int = -1) -> T:
            if not isinstance(index, int):
              raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
            if index < 0:
              if (self.size + 1) < abs(index):
                index: int = -1
              index: int = self.size + index
            if self.size < (index + 1):
              raise IndexError(f"{index}")
            removed_value: T = self[index]
            self.__values: tuple[T, ...] = (*self.__values[:index], *self.__values[index + 1:])
            return removed_value

          def search(self, value: T) -> int:
            """Returns the index of the value, otherwise -1 if not found."""
            if not self.__values: return -1
            value_type: type = type(self.__values[0])
            if not isinstance(value, value_type):
              raise TypeError(f"value: Must be an instance of {value_type}; not {value.__class__}")
            for index, item in enumerate(self.__values):
              if item == value:
                return index
            return -1

          def size(self) -> int:
            """Returns the size of the array."""
            return len(self.__values)
            

        array: Array[int] = Array(1, 2, 3)

        # Access
        array[1] # 2

        # Search
        array.search(2) # 1
        array.search(5) # -1

        # Insertion
        array.insert(4) # ( 1, 2, 3, 4 )

        # Deletion
        array.remove(3) # ( 1, 2, 4 )