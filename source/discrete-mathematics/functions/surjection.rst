:description: A surjective function (also called an "onto" function) is a function where every element in the codomain is mapped to by at least one element from the domain. No element in the target set is left out.


Surjection
==========

A **surjective function** (also called an **onto function**) is a function where every element in the codomain is mapped to by at least one element from the domain. No element in the target set is left out.


.. admonition:: Key Characteristics
    :class: tip

    Many-to-One Allowed
      Multiple domain elements can point to the same codomain element.

    Composition Rule
      The composite of two surjective functions is always surjective.

    Cardinality Constraint
      If :math:`f: A → B` is surjective, the size (cardinality) of the domain :math:`A` must be greater than or equal to the size of the codomain :math:`B` (:math:`|A| ≥ |B|`).

    Right Invertible
      Every surjection has a right inverse :math:`g: B → A` such that :math:`f(g(b)) = b`.


.. figure:: https://media.geeksforgeeks.org/wp-content/cdn-uploads/8-3.png
    :align: center
    :width: 50%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/maths/functions/>`_


How to Prove
^^^^^^^^^^^^

1. Let :math:`y` be arbitrary.
    Start by picking an arbitrary element :math:`x ∈ Y` from the codomain.

2. Set up the equation.
    Write out :math:`f(x) = y`.

3. Solve for :math:`x`.
    Use algebra to solve for :math:`x` in terms of :math:`y`.

4. Check the domain.
    Confirm that the resulting :math:`x`-value belongs to the domain :math:`X`.

5. Verify the mapping.
    Substitute your expression for :math:`x` back into :math:`f(x)` to show that :math:`f(x) = y`.


.. admonition:: Example
    :collapsible:
    :class: hint

    Prove that :math:`f : ℝ → ℝ` defined by :math:`f(x) = 3x - 5` is surjective.

    1. Let :math:`y` be an arbitrary real number in the codomain (:math:`\mathbb{Y} = \mathbb{R}`).

    2. Set :math:`f(x) = y`, which gives :math:`3x - 5 = y`.

    3. Solve for :math:`x`.

    .. math::

        3x = y + 5

        x = \frac{y + 5}{3}

    4. Since :math:`y \in \mathbb{R}`, :math:`\frac{y + 5}{3}` is also a real number, meaning :math:`x` is in the domain :math:`\mathbb{R}`.

    5. Verify.

    .. math::

        f\left(\frac{y + 5}{3}\right) = 3\left(\frac{y + 5}{3}\right) - 5
        
        = (y + 5) - 5

        = y

    Since for every :math:`y \in \mathbb{R}` there exists an :math:`x = \frac{y + 5}{3}` such that :math:`f(x) = y`, the function :math:`f` is surjective.