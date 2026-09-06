Constant
========

A **constant function** is a specific type of function where every input from the domain maps to the exact same single output in the codomain.


.. admonition:: Key Characteristics
    :class: tip

    Single Output Value
      The range contains only one element :math:`\{c\}` no matter how large the domain is.

    Independent of Input
      The value of the output does not change or depend on the input variable :math:`x`.

    Many-to-One Mapping
      If the domain has more than one element, multiple inputs point to the same single output.

    Not `Injective <./injection>`_
      It fails injectivity unless the domain contains at most one element.

    Polynomial Degree
      When dealing with real numbers, it acts as a polynomial of degree zero.


.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20231010191233/Constant-Function.png
    :align: center
    :width: 50%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/maths/constant-function/>`_


How to Prove
^^^^^^^^^^^^

To prove that a function :math:`f:A→B` is a constant function, you must show that for all elements :math:`x` in the domain :math:`A`, the output :math:`f(x)` equals a single fixed element :math:`x` in the codomain :math:`B`.

1. Assume :math:`A` is the domain. Show there exists some fixed element :math:`c \in B` such that for every :math:`x \in A`, :math:`f(x) = c`.

2. Let :math:`x` be an arbitrary element in :math:`A`.

3. Apply the explicit definition or formula of :math:`f(x)`.

4. Demonstrate through algebra or logic that the result simplifies to a fixed value :math:`c` that does not depend on :math:`x`.

5. State that because :math:`x` was arbitrary, :math:`f(x) = c` for all :math:`x \in A`.


.. admonition:: Example
    :class: hint

    Prove that :math:`f:\mathbb{R} → \mathbb{R}` defined by :math:`f(x) = |x| - |x|` is a constant function.

    1. Simplify the expression.
        For any real number :math:`x`, subtract the floor of :math:`x` from the floor of :math:`x`:

    .. math::

        f(x) = |x| - |x| = 0

    
    Result
      For any input :math:`x`, the output is always :math:`0`. Thus, :math:`c = 0`, proving it is a constant function.