Integers and Divisibility
=========================

This section includes some basic topics in number theory such as integers, divisibility, greatest common divisor, and integers.


The Division Algorithm
++++++++++++++++++++++

Let :math:`a` and :math:`b` (:math:`≥ 1`) be integers. Then there exist unique integers :math:`q` and :math:`r` such that

.. math::

    a = bq + r

Where :math:`0 ≤ r < b`.

The integer :math:`q` is called the **quotient** of :math:`a` and :math:`b` on dividing :math:`a` by :math:`b`; the integer :math:`r` is called the **remainder** of :math:`a` and :math:`b` on dividing :math:`a` by :math:`b`.

Greatest Common Divisor
+++++++++++++++++++++++

A nonzero integer :math:`d` is said to be a common divisor of integers :math:`a` and :math:`b` if :math:`d | a` and :math:`d | b`.

The largest nonzero integer :math:`d` is said to be the greatest common divisor of integers :math:`a` and :math:`b` denoted by :math:`\text{gcd} (a, b)`, if :math:`d|a` and :math:`d|b`.

.. admonition:: Example
    :class: hint

    :math:`1`, :math:`3`, :math:`5`, and :math:`15` divides both :math:`30` and :math:`45`. The greatest common divisor of :math:`30` and :math:`45` is :math:`\text{gcd} (30, 45) = 15`.

.. admonition:: Example
    :class: hint

    :math:`1`, :math:`2`, :math:`3`, :math:`6`, :math:`9`, and :math:`18` divides both :math:`54` and :math:`90`. The greatest common divisor of :math:`54` and :math:`90` is :math:`\text{gcd} (54, 90) = 18`.

.. admonition:: Example
    :class: hint

    :math:`15` and :math:`22` has no common divisor other than :math:`1`, so that :math:`\text{gcd} (15, 22) = 1`.

Eucledian Algorithm for Finding the GCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Consider two positive integers :math:`a` and :math:`b`. By the division algorithm, there exist integers :math:`q_1` and :math:`r_1` such that

.. math::

    a = q_1b + r_1, 0 ≤ r_1 < b.

Now consider :math:`b` and :math:`r_1`. Suppose :math:`r_1 \neq 0`. Then by the division algorithm, there exist integers :math:`q_2` and :math:`r_2` such that

.. math::

    b = q_2 r_1 + r_2, 0 \le r_2 < r_1.

Next consider :math:`r_1` and :math:`r_2`. Suppose :math:`r_2 \neq 0`. Then by the division algorithm, there exist integers :math:`q_3` and :math:`r_3` such that

.. math::

    r_1 = q_3 r_2 + r_3, 0 \le r_3 < r_2.

We continue this process. Then we have

.. math::

    \begin{aligned}
    &\phantom{\text{If } r_1 \neq 0,} & a &= q_1b + r_1, & 0 &\le r_1 < b \\
    &\text{If } r_1 \neq 0, & b &= q_2r_1 + r_2, & 0 &\le r_2 < r_1 \\
    &\text{If } r_2 \neq 0, & r_1 &= q_3r_2 + r_3, & 0 &\le r_3 < r_2 \\
    &\text{If } r_3 \neq 0, & r_2 &= q_4r_3 + r_4, & 0 &\le r_4 < r_3 \\
    & & &\vdots & & 
    \end{aligned}


The remainder :math:`r_1, r_2, r_3, ...` form the following decreasing sequence of nonnegative integers:

.. math::

    b > r_1 > r_2 > r_3 > ... \ge 0

Because :math:`b` is a fixed positive integer, we must encounter the remainder :math:`0` after a finite number of steps. Therefore, the process terminates after some steps.

.. admonition:: Example
    :class: hint

    Consider the integers :math:`448` and :math:`196`.

    By repeated application of the division algorithm, we get

    :math:`448 = 2 \times 196 + 56`

    :math:`196 = 3 \times 56 + 28`

    :math:`56 = 2 \times 28 + 0`

    The gcd is the last nonzero remainder. Thus, the :math:`\text{gcd} (196, 448) = 28`.

Least Common Multiple
+++++++++++++++++++++

The least common multiple of :math:`a` and :math:`b`, denoted by :math:`\text{lcm} (a, b)`, is the smallest positive integer that is both divisible by :math:`a` and :math:`b`.

.. admonition:: Example
    :class: hint

    The least common multiple of :math:`18` and :math:`20` is :math:`\text{lcm} (18, 20) = 180`.

    **Solution**.

    :math:`18 = 2 \times 3^2` and :math:`20 = 2^2 \times 5`

    The least common multiple of :math:`18` and :math:`20` is :math:`2^2 \times 3^2 \times 5 = 180`.