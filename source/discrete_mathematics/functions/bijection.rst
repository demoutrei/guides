:description: A bijective function is a function that is both injective (one-to-one) and surjective (onto). It pairs every element in the domain with a unique element in the codomain, leaving no elements unmatched in either set, creating a direct one-to-one correspondence.


Bijection
=========

A **bijective function** is a function that is both injective (one-to-one) and surjective (onto). It pairs every element in the domain with a unique element in the codomain, leaving no elements unmatched in either set, creating a direct one-to-one correspondence.


.. admonition:: Key Characteristics
    :class: tip

    Invertibility
      A function has an inverse function (:math:`f^{-1}`) if and only if it is a bijection.

    Cardinality Match
      If a bijection exists between two finite sets, both sets have the exact same number of elements. This is also used to define equal sizes for infinite sets.

    Composition
      The composition of two bijective functions is always another bijective function.


.. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20231019170642/Bijective-Function-2.png
    :align: center
    :width: 50%

    *Source*: `GeeksforGeeks <https://www.geeksforgeeks.org/maths/bijective-function/>`_


How to Prove
^^^^^^^^^^^^

To prove a function :math:`f: A → B` is a bijection, you must prove it has two properties: it is injective, and subjective.

1. Prove `Injectivity <./injection>`_.

2. Prove `Surjectivity <./surjection>`_.