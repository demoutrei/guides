:description: An injective function is a one-to-one function where every distinct input in the domain maps to a unique output in the codomain. No two different elemetns share the same image, meaning no target value is hit more than once.


Injection
=========

An **injective function** is a one-to-one function where every distinct input in the domain maps to a unique output in the codomain. No two different elements share the same image, meaning no target value is hit more than once.


.. admonition:: Key Characteristics
    :class: tip

    At Most One Preimage
      Every element in the codomain has at most one corresponding element (preimage) mapped to it. Some codomain elements may have zero preimages.

    No Collisions
      Two distinct inputs are never allowed to result in a shared output value.

    Cardinality Rule
      If a function maps from a finite set :math:`A` to finite set :math:`B` injectively, the size of the domain must be less than or equal to the size of the codomain (:math:`|A| ≤ |B|`).

    Left-Invertible
      An injection with a non-empty domain has a left inverse, meaning you can "undo" the mapping for elements in the range.


.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20231016183536/Injective-Function-1.png
    :align: center
    :width: 50%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/maths/injective-functions/>`_


How to Prove
^^^^^^^^^^^^

To prove that a function :math:`f: A → B` is an injection (one-to-one), show that equal outputs imply equal inputs. Assume :math:`f(x_1) = f(x_2)` for arbitrary elements :math:`x_1, x_2 \in A`, and use algebra to prove :math:`x_1 = x_2`.

1. Let :math:`x_1, x_2 \in A` and suppose :math:`f(x_1) = f(x_2)`.

2. Use the formula for :math:`f(x)` to expand both sides.

3. Use algebra to cancel terms and solve until you reach :math:`x_1 = x_2`.


.. admonition:: Example
    :collapsible:
    :class: hint

    Prove that :math:`f: \mathbb{R} → \mathbb{R}` defined by :math:`f(x) = 3x - 2` is injective.

    1. Let :math:`x_1, x_2 \in \mathbb{R}` and assume :math:`f(x_1) = f(x_2)`.

    2. By the definition of :math:`f`, this means:

    .. math::

        3x_1 - 2 = 3x_2 - 2

    3. Add :math:`2` to both sides:

    .. math::

        3x_1 = 3x_2

    4. Divide by :math:`3`:

    .. math::

        x_1 = x_2

    5. Thus, :math:`f` is injective.