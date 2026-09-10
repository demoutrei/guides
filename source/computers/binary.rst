:description: Binary is the base-2 numbering system consisting solely of 0s and 1s.


Binary
======

**Binary** is the base-2 numbering system consisting solely of ``0`` s and ``1`` s.


Decimal and Binary Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Binary to Decimal
~~~~~~~~~~~~~~~~~

Reverse the order of the binary code and multiply each binary number with its corresponding power of ``2``, and add the products.

To convert binary ``1101`` to decimal:

.. math::

    1 * (2^0) = 1

    0 * (2^1) = 0

    1 * (2^2) = 4
    
    1 * (2^3) = 8

Binary ``1101`` in decimal: :math:`8 + 4 + 0 + 1 = 13`


Octal to Decimal
~~~~~~~~~~~~~~~~


Method A
--------

Starting from the right, multiply the digits with the corresponding powers of ``8`` and add the results.

To convert octal number ``15`` to decimal:

.. math::

    1|5 → 1 * (8^1)|5 * (8^0)

    8|5 → 8 + 5
    
    13

Octal number ``15`` in decimal: ``13``


Method B
--------

Write the three-digit binary representation of each octal digit side-by-side.

.. math::

    0 = 000

    1 = 001
    
    2 = 010

    3 = 011
    
    4 = 100
    
    5 = 101
    
    6 = 110
    
    7 = 111

To convert octal number ``15`` to binary:

.. math::

    15 → 1|5

    1|5 → 001|101

    001101

Octal number ``15`` in binary: ``001101``

`Convert binary to decimal <#binary-to-decimal>`_.

Binary ``001101`` in decimal: ``13``


Hexadecimal to Decimal
~~~~~~~~~~~~~~~~~~~~~~


Method A
--------

Convert each digit to its corresponding decimal value. Multiply each digits by powers of ``16``, starting from the rightmost, and sum the products.

.. math::

    0 = 0
    
    1 = 1

    2 = 2

    3 = 3

    4 = 4

    5 = 5
    
    6 = 6

    7 = 7

    8 = 8

    9 = 9

    10 = A

    11 = B

    12 = C

    13 = D

    14 = E

    15 = F

To convert hexadecimal ``0xD`` to decimal:

.. math::

    |D → |13
    |13 → |13 * (16 ^ 0)
    13

Hexadecimal ``0xD`` in decimal: ``13``


Method B
--------

Convert each digit to its corresponding binary value.

.. math::

    0 = 0000

    1 = 0001

    2 = 0010

    3 = 0011

    4 = 0100

    5 = 0101

    6 = 0110

    7 = 0111

    8 = 1000

    9 = 1001

    A = 1010

    B = 1011

    C = 1100

    D = 1101

    E = 1110

    F = 1111

Convert hexadecimal ``0xD`` to binary:

.. math::

    D → 1101

Hexadecimal ``0xD`` in binary: ``1101``

`Convert binary to decimal <#binary-to-decimal>`_.

Binary ``1101`` in decimal: ``13``


Decimal to Binary
~~~~~~~~~~~~~~~~~

Return the modulo of the decimal until quotient becomes ``0``, and reverse the order of remainders. To convert decimal ``13`` to binary:

.. math::

    13 / 2 = 6 r.1
    
    6 / 2 = 3 r.0
    
    3 / 2 = 1 r.1
    
    1 / 2 = 0 . 1

Decimal ``13`` in binary: ``1101``.


Decimal to Octal
~~~~~~~~~~~~~~~~

First, convert `decimal to binary <#decimal-to-binary>`_.

Starting from the right, group the binary digits into 3. Per group, each digit is represented as 4-2-1---add these up and concatenate the sum of every group. To convert binary ``1101`` to octal:

.. math::

    1101 → 1|101

    1|(4 + 1) → 1|5

    15

Binary ``1101`` in octal: ``15``


Decimal to Hexadecimal
~~~~~~~~~~~~~~~~~~~~~~

First, convert `decimal to binary <#decimal-to-octal>`_.

Group the binary digits into sets of four, starting from the right, and then convert each group into its corresponding hexadecimal digit:

.. math::

    0 = 0

    1 = 1

    2 = 2

    3 = 3

    4 = 4

    5 = 5

    6 = 6

    7 = 7

    8 = 8

    9 = 9

    10 = A

    11 = B
    
    12 = C

    13 = D

    14 = E

    15 = F

To convert binary ``1101`` to hexadecimal:

.. math::

    1101 → |1101
    
    |(8 + 4 + 0 + 1) → |13

    13 → D

Binary ``1101`` in hexadecimal: ``#D`` or ``0xD``


Binary Operations
^^^^^^^^^^^^^^^^^


.. grid:: 1 2 2 2
    :gutter: 3


    .. grid-item-card:: Binary Addition

        +-----------+------------+---------+
        |           | Carry Over | Results |
        +===========+============+=========+
        | 0 + 0     | 0          | 0       |
        +-----------+------------+---------+
        | 0 + 1     | 0          | 1       |
        +-----------+------------+---------+
        | 1 + 0     | 0          | 1       |
        +-----------+------------+---------+
        | 1 + 1     | 1          | 0       |
        +-----------+------------+---------+
        | 1 + 1 + 1 | 1          | 1       |
        +-----------+------------+---------+


    .. grid-item-card:: Binary Subtraction

        +-------+--------+
        |       | Result |
        +=======+========+
        | 1 - 0 | 1      |
        +-------+--------+
        | 1 - 1 | 0      |
        +-------+--------+
        | 0 - 0 | 0      |
        +-------+--------+
        | 0 - 1 | 1      |
        +-------+--------+


    .. grid-item-card:: Binary Multiplication

        +-------+--------+
        |       | Result |
        +=======+========+
        | 0 * 0 | 0      |
        +-------+--------+
        | 0 * 1 | 0      |
        +-------+--------+
        | 1 * 0 | 0      |
        +-------+--------+
        | 1 * 1 | 1      |
        +-------+--------+


    .. grid-item-card:: Binary Division

        +-------+--------+
        |       | Result |
        +=======+========+
        | 0 / 1 | 0      |
        +-------+--------+
        | 1 / 1 | 1      |
        +-------+--------+