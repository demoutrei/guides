Space Complexity
================

Space complexity is a metric that quantifies the total memory space an algorithm or data structure requires to run to completion as a function of the input size (:math:`n`). It is expressed using Big O notation to define how memory requirements scale rather than measuring exact bytes, which vary by hardware.


Space Complexity vs. Auxiliary Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These terms are often confused but have distinct definitions:


.. epigraph::

    | Space Complexity = Input Space + Auxiliary Space


Input Space
  The memory required to store the original input data.

Auxiliary Space
  The temporary or extra memory allocated by the algorithm to solve the problem (e.g. local variables, dynamically allocated memory, scratchpad arrays).


Components of Space Memory
^^^^^^^^^^^^^^^^^^^^^^^^^^

An algorithm allocates memory across two core components:


Fixed Part (:math:`O(1)`)
  Memory required by the program that remains constant regardless of the input size.

  - Instruction space (the compiled code itself).
  - Simple variables and constants

Variable Part
  Memory required by components that scale as the input data scales.

  - **Dynamic data structures**: arrays, trees, or tables whose sizes match the input load.
  - **Recursion stack space**: each active function call in recursion pushes stack frames containing arguments and local variables onto the call stack.


Common Complexities
^^^^^^^^^^^^^^^^^^^

Ordered by efficiency:


Constant Space :math:`O(1)`
  Memory stays exactly the same regardless of input size.


  .. admonition:: Common Use Case / Triggers
      :class: hint

      In-place mutations, primitive variables.


Logarithmic Space :math:`O(log n)`
  Memory grows slowly, scaling with the height of balanced tree paths.


  .. admonition:: Common Use Case / Triggers
      :class: hint

      Iterative halving, balanced search trees.


Linear Space :math:`O(n)`
  Memory grows at a direct 1:1 ratio with the input size.


  .. admonition:: Common Use Case / Triggers
      :class: hint

      Cloning arrays, recursion stacks, linear data structures.


Linearithmic Space :math:`O(n log n)`
  Memory grows slightly faster than linear.


  .. admonition:: Common Use Case / Triggers
      :class: hint

      Sorting with deep allocation or multi-level tracking.


Quadratic Space :math:`O(n ^ 2)`
  Memory scales by the square of input size.


  .. admonition:: Common Use Case / Triggers
      :class: hint

      2D matrices, dense graphs, nested dynamic tracking.


How to Calculate Space Complexity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To calculate space complexity, you must measure the total amount of memory an algorithm needs to run to completion relative to its input size (:math:`n`). The mathematical formula representing memory consumption is:


.. epigraph::

    | Total Space :math:`S(P) = C + S_P`


Where :math:`C` is the fixed part, and :math:`S_P` is the variable part. In algorithmic analysis, we drop the constants and focus on the highest growth rate using Big O notation.


1. Look for single variables, loops, counters, or flags. If they do not scale with the input size, they take constant space.

2. Look for allocations that scale dynamically with the input size :math:`n`.
    - **Linear** :math:`O(n)`: a new array, list, stack, or queue of size :math:`n`.
    - **Quadratic** :math:`O(n ^ 2)`: a 2D matrix of size :math:`n * 2`.

3. Every time a function calls itself, a new stack frame is added to the system memory to track variables and execution context.
    - Calculate the maximum depth of the recursion tree.
    - If a function recurses :math:`n` times before reaching its base case, the stack memory scales linearly to :math:`O(n)`.

4. Differentiate Space vs. Auxiliary Space
    - **Total space complexity**: includes the input data itself + any extra space used.
    - **Auxiliary space**: includes only the extra or temporary space allocated by the algorithm (excluding the initial input).