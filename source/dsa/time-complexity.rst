Time Complexity
===============

Time Complexity is a theoretical measure that quantifies the amount of time an algorithm takes to run as a function of the length of its input (:math:`n`). Instead of measuring actual seconds---which change based on hardware, compilers, and processors---time complexity counts the number of elementary operations or code statements executed.


Asymptotic Notations
^^^^^^^^^^^^^^^^^^^^

Algorithms can perform differently depending on the structure of the input data. We analyze them using three main bounds:


Worst-Case
~~~~~~~~~~

**Big O notation** :math:`O` is a mathematical metric used to describe the efficiency and performance of an algorithm. It measures how the execution time or space requirements grow relative to the input size (:math:`n`), specially representing the worse-case scenario (upper bound).


Best-Case
~~~~~~~~~

**Big Omega notation** :math:`Ω` defines the asymptotic lower bound of an algorithm's time complexity. It represents absolute minimum time or steps an algorithm requires to run for large input sizes. In simpler terms, it answers the question: "*At the very least, how fast will this algorithm grow?*".


Average-Case
~~~~~~~~~~~~

**Big Theta notation** :math:`Θ` defines a tight asymptotic bound on the execution time of an algorithm. Unlike `Big O <#worst-case>`_ (which provides a maximum boundary) or `Big Omega <#best-case>`_ (which provides a minimum boundary), Big Theta bounds a function from both above and below. This means the algorithm's actual performance scales precisely at the rate indicated by the bounding function as input size grows toward infinity.


Common Time Complexities
^^^^^^^^^^^^^^^^^^^^^^^^

Ordered by efficiency:


Constant Time :math:`O(1)`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Execution time remains the same regardless of input size.


.. admonition:: Common Examples
    :class: hint

    Accessing an array element by its index.


.. tabs::

    .. code-tab:: c++

        template <int size>
        int constant(int (&array)[size]) {
          return array[0];
        }


    .. code-tab:: py

        def constant(array: list[int]) -> int:
          return array[0]


Logarithmic Time :math:`O(log n)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The problem size is divided by a factor (usually halved) at each step.


.. admonition:: Common Examples
    :class: hint

    `Binary Search`_


.. tabs::

    .. code-tab:: c++

        int power(int base, int exponent) {
          int result { 1 };
          while (0 < exponent) {
            if (exponent % 2 == 1) {
              result *= base;
            }
            base *= base;
            exponent /= 2;
          }
          return result;
        }


    .. code-tab:: py

        def power(base: int, exponent: int) -> int:
          result: int = 1
          while 0 < exponent:
            if exponent % 2 == 1:
              result *= base
            base *= base
            exponent //= 2
          return result


Linear Time :math:`O(n)`
~~~~~~~~~~~~~~~~~~~~~~~~

Running time grows in direct proportion to the input size.

.. admonition:: Common Examples
    :class: hint

    A single loop traversing a list.


.. tabs::

    .. code-tab:: c++

        template <int size>
        void linear(int (&array)[size]) {
          for (int element : array) {
            std::cout << element << " ";
          }
        }


    .. code-tab:: py

        def linear(array: list[int]) -> None:
          for element in array:
            print(element)


Linearithmic Time :math:`O(n log n)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slightly worse than `linear <#linear-time-o-n>`_, typical for efficient sorting mechanisms.


.. admonition:: Common Examples
    :class: hint

    `Merge Sort`_ and `Quick Sort`_


.. tabs::

    .. code-tab:: c++

        int linearithmic(int size) {
          int count { 0 };
          for (int i = 0; i < size; ++i) {
            int j { size };
            while (1 < j) {
              j /= 2;
              count += 1;
            }
          }
          return count;
        }


    .. code-tab:: py

        def linearithmic(size: int) -> int:
          count: int = 0
          for i in range(size):
            j: int = size
            while 1 < j:
              j //= 2
              count += 1
          return count


Quadratic Time :math:`O(n ^ 2)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execution time scales non-linearly, squaring the input size growth.


.. admonition:: Common Examples
    :class: hint

    Nested loops, like `Bubble Sort`_


.. tabs::

    .. code-tab:: c++

        template <int size>
        void quadratic(int (&array)[size]) {
          for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
              std::cout << i << j << std::endl;
            }
          }
        }


    .. code-tab:: py

        def quadratic(array: list[int]) -> None:
          for i in array:
            for j in array:
              print(i, j)


Exponential Time :math:`O(2 ^ n)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Growth doubles with each additional data unit; quickly becomes unrunnable.


.. admonition:: Common Examples
    :class: hint

    Recursive Fibonacci sequence calculations.


.. tabs::

    .. code-tab:: c++

        int fibonacci(int n) {
          if (n < 2) return n;
          return fibonacci(n - 1) + fibonacci(n - 2);
        }


    .. code-tab:: py

        def fibonacci(n: int) -> int:
          if n < 2: return n
          return fibonacci(n - 1) + fibonacci(n - 2)


Factorial Time :math:`O(n!)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Grows incredibly fast; completely unusable for inputs larger than :math:`n ≈ 10`.


.. admonition:: Common Examples
    :class: hint

    Generating all permutations of a string, or solving the Traveling Salesperson Problem.


.. tabs::

    .. code-tab:: c++

        std::vector<std::vector<int>> permutations(std::vector<int> &array) {
          if (array.size() <= 1) return { array };
          std::vector<std::vector<int>> allPermutations;
          for (int i = 0; i < array.size(); ++i) {
            int current { array[i] };
            std::vector<int> remaining;
            remaining.insert(remaining.end(), array.begin(), array.begin() + i);
            remaining.insert(remaining.end(), array.begin() + i + 1, array.end());
            std::vector<std::vector<int>> subpermutations { permutations(remaining) };
            for (int i = 0; i < subpermutations.size(); ++i) {
              std::vector<int> permutation { current };
              permutation.insert(permutation.end(), subpermutations[i].begin(), subpermutations[i].end());
              allPermutations.push_back(permutation);
            }
          }
          return allPermutations;
        }


    .. code-tab:: py

        def permutations(array: list[int]) -> list[list[int]]:
          if len(array) <= 1: return [array]
          all_permutations: list[list[int]] = list()
          for i in range(len(array)):
            current: int = array[i]
            remaining: list[int] = array[:i] + array[i + 1:]
            for permutation in permutations(remaining):
              all_permutations.append([current] + permutation)
          return all_permutations


.. figure:: https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg
    :align: center
    :width: 80%

    *Source*: `Medium <https://medium.com/data-science/understanding-time-complexity-with-python-examples-2bda6e8158a7>`_


How to Calculate Time Complexity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To determine the time complexity of a block of code, follow these three practical rules:

1. Count the loops.
    - A single loop running from :math:`0` to :math:`n` takes :math:`O(n)` time.
    - Two nested loops running up to :math:`n` take :math:`n * n = O(n ^ 2)` time.

2. Drop constant terms.
    Big O isolates the overall growth trend. If an algorithm takes :math:`2n + 5` operations, drop the multiplier :math:`2` and the constant :math:`5`. The time complexity is simply :math:`O(n)`.

3. Keep only the dominating term.
    If a code snippet has one portion taking :math:`O(n ^ 2)` and another taking :math:`O(n)`, the total time formula is :math:`n ^ 2 + n`. As :math:`n` approaches infinity, the :math:`n` term becomes insignificant next to :math:`n ^ 2`. Keep only the largest term: :math:`O(n ^ 2)`.


.. _Binary Search: ./algorithms/binary_search
.. _Bubble Sort: ./algorithms/bubble_sort
.. _Merge Sort: ./algorithms/merge_sort
.. _Quick Sort: ./algorithms/quick_sort