:description: Propositional logic is concerned with statements to which the truth values, true and false, can be assigned. The purpose is to analyze these statements either individually or in a composite manner.


Propositional Logic
===================

**Propositional logic** is concerned with statements to which the truth values, ``true`` and ``false``, can be assigned. The purpose is to analyze these statements either individually or in a composite manner.


Definition
++++++++++

A **proposition** is a collection of declarative statements that has either a truth value ``true`` or ``false``. A propositional consists of propositional variables and `connectives <#connectives>`_. We denote the propositional variables by capital letters (:math:`A`, :math:`B`, etc). The connectives must connect the propositional variables.


.. admonition:: Example
    :class: hint

    - "Man is Mortal": it returns truth value ``true``

    - "12 + 9 = 32": it returns truth value ``false``


The following is not a proposition:

- ":math:`A` is less than 2": It is because unless we give a specific value of :math:`A`, we cannot say whether the statement is ``true`` or ``false``.


Connectives
+++++++++++

**Logical connectives** are symbols or words used to combine simple propositions into complex compound statements.

In propositional logic, generally we use five connectives, which are:


Disjunction (:math:`∨`)
^^^^^^^^^^^^^^^^^^^^^^^

The logical-OR operation of two propositions :math:`A` and :math:`B` (written as :math:`A ∨ B`) is ``true`` if at least any of the propositional variable :math:`A` or :math:`B` is ``true``.

The truth table is as follows:

+-----------+-----------+---------------+
| :math:`A` | :math:`B` | :math:`A ∨ B` |
+===========+===========+===============+
| ``true``  | ``true``  | ``true``      |
+-----------+-----------+---------------+
| ``true``  | ``false`` | ``true``      |
+-----------+-----------+---------------+
| ``false`` | ``true``  | ``true``      |
+-----------+-----------+---------------+
| ``false`` | ``false`` | ``false``     |
+-----------+-----------+---------------+


Conjunction (:math:`∧`)
^^^^^^^^^^^^^^^^^^^^^^^

The logical-AND operation of two propositions :math:`A` and :math:`B` (written as :math:`A ∧ B`) is ``true`` if both the propositional variable :math:`A` and :math:`B` is ``true``.

The truth table is as follows:

+-----------+-----------+---------------+
| :math:`A` | :math:`B` | :math:`A ∧ B` |
+===========+===========+===============+
| ``true``  | ``true``  | ``true``      |
+-----------+-----------+---------------+
| ``true``  | ``false`` | ``false``     |
+-----------+-----------+---------------+
| ``false`` | ``true``  | ``false``     |
+-----------+-----------+---------------+
| ``false`` | ``false`` | ``false``     |
+-----------+-----------+---------------+


Negation (:math:`¬`)
^^^^^^^^^^^^^^^^^^^^

The negation of a proposition :math:`A` (written as :math:`¬A`) is ``false`` when :math:`A` is ``true``, and is ``true`` when :math:`A` is ``false``.

The truth table is as follows:

+-----------+------------+
| :math:`A` | :math:`¬A` |
+===========+============+
| ``true``  | ``false``  |
+-----------+------------+
| ``false`` | ``true``   |
+-----------+------------+


Implication (:math:`→`)
^^^^^^^^^^^^^^^^^^^^^^^

An implication :math:`A → B` is the proposition if :math:`A`, then :math:`B`. It is ``false`` if :math:`A` is ``true`` and :math:`B` is ``false``. The rest cases are ``true``.

The truth table is as follows:

+-----------+-----------+---------------+
| :math:`A` | :math:`B` | :math:`A → B` |
+===========+===========+===============+
| ``true``  | ``true``  | ``true``      |
+-----------+-----------+---------------+
| ``true``  | ``false`` | ``false``     |
+-----------+-----------+---------------+
| ``false`` | ``true``  | ``true``      |
+-----------+-----------+---------------+
| ``false`` | ``false`` | ``true``      |
+-----------+-----------+---------------+


Biconditional (:math:`⇔`)
^^^^^^^^^^^^^^^^^^^^^^^^^^

:math:`A ⇔ B` is biconditional logical connective which is ``true`` when ``p`` and ``q`` are same, i.e. both are ``false`` or both are ``true``.

The truth table is as follows:

+-----------+-----------+---------------+
| :math:`A` | :math:`B` | :math:`A ⇔ B` |
+===========+===========+===============+
| ``true``  | ``true``  | ``true``      |
+-----------+-----------+---------------+
| ``true``  | ``false`` | ``false``     |
+-----------+-----------+---------------+
| ``false`` | ``true``  | ``false``     |
+-----------+-----------+---------------+
| ``false`` | ``false`` | ``true``      |
+-----------+-----------+---------------+


Tautology
+++++++++

A **tautology** is a formula which is always ``true`` for every value of its propositional variables.


.. admonition:: Example
    :class: hint

    Prove :math:`[(A → B) ∧ A] → B` is a tautology:

    +-----------+-----------+---------------+---------------------+---------------------------+
    | :math:`A` | :math:`B` | :math:`A → B` | :math:`(A → B) ∧ A` | :math:`[(A → B) ∧ A] → B` |
    +===========+===========+===============+=====================+===========================+
    | ``true``  | ``true``  | ``true``      | ``true``            | ``true``                  |
    +-----------+-----------+---------------+---------------------+---------------------------+
    | ``true``  | ``false`` | ``false``     | ``false``           | ``true``                  |
    +-----------+-----------+---------------+---------------------+---------------------------+
    | ``false`` | ``true``  | ``true``      | ``false``           | ``true``                  |
    +-----------+-----------+---------------+---------------------+---------------------------+
    | ``false`` | ``false`` | ``true``      | ``false``           | ``true``                  |
    +-----------+-----------+---------------+---------------------+---------------------------+

    As we can see, every value of :math:`[(A → B) ∧ A] → B` is ``true``. Therefore, it is a tautology.


Contradictions
++++++++++++++

A **contradiction** is a formula which is always ``false`` for every value of its propositional variables.


.. admonition:: Example
    :class: hint

    Prove :math:`(A ∨ B) ∧ [(¬A) ∧ (¬B)]` is a contradiction:

    +-----------+-----------+---------------+------------+------------+------------------------+------------------------------------+
    | :math:`A` | :math:`B` | :math:`A ∨ B` | :math:`¬A` | :math:`¬B` | :math:`(¬ A) ∧ ( ¬ B)` | :math:`(A ∨ B) ∧ [( ¬ A) ∧ (¬ B)]` |
    +===========+===========+===============+============+============+========================+====================================+
    | ``true``  | ``true``  | ``true``      | ``false``  | ``false``  | ``false``              | ``false``                          |
    +-----------+-----------+---------------+------------+------------+------------------------+------------------------------------+
    | ``true``  | ``false`` | ``true``      | ``false``  | ``true``   | ``false``              | ``false``                          |
    +-----------+-----------+---------------+------------+------------+------------------------+------------------------------------+
    | ``false`` | ``true``  | ``true``      | ``true``   | ``false``  | ``false``              | ``false``                          |
    +-----------+-----------+---------------+------------+------------+------------------------+------------------------------------+
    | ``false`` | ``false`` | ``false``     | ``true``   | ``true``   | ``true``               | ``false``                          |
    +-----------+-----------+---------------+------------+------------+------------------------+------------------------------------+

    As we can see, every value of :math:`(A ∨ B) ∧ [( ¬ A) ∧ (¬ B)]` is ``false``. Therefore, it is a contradiction.


Contingency
+++++++++++

A **contingency** is a formula which has both some ``true`` and some ``false`` values for every value of its propositional variables.


.. admonition:: Example
    :class: hint

    Prove :math:`(A ∨ B) ∧ (¬A)` is a contingency.

    +-----------+-----------+---------------+------------+-------------------------+
    | :math:`A` | :math:`B` | :math:`A ∨ B` | :math:`¬A` | :math:`(A ∨ B) ∧ (¬ A)` |
    +===========+===========+===============+============+=========================+
    | ``true``  | ``true``  | ``true``      | ``false``  | ``false``               |
    +-----------+-----------+---------------+------------+-------------------------+
    | ``true``  | ``false`` | ``true``      | ``false``  | ``false``               |
    +-----------+-----------+---------------+------------+-------------------------+
    | ``false`` | ``true``  | ``true``      | ``true``   | ``true``                |
    +-----------+-----------+---------------+------------+-------------------------+
    | ``false`` | ``false`` | ``false``     | ``true``   | ``false``               |
    +-----------+-----------+---------------+------------+-------------------------+

    As we can see, every value of :math:`(A ∨ B) ∧ (¬A)` has both ``true`` and ``false``. Therefore, it is a contingency.


Propositional Equivalences
++++++++++++++++++++++++++

Two statements :math:`A` and :math:`B` are logically equivalent if any of the following two conditions hold:

- the truth tables of each statement have the same truth values; or,

- the biconditional statement :math:`A ⇔ B` is a `tautology`_.


.. admonition:: Example
    :class: hint

    Prove :math:`¬(A ∨ B)` and :math:`[(¬A) ∧ (¬B)]` are equivalent.


    **Method 1: Matching truth table**

    +-----------+-----------+---------------+-------------------+------------+-------------+-----------------------+
    | :math:`A` | :math:`B` | :math:`A ∨ B` | :math:`¬ (A ∨ B)` | :math:`¬A` | :math:`¬ B` | :math:`[(¬A) ∧ (¬B)]` |
    +===========+===========+===============+===================+============+=============+=======================+
    | ``true``  | ``true``  | ``true``      | ``false``         | ``false``  | ``false``   | ``false``             |
    +-----------+-----------+---------------+-------------------+------------+-------------+-----------------------+
    | ``true``  | ``false`` | ``true``      | ``false``         | ``false``  | ``true``    | ``false``             |
    +-----------+-----------+---------------+-------------------+------------+-------------+-----------------------+
    | ``false`` | ``true``  | ``true``      | ``false``         | ``true``   | ``false``   | ``false``             |
    +-----------+-----------+---------------+-------------------+------------+-------------+-----------------------+
    | ``false`` | ``false`` | ``false``     | ``true``          | ``true``   | ``true``    | ``true``              |
    +-----------+-----------+---------------+-------------------+------------+-------------+-----------------------+

    Here, we can see the truth values of :math:`¬(A ∨ B)` and :math:`[(¬A) ∧ (¬B)]` are the same, hence the statements are equivalent.


    **Method 2: Biconditionality**

    +-----------+-----------+--------------------+-------------------------+-----------------------------------+
    | :math:`A` | :math:`B` | :math:`¬ (A ∨ B )` | :math:`[(¬ A) ∧ (¬ B)]` | :math:`¬(A ∨ B) ⇔ [(¬A) ∧ (¬B)]`  |
    +===========+===========+====================+=========================+===================================+
    | ``true``  | ``true``  | ``false``          | ``false``               | ``true``                          |
    +-----------+-----------+--------------------+-------------------------+-----------------------------------+
    | ``true``  | ``false`` | ``false``          | ``false``               | ``true``                          |
    +-----------+-----------+--------------------+-------------------------+-----------------------------------+
    | ``false`` | ``true``  | ``false``          | ``false``               | ``true``                          |
    +-----------+-----------+--------------------+-------------------------+-----------------------------------+
    | ``false`` | ``false`` | ``false``          | ``true``                | ``true``                          |
    +-----------+-----------+--------------------+-------------------------+-----------------------------------+

    As :math:`¬(A ∨ B) ⇔ [(¬A) ∧ (¬B)]` is a `tautology`_, the statements are equivalent.


Inverse, Converse, and Contra-positive
++++++++++++++++++++++++++++++++++++++

`Implication <#implication>`_ is also called a **conditional statement**. It has two parts:

- **Hypothesis**, :math:`P`; and,

- **Conclusion**, :math:`Q`.


.. note::

    As mentioned earlier, it is denoted as :math:`P → Q`.


.. admonition:: Example
    :class: hint

    *"If you do your homework, you will not be punished."*

    Here, *"you do your homework"* is the hypothesis, and *"you will not be punished"* is the conclusion.


.. grid:: 1
    :gutter: 3

    
    .. grid-item-card:: Inverse

        An **inverse** of the conditional statement is the negation of both hypothesis and the conclusion. The inverse of :math:`P → Q` is :math:`¬P → ¬Q`.


        .. admonition:: Example
            :class: hint

            The inverse of...
            

            .. epigraph::

                | "If you do your homework, you will not be punished."

            
            is...


            .. epigraph::

              | "If you do not do your homework, you will be punished."


    .. grid-item-card:: Converse

        The **converse** of the conditional statement is computed by interchanging the hypothesis and the conclusion. The converse of :math:`P → Q` is :math:`Q → P`.


        .. admonition:: Example
            :class: hint

            The converse of...


            .. epigraph::

                | "If you do your homework, you will not be punished." 


            is...


            .. epigraph::

                | "If you will not be punished, you do your homework."


    .. grid-item-card:: Contra-positive

        The **contra-positive** of the conditional is computed by interchanging the hypothesis and the conclusion of the inverse statement. The contra-positive of :math:`P → Q` is :math:`¬Q → ¬P`.


        .. admonition:: Example
            :class: hint

            The contra-positive of...


            .. epigraph::

                | "If you do your homework, you will not be pubished."

            
            is...


            .. epigraph::

                | "If you are punished, you did not do your homework."


De Morgan's Laws
++++++++++++++++

**De Morgan's Laws** are a pair of logical equivalence rules that show how negation interacts with `conjunction <#conjunction>`_ and `disjunction <#disjunction>`_.


.. epigraph::

    | :math:`\neg(P \wedge Q)` is logically equivalent to :math:`\neg P \vee \neg Q`.
    | :math:`\neg(P \vee Q)` is logically equivalent to :math:`\neg P \wedge \neg Q`.


Implications are Disjunctions
+++++++++++++++++++++++++++++

Every implication can be written as a disjunction:


.. epigraph::

    | :math:`P → Q` is logically equivalent to :math:`\neg P \vee Q`.


Double Negation
+++++++++++++++

:math:`\neg \neg P` is logically equivalent to :math:`P`


Negation of an Implication
++++++++++++++++++++++++++

The negation of an implication is a `conjunction <#conjunction>`_:


.. epigraph::

    | :math:`\neg(P \imp Q)` is logically equivalent to :math:`P \wedge \neg Q`.


That is, the only way for an implication to be ``false`` is for the hypothesis to be ``true`` *AND* the conclusion to be ``false``.


.. toctree::
    :maxdepth: 1
    :caption: SubTopics

    deductions
    predicates


-----

Source
  `Discrete Mathematics - Propositional Logic`_

  `discrete.openmathbooks.org <https://discrete.openmathbooks.org/dmoi3/sec_propositional.html>`_


.. _Discrete Mathematics - Propositional Logic: https://www.tutorialspoint.com/discrete_mathematics/discrete_mathematics_propositional_logic.htm
.. _tautology: #tautology