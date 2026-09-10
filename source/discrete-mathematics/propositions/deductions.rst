:description: Deductions in Discrete Mathematics use rules of inference to derive a valid conclusion from a set of given premises.


Deductions
==========

In propositional logics, sometimes we deduct one logical expression from another; we call them **deductions**. Deductions form the backbone of logical reasoning. Deductions are used to derive conclusions from premises. They follow rules that guarantee the truth of the conclusion if the premises are ``true``. This concept is important in mathematical proofs in computer algorithms, and reasoning systems.

A **deduction** is a logical process where, starting from a set of premises (assumptions), we find a conclusion that logically follows. For example, if we know that,

- If Edith eats her vegetables, she gets a cookie.

- Edith ate her vegetables.

Here, we can deduce that *"Edith gets a cookie"*. This simple example shows a rule called `modus ponens <#modus-ponens>`_, one of the most common deduction rules.


This notation means: if :math:`P` is ``true``, and we also know that :math:`P → Q`, then :math:`Q` must be ``true``.


Modus Ponens
++++++++++++

**Modus ponens** (Latin for "method of affirming") is a fundamental rule of inference which states that if a conditional statement (:math:`P → Q`) and its antecedent (:math:`P`) are both ``true``, then its consequent (:math:`Q`) must also be ``true``.

In propositional logic, the rule is expressed as:


.. math::

    \frac{P → Q, P}{∴ Q}


.. admonition:: Example
    :class: hint

    - **Premise 1**: *"If it rains, the grass will be wet."*

    - **Premise 2**: *"It is raining."*

    - **Conclusion**: *"The grass wil be wet."*

    To prove that modus ponens is a valid rule, we can use a truth table. Let us construct one for :math:`P → Q`:

    +-----------+-----------+---------------+
    | :math:`P` | :math:`Q` | :math:`P → Q` |
    +===========+===========+===============+
    | ``true``  | ``true``  | ``true``      |
    +-----------+-----------+---------------+
    | ``true``  | ``false`` | ``false``     |
    +-----------+-----------+---------------+
    | ``false`` | ``true``  | ``true``      |
    +-----------+-----------+---------------+
    | ``false`` | ``false`` | ``true``      |
    +-----------+-----------+---------------+

    From the table, we can see that whenever :math:`P` is ``true`` and :math:`P → Q` is ``true``, :math:`Q` must also be ``true``. This confirms that modus ponens is a valid form of deduction.


-----

Source
  `Deductions in Discrete Mathematics`_


.. _Deductions in Discrete Mathematics: https://www.tutorialspoint.com/discrete_mathematics/discrete_mathematics_deductions.htm