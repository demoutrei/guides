Identity
========

An **identity function** is a special mapping on a set that returns every element exactly as it was given. Written as :math:`i_A` or :math:`id_A:A→A`, it is formally defined by the rule :math:`id_A(x) = x` for every :math:`x \in A`.


.. admonition:: Key Characteristics
    :class: tip

    Equivalence
      Every input value matches its output value with no change.

    Bijectivity
      It is always both `injective <./injection>`_ and `surjective <./surjective>`_, forming a perfect one-to-one correspondence with itself.

    Self-Inverse
      The inverse of an identity function is itself (:math:`id_A^{-1} = id_A`).

    Composition Neutrality
      Composing any function :math:`f` with an identity function leaves :math:`f` unchanged (:math:`f \circ \text{id} = \text{id} \circ f = f`).


.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20250201153437076377/Identity-Function.webp
    :align: center
    :width: 50%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/maths/identity-function/>`_


.. seealso::

    `How to Prove Injectivity <./injection#how-to-prove>`_
    
    `How to Prove Surjectivity <./surjection#how-to-prove>`_