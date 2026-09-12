:description: A matrix is some table of numbers, symbols, or mathematical objects coming from a set. A matrix has a "height" and a "width" corresponding to the number of rows and the number of columns, respectively. We describe a matrix first by its number of rows and then by its number of columns.


Matrix
======

A **matrix** is some table of numbers, symbols, or mathematical objects coming from a set. A matrix has a "height" and a "width" corresponding to the number of rows and the number of columns, respectively. We describe a matrix first by its number of rows and then by its number of columns. A "two by three matrix of integers", shown below, has two rows, three columns, and its *entries* are integers.


.. math::

    \begin{split}
    \begin{bmatrix}
    3 & 5 & 12 \\
    -1 & -7 & 4
    \end{bmatrix}
    \end{split}


For a particular :math:`(i, j)` index, we can say the :math:`(i, j) \text{th}` entry of a matrix is the element of the matrix in the :math:`i \text{th}` row and the :math:`j \text{th}` column. In the previous matrix, :math:`5` is the :math:`(1, 2)` entry; :math:`-7` is the :math:`(2, 1)` entry. Generally, we can have an :math:`m` by :math:`n` matrix with :math:`m` rows and :math:`n` columns. An :math:`m` by :math:`n` matrix can be denoted as :math:`A_{m \times n}`.


We give special names to matrices with certain dimensions:


1. When :math:`m = 1`, we have a **row vector**. Below is a row vector with 7 entries.


.. math::

    \begin{bmatrix}
    4 & 1 & 4 & 2 & 3 & 7 & 8
    \end{bmatrix}


2. When :math:`n = 1`, we have a **column vector**. Below is a column vector with 6 entries.


.. math::

    \begin{split}
    \begin{bmatrix}
    5 \\
    -3 \\
    4 \\
    -11 \\
    22 \\
    6
    \end{bmatrix}
    \end{split}


3. When :math:`m = n`, we have a **square matrix**. We say a square matrix is of *order* :math:`n` for a matrix with dimension :math:`n` by :math:`n`. A square matrix of order :math:`3` is shown below.


.. math::

    \begin{split}
    \begin{bmatrix}
    9 & -1 & 16 \\
    3 & -5 & 12 \\
    11 & 4 & -8
    \end{bmatrix}
    \end{split}


Operations
++++++++++

When matrices have entries coming from a set with supports addition and multiplication, like real numbers, integers, or even more general objects like polynomials, it is possible to combine them when a generalized form of arithmetic.


Scalar Multiplication
^^^^^^^^^^^^^^^^^^^^^

Scalar multiplication is a simple operation which multiplies a single number against each entry of a matrix to produce another matrix of the same dimensions.

Say :math:`A = (a_{i, j})` is an :math:`m` by :math:`n` integer matrix. Given some other integer :math:`c`, :math:`cA` is another :math:`m` by :math:`n` matrix where:


.. math::

    \begin{split}cA = (c \cdot a_{i,j})  &= c\begin{bmatrix}
    a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
    a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
    \vdots & \vdots   & \ddots & \vdots \\
    a_{m,1} & a_{m,2} & \cdots & a_{m,n} \\
    \end{bmatrix} \\[1em]
    & = \begin{bmatrix}
    c\cdot a_{1,1} & c\cdot a_{1,2} & \cdots & c\cdot a_{1,n} \\
    c\cdot a_{2,1} & c\cdot a_{2,2} & \cdots & c\cdot a_{2,n} \\
    \vdots & \vdots   & \ddots & \vdots \\
    c\cdot a_{m,1} & c\cdot a_{m,2} & \cdots & c\cdot a_{m,n} \\
    \end{bmatrix}
    \end{split}


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        A = \begin{bmatrix}
        3 & 5 & 12 \\
        -1 & -7 & 4
        \end{bmatrix}
        \qquad
        4A = \begin{bmatrix}
        12 & 20 & 48 \\
        -4 & -28 & 16
        \end{bmatrix}
        \end{split}


Addition and Subtraction
^^^^^^^^^^^^^^^^^^^^^^^^

Two matrices can be added or subtracted when they have the same dimensions. For two :math:`m` by :math:`n` matrices, :math:`A = (a_{i, j})` and :math:`B = (b_{i, j})`, their sum :math:`A + B` is equal to :math:`(a_{i, j} + b_{i, j})`. That is, each entry of :math:`A` is added to the corresponding entry in :math:`B` in the same position.


.. math::

    \begin{aligned}
    \begin{bmatrix}
    a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
    a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
    \vdots & \vdots   & \ddots & \vdots \\
    a_{m,1} & a_{m,2} & \cdots & a_{m,n} \\
    \end{bmatrix}  +
    \begin{bmatrix}
    b_{1,1} & b_{1,2} & \cdots & b_{1,n} \\
    b_{2,1} & b_{2,2} & \cdots & b_{2,n} \\
    \vdots & \vdots   &  \ddots & \vdots \\
    b_{m,1} & b_{m,2} & \cdots & b_{m,n} \\
    \end{bmatrix} &= \\[1em]
    \begin{bmatrix}
    a_{1,1} + b_{1,1} & a_{1,2} + b_{1,2} &\cdots & a_{1,n} + b_{1,n} \\
    a_{2,1} + b_{2,1} & a_{2,2} + b_{2,2} & \cdots & a_{2,n} + b_{2,n} \\
    \vdots & \vdots    &  \ddots & \vdots \\
    a_{m,1} + b_{m,1} & a_{m,2} + b_{m,2} & \cdots & a_{m,n} + b_{m,n} \\
    \end{bmatrix} &
    \end{aligned}


By scalar multiplication, we can define subtraction via addition:


.. math::

    A - B = A + (-1)B


To add or subtract matrices they must be of the same dimensions. Every entry in the first matrix must have a corresponding entry in the second matrix to be added to.


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        \begin{bmatrix}
        1 & -4 & 8\\
        11 & 2 & 24 \\
        12 & 4 & 1 \\
        \end{bmatrix}
        +
        \begin{bmatrix}
        -9 & 8 & 6 \\
        0 & 15 & 2 \\
        3 & 14 & 0
        \end{bmatrix}
        =
        \begin{bmatrix}
        -8 & 4 & 14 \\
        11 & 17 & 26 \\
        15 & 18 & 1
        \end{bmatrix}
        \end{split}


Matrix Multiplication
^^^^^^^^^^^^^^^^^^^^^

Matrix multiplication is much more involved than addition. First, we must consider under which conditions two matrices can be multiples.

Matrix multiplication between two matrices is only defined when the number of columns in the left-hand matrix equals the number of rows in the right-hand matrix. The result of the multiplication is another matrix whose number of rows equals the left-hand matrix's and whose number of columns equals the right-hand matrix's.


.. math::

    A_{m\times n} \cdot B_{n\times p} = C_{m \times p}


In this notation, the "inner" dimensions must be the same, and the "outer" dimensions give the dimensions of the product. In this case, :math:`n = n` are the inner dimensions, and :math:`m, p` are the outer dimensions.

But how do we define the entries of the product :math:`C = (c_{i, j})`? Each entry of the matrix product :math:`c_{i, j}` is an *inner product* of the :math:`i \text{th}` row of :math:`A` and the :math:`j \text{th}` column of B.


.. math::

    \begin{split}
    c_{i,j} &=
    \begin{bmatrix}
    a_{i,1} & a_{i,2} & a_{i,3} & \cdots & a_{i,n} \\
    \end{bmatrix} \cdot
    \begin{bmatrix}
    b_{1,j} \\
    b_{2,j} \\
      b_{3,j} \\
      \vdots \\
      b_{n,j} \\
    \end{bmatrix} \\[1em]
    &= \left(a_{i,1}\cdot b_{1,j} + a_{i,2} \cdot b_{2,j} + \cdots + a_{i,n}\cdot b_{n,j}\right) \\[1em]
    &= \sum_{k=1}^n a_{i,k} \cdot b_{k,j}
    \end{split}


Therefore, the matrix multiplication :math:`A_{m\times n} \cdot B_{n\times p} = C_{m \times p}` is actually :math:`m \times p` individual inner products.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/MatrixMult.svg
    :align: center
    :class: bg-white
    :width: 80%

    A :math:`4` by :math:`4` matrix multiplication showing the inner product producing :math:`c_{2, 2}`.


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        \begin{bmatrix}
        -9 & 6 \\
        0 &  2 \\
        3 & 0
        \end{bmatrix}_{3\times\textcolor{green}{2}}
        & \times
        \begin{bmatrix}
        1 & -4 & 5 \\
        7 & 2 & 2 \\
        \end{bmatrix}_{\textcolor{green}{2}\times3} \\[1em]
        &  =
        \begin{bmatrix}
        (-9 \cdot 1) + (6 \cdot 7) & (-9\cdot -4) + (6 \cdot 2) &  (-9 \cdot 5) + (6 \cdot 2)  \\
        (0 \cdot 1) + (2 \cdot 7) & (0\cdot -4) + (2 \cdot 2) &  (0 \cdot 5) + (2 \cdot 2)  \\
        (3 \cdot 1) + (0 \cdot 7) & (3\cdot -4) + (0 \cdot 2) &  (3 \cdot 5) + (0 \cdot 2)  \\
        \end{bmatrix}_{3\times3} \\[1em]
        & =
        \begin{bmatrix}
        33 & 48 & -33 \\
        14 & 4 & 4 \\
        3 & -12 & 15 \\
        \end{bmatrix}_{3\times3}\end{split}


.. important::

    Matrix multiplication is not commutative. In general, :math:`AB \neq BA`.


Zero and Identity Matrices
^^^^^^^^^^^^^^^^^^^^^^^^^^

It is sometimes possible for :math:`AB = BA`. Two important examples are when one of the matrices is the **zero matrix** or the **identity matrix**.


Zero matrix
~~~~~~~~~~~

The **zero matrix** is a matrix with all zero entries. The :math:`m` by :math:`n` zero matrix is denoted by :math:`0_{m, n}`.


.. math::

    \begin{split}
    0_{m,n} = \left.\begin{bmatrix}
    0 & 0 & \cdots & 0 \\
    0 & 0 & \cdots &0 \\
    \vdots & \vdots   & \ddots & \vdots \\
    0 & 0 & \cdots & 0 \\
    \end{bmatrix}\
    \right\} \small{m \text{ rows}}
    \end{split}


Assuming matrix multiplication is defined, the product of a zero matrix by any other matrix is the zero-matrix (of possibly different dimension).


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        \begin{bmatrix}
        0 & 0 \\
        0 & 0 \\
        0 & 0 \\
        \end{bmatrix}
        \cdot
        \begin{bmatrix}
        2 & 1 & 6 \\
        5 & 3 & 3 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
        0 & 0 & 0 \\
        0 & 0 & 0 \\
        0 & 0 & 0 \\
        \end{bmatrix}
        \end{split}


For a matrix :math:`A = (a_{i, j})`, its main diagonal is the entries :math:`a_{i, j}` for which :math:`i = j`. In a square matrix of order :math:`n`, there are :math:`n` entries along the main diagonal. In a rectangular matrix, the smaller of the two dimensions determines the number of entries along the main diagonal.


.. math::

    \begin{split}
    \begin{bmatrix}
    \textcolor{green}{x} & 0 & 0 \\
    0 & \textcolor{green}{y} & 0 \\
    0 & 0 & \textcolor{green}{z} \\
    \end{bmatrix}
    \qquad
    \begin{bmatrix}
    \textcolor{green}{x} & 0 & 0 \\
    0 & \textcolor{green}{y} & 0 \\
    0 & 0 & \textcolor{green}{z} \\
    0 & 0 & 0 \\
    \end{bmatrix}
    \qquad
    \begin{bmatrix}
    \textcolor{green}{x} & 0 & 0 & 0 \\
    0 & \textcolor{green}{y} & 0 & 0\\
    0 & 0 & \textcolor{green}{z} & 0\\
    \end{bmatrix}
    \end{split}


Note that the other entries need to be :math:`0`. For example, the three main diagonals of the matrices in the zero multiplication example are :math:`(0, 0)`, :math:`(2, 3)`, and :math:`(0, 0, 0)`. If all entries not on the main diagonal *are* :math:`0`, then we call that matrix a **diagonal matrix**.


Identity matrix
~~~~~~~~~~~~~~~

The **identity matrix** is a square diagonal matrix with all entries of the main diagonal equal to :math:`1`. The identity matrix of order :math:`n` is denoted :math:`I_n`.

The property of the identity matrix is that any other matrix multiplied by the identity is equal to itself. For an :math:`m` by :math:`n` matrix :math:`A`, we have:


.. math::

    I_mA = AI_n = A.


If :math:`A` is a square matrix of order :math:`n`, then we have:


.. math::

    I_nA = AI_n = A.


We can also leave the order of the identity matrix implicit. For an :math:`m` by :math:`n` matrix :math:`A`, we write :math:`AI` to mean :math:`A` times :math:`I_n`. The dimensions of the other matrix dictate the order of the identity matrix.


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        \begin{bmatrix}
        1 & 0  \\
        0 & 1 \\
        \end{bmatrix}
        \cdot
        \begin{bmatrix}
        2 & 1 & 6 \\
        5 & 3 & 3 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
        2 & 1 & 6 \\
        5 & 3 & 3 \\
        \end{bmatrix} \\[1em]
        \begin{bmatrix}
        2 & 1 & 6 \\
        5 & 3 & 3 \\
        \end{bmatrix}
        \cdot
        \begin{bmatrix}
        1 & 0 & 0  \\
        0 & 1 & 0 \\
        0 & 0 & 1 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
        2 & 1 & 6 \\
        5 & 3 & 3 \\
        \end{bmatrix}
        \end{split}


Power of Matrices
^^^^^^^^^^^^^^^^^

For square matrices, we can define the power of a matrix as the repeated multiplication of the matrix with itself.

Let :math:`A` be a square matrix of order :math:`n`. Then:


.. math::

    A^0 = I_n, \qquad\qquad A^2 = AA, \qquad\qquad A^3 = AAA, \qquad\qquad\text{etc.}


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        \begin{bmatrix}
        2 & 6 \\
        5 & 3 \\
        \end{bmatrix}^2
        &=
        \begin{bmatrix}
        2 & 6 \\
        5 & 3 \\
        \end{bmatrix}
        \cdot
        \begin{bmatrix}
        2 & 6 \\
        5 & 3 \\
        \end{bmatrix} \\[1em]
        &=
        \begin{bmatrix}
        34 & 30 \\
        25 & 39 \\
        \end{bmatrix}\end{split}


Matrix Transpose
^^^^^^^^^^^^^^^^

A **transpose** is an operation performed on a matrix which reverses its dimensions. In particular, it exchanges the rows of the matrix with its columns.

Given an :math:`m` by :math:`n` matrix :math:`A`, its transpose is denoted :math:`A^T` and is an :math:`n` by :math:`m` matrix. :math:`A^T` is defined as:


.. math::

    \begin{split}
    A &= (a_{i,j}) =
    \begin{bmatrix}
    a_{1,1} & \textcolor{green}{a_{1,2}} & \cdots & a_{1,n} \\
    a_{2,1} & \textcolor{green}{a_{2,2}} & \cdots & a_{2,n} \\
    a_{3,1} & \textcolor{green}{a_{3,2}} & \cdots & a_{3,n} \\
    a_{4,1} & \textcolor{green}{a_{4,2}} & \cdots & a_{4,n} \\
    \vdots & \textcolor{green}{\vdots}   &  \ddots & \vdots \\
    a_{m,1} & \textcolor{green}{a_{m,2}} & \cdots & a_{m,n} \\
    \end{bmatrix} \\[1em]
    A^T &= (a_{j,i}) =
    \begin{bmatrix}
    a_{1,1} & a_{2,1} & a_{3,1} & a_{4,1} & \cdots & a_{m,1} \\
    \textcolor{green}{a_{1,2}} & \textcolor{green}{a_{2,2}} & \textcolor{green}{a_{3,2}} & \textcolor{green}{a_{4,2}} & \textcolor{green}{\cdots} & \textcolor{green}{a_{m,2} }\\
    \vdots & \vdots   & \vdots  & \vdots &  \ddots & \vdots \\
    a_{1,n} & a_{2,n} & a_{3,n} & a_{4,n} & \cdots & a_{m,n} \\
    \end{bmatrix}
    \end{split}


Notice that the second column becomes the second row.

Since a transpose changes the dimensions, the transpose of a "tall" matrix is a "wide" matrix. Visually, matrix transposition "flips" or "rotates" the entries of the matrix along its main diagonal. The entries on the main giagonal do not change.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/Matrix_transpose.gif
    :align: center
    :width: 33%

    Animated matrix transpose.


Matrix transposition is easily reversible. Simply apply the transpose a second time.


.. math::

    A = {(A^T)}^T


Notice also that the identity matrix is not affected by transposition.


.. math::

    I = I^T = {I^T}^T


Zero-One Matrices
+++++++++++++++++

A special class of matrices whose entries come from the set :math:`\{0, 1\}` are called **zero-one matrices**. These matrices have numerous and important applications in computer science. Indeed, :math:`\{0, 1\}` may represent binary digits, ubiquitous in computer science.

Moreover, we can use :math:`\{0, 1\}` to encode truth values :bdg-danger-line:`false` and :bdg-success-line:`true`, respectively. This extends propositional logic to matrices.


.. seealso::

    `Propositions -- Connectives`_


Join and Meet
^^^^^^^^^^^^^

FOr two zero-one matrices, we can define operations similar to matrix addition, but using :math:`\wedge` and :math:`\vee` isntead of :math:`+`. Let :math:`A = (a_{i, j})` and :math:`B = (b_{i, j})` be :math:`m` by :math:`n` matrices.


The *join* of :math:`A` and :math:`B` is the :math:`m` by :math:`n` zero-one matrix defined as:


.. math::

    A \lor B = (a_{i,j} \lor b_{i,j})


The *meet* of :math:`A` and :math:`B` is the :math:`m` by :math:`n` zero-one matrix defined as:


.. math::

    A \land B = (a_{i,j} \land b_{i,j})


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        A = \begin{bmatrix}
        1 & 0 & 1\\
        0 & 1 & 0 \\
        \end{bmatrix}
        \qquad\qquad
        B = \begin{bmatrix}
        0 & 1 & 1\\
        1 &  1 & 0\\
        \end{bmatrix}
        \end{split}


    The join of :math:`A` and :math:`B` is:


    .. math::

        \begin{split}
        A \lor B = \begin{bmatrix}
        1 \lor 0 & 0 \lor 1 & 1 \lor 1\\
        0 \lor 1& 1 \lor 1& 0 \lor 0\\
        \end{bmatrix}
        =\
        \begin{bmatrix}
        1 & 1 & 1\\
        1 &  1 & 0\\
        \end{bmatrix}
        \end{split}


    The meet of :math:`A` and :math:`B` is:


    .. math::

        \begin{split}
        A \land B = \begin{bmatrix}
        1 \land 0 & 0 \land 1 & 1 \land 1\\
        0 \land 1& 1 \land 1& 0 \land 0\\
        \end{bmatrix}
        =\
        \begin{bmatrix}
        0 & 0 & 1\\
        0 &  1 & 0\\
        \end{bmatrix}
        \end{split}


Boolean Product
^^^^^^^^^^^^^^^

Similar to matrix multiplication, we can define a multiplication-like operation using zero-one matrices.

The typical *inner product* used matrix multiplication replaced by a "disjunction of conjunctions".

Let :math:`A` be an :math:`m` by :math:`n` zero-one matrix and :math:`B` be an :math:`n` by :math:`o` zero-one matrix. The boolean product of :math:`A` and :math:`B`, denoted :math:`A \odot B` is an :math:`m` by :math:`p` zero-one matrix with elements :math:`c_{i, j}` defiend as:


.. math::

    \begin{split}
    c_{i,j} &=
    \begin{bmatrix}
    a_{i,1} & a_{i,2} & a_{i,3} & \cdots & a_{i,n} \\
    \end{bmatrix} \odot
    \begin{bmatrix}
    b_{1,j} \\
    b_{2,j} \\
      b_{3,j} \\
      \vdots \\
      b_{n,j} \\
    \end{bmatrix} \\[1em]
    &= \left(a_{i,1}\land b_{1,j}) \ \ \lor\ \  (a_{i,2} \land b_{2,j}) \ \ \lor\ \  \cdots \ \ \lor\ \  (a_{i,n}\land b_{n,j}\right) \\[1em]
    \end{split}


.. admonition:: Example
    :class: hint


    .. math::

        \begin{split}
        \begin{bmatrix}
        1 &  0\\
        0 &  1\\
        1 &  0\\
        \end{bmatrix} &\odot
        \begin{bmatrix}
        1 & 1 & 0 \\
        0 & 1 & 1 \\
        \end{bmatrix}\\[1em]
        &=
        \begin{bmatrix}
        (1 \land 1) \lor (0 \land 0) & (1\land 1) \lor (0 \land 1) &  (1 \land 0) \lor (0 \land 1)  \\
        (0 \land 1) \lor (1 \land 0) & (0\land 1) \lor (1 \land 1) &  (0 \land 0) \lor (1 \land 1)  \\
        (1 \land 1) \lor (0 \land 0) & (1\land 1) \lor (0 \land 1) &  (1 \land 0) \lor (0 \land 1)  \\
        \end{bmatrix}\\[1em]
        &=
        \begin{bmatrix}
        1 \lor 0 & 1 \lor 0 & 0 \lor 0 \\
        0 \lor 0 & 0 \lor 1 & 0 \lor 1 \\
        1 \lor 0 & 1 \lor 0 & 0 \lor 0 \\
        \end{bmatrix}\\[1em]
        &=
        \begin{bmatrix}
        1 & 1 & 0 \\
        0 & 1 & 1 \\
        1 & 1 & 0 \\
        \end{bmatrix}
        \end{split}


For square zero-one matrices, we can extend Boolean product to **Boolean power**. Denote :math:`A^{[n]}` the Boolean product product of :math:`A` with itself :math:`n` times. Since Boolean products are associative, the order of operations does not matter for a Boolean power.


.. math::

    A^{[2]} = A \odot A, \qquad A^{[3]} = A^{[2]} \odot A = A \odot A^{[2]} = A \odot A \odot A, \qquad \text{etc.}\,


-----

.. admonition:: Sources
    :class: seealso
  
    `Matrices --- Discrete Structures for Computing`_


.. _Matrices --- Discrete Structures for Computing: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/Chapter3/matrices.html
.. _Propositions -- Connectives: ./propositions/#id1