:description: Predicate Logic deals with predicates, which are propositions containing variables.


Predicate Logic
===============

**Predicate logic** deals with predicates, which are propositions containing variables.

A **predicate** is an expression of one or more variables defined on some specific domain. A predicate with variables can be made a proposition by either assigning a value to the variable or by quantifying the variable.


.. admonition:: Example
    :class: hint

    - Let :math:`E(x, y)` denote ":math:`x = y`"

    - Let :math:`X(a, b, c)` denote ":math:`a + b + c = 0`"

    - Let :math:`M(x, y)` denote ":math:`x is married to y`"


Well Formed Formula
+++++++++++++++++++

**Well Formed Formula (WFF)** is a predicate holding any of the following:

- All propositional constants and propositional variables are WFFs.

- If :math:`x` is a variable and :math:`Y` is a WFF, :math:`∀xY` and :math:`∃xY` are also WFFs.

- Truth value and false values are WFFs.

- Each atomic formula is a WFF.

- All connectives connecting WFFs are WFFs.


Quantifiers
+++++++++++

The variable of predicates is quantified by **quantifiers**. There are two types of quantifier in predicate logic: `Universal Quantifier <#universal-quantifier>`_ and `Existential Quantifier <#existential-quantifier>`_.


Universal Quantifier
^^^^^^^^^^^^^^^^^^^^

**Universal quantifier** states that the statements within its scope are ``true`` for every value of the specific variable. It is denoted by the symbol :math:`∀`.

:math:`∀xP(x)` is read as "for every value of :math:`x`, :math:`P(x)` is true."


.. admonition:: Example
    :class: hint

    "Man is mortal" can be transform into the propositional form :math:`∀xP(x)` where :math:`P(x)` is the predicate which denotes :math:`x` is mortal and the universe of discourse is all men.


Existential Quantifier
^^^^^^^^^^^^^^^^^^^^^^

**Existential quantifier** states that the statements within its scope are ``true`` for some values of the specific variable. It is denoted by the symbol :math:`∃`.

:math:`∃xP(x)` is read as "for some values of :math:`x`, :math:`P(x)` is true."


.. admonition:: Example
    :class: hint

    "Some people are dishonest" can be transformed into the propositional form :math:`∃xP(x)` where :math:`P(x)` is the predicate which denotes :math:`x` is dishonest and the universe of discourse is some people.


Nested Quantifiers
^^^^^^^^^^^^^^^^^^

If we use a quantifier that appears within the scope of another quantifier, it is called **nested quantifier**.


.. admonition:: Example
    :class: hint

    - :math:`∀x∃yP(x, y)` where :math:`P(x, y)` denotes :math:`x + y = 0`

    - :math:`∀a∀b∀cP(a, b, c)` where :math:`P(a, b)` denotes :math:`a + (b + c) = (a + b) + c`


.. note::

    :math:`-∀a∃bP(x, y) ≠ ∃a∀bP(x, y)`


-----

.. admonition:: Sources
    :class: seealso
  
    `Discrete Mathematics - Predicate Logic`_


.. _Discrete Mathematics - Predicate Logic: https://www.tutorialspoint.com/discrete_mathematics/discrete_mathematics_predicate_logic.htm