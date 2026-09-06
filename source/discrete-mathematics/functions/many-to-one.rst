Many-to-One
===========

A **many-to-one function** is a function where two or more distinct inputs from the domain map to the same single output in the codomain. It satisfies the core rule of a function---each input has only one output---but breaks uniqueness in reverse, meaning multiple inputs share an image.


.. admonition:: Key Characteristics
    :class: tip

    Lack of Inverse
      Because multiple inputs yield the same output, you cannot reverse the mapping uniquely; thus, a many-to-one function is not invertible.

    Cardinality of Sets
      For finite sets, the size of the domain can be (and often is) greater than or equal to the size of the range/codomain to force overlapping targets.

    Relation to Surjectivity
      A many-to-one function *can* be onto (`surjective <./surjection>`_) if every element in the codomain is hit by at least one domain element, or *into* if some codomain elements remain unmapped.


.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20231213180200/Many-one-Function.png
    :align: center
    :width: 50%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/maths/many-one-functions/>`_


How to Prove
^^^^^^^^^^^^

1. Verify it is a function.
    Show that every input in the domain maps to one and only one output in the codomain.

2. State the negation of one-to-one.
    A function is not one-to-one if there exist elements :math:`x_1, x_2` in the domain such that :math:`x_1 ≠ x_2`, but :math:`f(x_1) = f(x_2)`.

3. Find a specific counterexample.
    Pick two distinct numbers (:math:`x_1` and :math:`x_2`) from your domain.

4. Evaluate the function.
    Plug both numbers into the function rule :math:`f(x)`.

5. Demonstrate equality.
    Show that :math:`f(x_1) = f(x_2)`, proving that multiple inputs share a single output.


.. admonition:: Example
    :class: hint

    Let :math:`f: \mathbb{R} → \mathbb{R}` be defined by :math:`f(x) = x ^ 2`.

    1. Choose two different real numbers in the domain: let :math:`x_1 = 2` and :math:`x_2 = -2`. Note that :math:`x_1 ≠ x_2` (:math:`2 ≠ -2`).

    2. Evaluate the function for both inputs:

    .. math::

        f(2) = (2) ^ 2 = 4

        f(-2) = (-2) ^ 2 = 4

    3. Conclude that :math:`f(2) = f(-2)` while :math:`2 ≠ -2`. Because two distinct inputs produce the same output, :math:`f(x) = x ^ 2` is not one-to-one and is therefore a many-to-one function.