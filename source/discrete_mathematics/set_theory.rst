:description: Set theory in discrete mathematics is the foundational branch of mathematical logic that studies sets, which are unordered collections of distinct objects.


Set Theory
==========

**Set theory** forms the basis of several other fields of study like counting theory, relations, graph theory and finite state machines.


.. admonition:: Set Theory Notation
    :class: tip

    :math:`\{ , \}`
      We use braces to enclose the elements of a set. So :math:`\{ 1, 2, 3 \}` is the set containing :math:`1`, :math:`2`, and :math:`3`.

    :math:`:`
      :math:`\{ x : x > 2\}` is the set of all :math:`x` such that :math:`x` is greater than :math:`2`.

    :math:`\in`
      :math:`2 \in \{ 1, 2, 3 \}` asserts that :math:`2` is an element of the set :math:`\{ 1, 2, 3 \}`.

    :math:`\notin`
      :math:`4 \notin \{ 1, 2, 3 \}` because :math:`4` is not an element of the set :math:`\{ 1, 2, 3 \}`.

    :math:`\subseteq`
      :math:`A \subseteq B` asserts that :math:`A` is a subset of :math:`B`; every element of :math:`A` is also an element of :math:`B`.

    :math:`\subset`
      :math:`A \subset B` asserts that :math:`A` is a proper subset of :math:`B`; every element of :math:`A` is also an element of :math:`B`, but :math:`A \neq B`.

    :math:`\cap`
      :math:`A \cap B` is the intersection of :math:`A` and :math:`B`; the set containing all elements which are elements of both :math:`A` and :math:`B`.

    :math:`\cup`
      :math:`A \cup B` is the union of :math:`A` and :math:`B`; the set containing all elements which are elements of :math:`A` or :math:`B` or both.

    :math:`\times`
      :math:`A \times B` is the Cartesian product of :math:`A` and :math:`B`; the set of all ordered pairs :math:`( a, b )` with :math:`a \in A` and :math:`b \in B`.

    :math:`\setminus`
      :math:`A \setminus B` is set difference between :math:`A` and :math:`B`; the set containing all elements of :math:`A` which are not elements of :math:`B`.

    :math:`\bar{A}`
      The complement of :math:`A` is the set of everything which is not an element of :math:`A`.

    :math:`|A|`
      The cardinality (or size) of :math:`A` is the number of elements in :math:`A`.


Sets
++++

A **set** is an unordered collection of different elements. A set can be written explicitly by listing its elements using set bracket. If the order of the elements is changed or any element of a set is repeated, it does not make any changes in the set.


.. admonition:: Examples
    :class: hint

    - A set of all positive integers.

    - A set of all the planets in the solar system.

    - A set of all the states in India.

    - A set of all the lowercase letters of the alphabet.


Set Representations
+++++++++++++++++++


Roster or Tabular Form
^^^^^^^^^^^^^^^^^^^^^^

The set is represented by listing all the elements comprising it. The elements are enclosed within braces and separated by commas.


.. admonition:: Examples
    :class: hint

    Set of vowels in English alphabet, :math:`A = \{a, e, i, o, u\}`.

    Set of odd numbers less than :math:`10`, :math:`B = \{1, 3, 5, 7, 9\}`.


Set Builder Notation
^^^^^^^^^^^^^^^^^^^^

The set is defined by specifying a property that elements of the set have in common. The set is described as :math:`A = \{x : p(x)\}`.


.. admonition:: Examples
    :class: hint

    The set :math:`\{a, e, i, o, u\}` is written as:


    .. math::

        A = \lbrace x : \text{x is a vowel in English alphabet} \rbrace


    The set :math:`\{1, 3, 5, 7, 9\}` is written as:


    .. math::

        B = \lbrace x : 1 \le x \lt 10 \ and\ (x \% 2) \ne 0 \rbrace


If an element :math:`x` is a member of any set :math:`S`, it is denoted by :math:`x \in S`; and if an element :math:`y` is not a member of set :math:`S`, it is denoted by :math:`y \notin S`.


.. admonition:: Example
    :class: hint

    If :math:`S = \{1, 1.2, 1.7, 2\}`, :math:`1 \in S` but :math:`1.5 \notin S`.


.. admonition:: Some Important Sets
    :class: tip

    :math:`N` -- the set of all natural numbers: :math:`\{ 1, 2, 3, 4, ... \}`.

    :math:`Z` -- the set of all integers: :math:`\{ ..., -3, -2, -1, 0, 1, 2, 3, ... \}`.

    :math:`Z^+` -- the set of all positive integers: :math:`\{ 1, 2, 3, ... \}`.

    :math:`Q` -- the set of all rational numbers: :math:`\{ \frac{p}{q} | p, q \in Z, q \neq 0 \}`.

    :math:`R` -- the set of all real numbers.

    :math:`W` -- the set of all whole numbers: :math:`\{ 0, 1, 2, 3, ... \}`.


Natural Language Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is often called a **semantic description** of the set, where a sentence is used to describe the properties of objects contained in a set.

The following are valid semantic descriptions of sets:

- Let :math:`A` be the set of three primary colors: :math:`A = \{ \text{red}, \text{blue}, \text{yellow} \}`

- Let :math:`B` be the set of five smallest positive integers: :math:`B = \{ 1, 2, 3, 4, 5 \}`

- Let :math:`C` be the set of positive rational numbers with 1 as a numerator: :math:`C = \{1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots\}`


.. important::

    When using semantic descriptions, it is important that the sentence be as clear as possible and unambiguous.


Interval Notation
^^^^^^^^^^^^^^^^^

For sets of real numbers, a particularly useful notation is **interval notation**. We are probably familiar with this notation from calculus. For two real numbers :math:`a` and :math:`b`, such that :math:`a < b`, we have the following possible intervals:


.. math::

    \begin{array}{rll}
    (a,b)  &= \{x \in \mathbb{R} \mid a < x < b\} \\[1em]
    (a,b]  &= \{x \in \mathbb{R} \mid a < x \leq b\} \\[1em]
    [a,b)  &= \{x \in \mathbb{R} \mid a \leq x < b\} \\[1em]
    [a,b]  &= \{x \in \mathbb{R} \mid a \leq x \leq b\}
    \end{array}


The choice of including the end point of an interval or not determines if the interval is **closed** or **open**.

A **closed interval** is the set of all numbers between two end points, including those endpoints. It is denoted by square brackets. :math:`[a, b]` is all numbers :math:`x` such that :math:`a \leq x \leq b`.

An **open interval** is the set of all numbers between two end points, excluding those endpoints. It is denoted by parentheses. :math:`(a, b)` is all numbers :math:`x` such that :math:`a < x < b`.

A **half-open** or **half-closed** interval is where one endpoint is included and one endpoint is excluded. To be more precise, we can say **left-open** or **right-closed** to mean only the right end point is included, e.g. :math:`( a, b ]`. We can say **left-closed** or **right-open** to mean only the left end point is included, e.g. :math:`[ a, b )`.

When we want to describe intervals which are unbounded on one side (i.e. go until positive or negative infinity), we use a parenthesis and the infinity symbol.


.. math::

    \begin{split}
    (-\infty, a) = \{x \in \mathbb{R} \ |\ x < a\} \\[1em]
    (-\infty, a] = \{x \in \mathbb{R} \ |\ x \leq a\} \\[1em]
    (a, \infty) = \{x \in \mathbb{R} \ |\ x > a\} \\[1em]
    [a, \infty) = \{x \in \mathbb{R} \ |\ x \geq a\}
    \end{split}


Membership and Equality
+++++++++++++++++++++++

**Membership** is the basic property of sets from which all other operatiosn and properties can be defined. A set either contains an object or does not contain an object. Sets define a clear and unambiguous description of its members.

We have already seen the notation :math:`\in` which is used to say that an element is included in the set. The notation :math:`\notin` says an element is not included in a set.


.. math::

    \begin{aligned}
    a &\in \{a, b, c, d, e\} \\
    4 &\notin \{1, 3, 5, 7, 9, \ldots\}
    \end{aligned}


Again, membership is a strict binary---an object is either in a set or is not in a set. Because of that, we have the following results:


.. math::

    \begin{split}
    \begin{array}{l}
    1 \in \{1,2\} \\[0.5em]
    1 \in \{2,1\} \\[0.5em]
    1 \in \{1,1,1,2\}  \\[0.5em]
    1 \in \{1,1,1,2,2,27\}  \\[0.5em]
    3 \not\in \{1, 1, 1, 2\} \\[0.5em]
    \end{array}
    \end{split}


Stated in predicate logic, two sets are equal if :math:`\forall x (x \in A \leftrightarrow x \in B)`.

Because the only basic property of a set is membership, a set does not care about the order in which elements are listed or the number of times each element appears in the set construction. For example, the following sets are equal:


.. math::

    \{1,2\} = \{2,1\} = \{1,1,2\} = \{2,1,2,1,1,1,1,2,1,2,1,2,2\}


To avoid this awkward and "non-canonical" description of sets, it is often said that sets should only contain *unique*, *distinct*, and *distinguishable* objects. In particular, when using the roster method, one should only write each unique element once. Therefore, :math:`\{ 1, 2 \}` or :math:`\{ 2, 1 \}` is the most "correct" description of the previous set.


Cardinality of a Set
++++++++++++++++++++

**Cardinality** of a set :math:`S`, denoted by :math:`|S|`, is the number of elements of the set. The number is also referred as the cardinal number. If a set has an infinite number of elements, its cardinality is :math:`\infty`.


.. admonition:: Example
    :class: hint

    :math:`|\lbrace 1, 4, 3, 5 \rbrace | = 4, | \lbrace 1, 2, 3, 4, 5, \dots \rbrace | = \infty`


Types of Sets
+++++++++++++

Sets can be classified into many types. Some of which are finite, infinite, subset, universal, proper, singleton set, etc.


Finite Set
^^^^^^^^^^

A set which contains a definite number of elements is called a **finite set**.


.. admonition:: Example
    :class: hint

    
    :math:`S = \{ x | x \in N \text{and} 70 > x > 50 \}`


Infinite Set
^^^^^^^^^^^^

A set which contains infinite number of elements is called an **infinite set**.


.. admonition:: Example
    :class: hint

    :math:`S = \{ x | x \in N \text{and} x > 10 \}`


Subset
^^^^^^

A set :math:`X` is a subset of set :math:`Y` (written as :math:`X \subseteq Y`) if every element of :math:`X` is an element of set :math:`Y`.


.. admonition:: Examples
    :class: hint

    Let :math:`X = \{ 1, 2, 3, 4, 5, 6 \}` and :math:`Y = \{ 1, 2 \}`. Here, set :math:`Y` is a subset of set :math:`X` as all the elements of set :math:`Y` is in set :math:`X`. Hence, we can write :math:`Y \subseteq X`.

    Let :math:`X = \{ 1, 2, 3 \}` and :math:`\{ 1, 2, 3 \}`. Here, set :math:`Y` is a subset (not a proper subset) of set :math:`X` as all the elements of set :math:`Y` is in set :math:`X`. Hence, we can write :math:`Y \subseteq X`.


Proper Subset
^^^^^^^^^^^^^

The term **proper subset** can be defined as subset of but not equal to. A set :math:`X` is a proper subset of set :math:`Y` (written as :math:`X \subset Y`) if every element of :math:`X` is an element of set :math:`Y` and :math:`|X| < |Y|`.


.. admonition:: Example
    :class: hint

    Let :math:`X = \{ 1, 2, 3, 4, 5, 6 \}` and :math:`Y = \{ 1, 2 \}`. Here, set :math:`Y \subset X` since all elmeents in :math:`Y` are contained in :math:`X` too, and :math:`X` has at least one element more than set :math:`Y`.


Universal Set
^^^^^^^^^^^^^

It is a collection of all elements in a particular context or application. All the sets in that context or application are essentially subsets of this universal set. Universal sets are represented as :math:`U`.


.. admonition:: Example
    :class: hint

    We may define :math:`U` as the set of all animals on Earth. In this case, set of all mammals is a subset of :math:`U`, set of all fishes is a subset of :math:`U`, set of all insects is a subset of :math:`U`, and so on.


Empty Set or Null Set
^^^^^^^^^^^^^^^^^^^^^

An **empty set** contains no elements. It is denoted by :math:`\emptyset`. As the number of elements in an empty set is finite, empty set is a finite set. The cardinality of empty set or null set is zero.


.. admonition:: Example
    :class: hint

    :math:`S = \{ x | x \in N \text{and} 7 < x < 8 \} = \emptyset`


Singleton Set or Unit Set
^^^^^^^^^^^^^^^^^^^^^^^^^

**Singleton set** or **unit set** contains only one element. A singleton set is denoted by :math:`\{ s \}`.


.. admonition:: Example
    :class: hint

    :math:`S = \{ x | x \in N, 7 < x < 9 \} = \{ 8 \}`


Equal Set
^^^^^^^^^

If two sets contain the same elements, they are said to be equal.


.. admonition:: Example
    :class: hint

    If :math:`A = \{ 1, 2, 6 \}` and :math:`B = \{ 6, 1, 2 \}`, they are equal as every element of set :math:`A` is an element of set :math:`B`, and every element of set :math:`B` is an element of set :math:`A`.


Equivalent Set
^^^^^^^^^^^^^^

If the cardinalities of two sets are same, they are called **equivalent sets**.


.. admonition:: Example
    :class: hint

    If :math:`A = \{ 1, 2, 6 \}` and :math:`B = \{ 16, 17, 22 \}`, they are equivalent as cardinality of :math:`A` is equal to the cardinality of :math:`B`, i.e. :math:`|A| = |B| = 3`.


Overlapping Set
^^^^^^^^^^^^^^^

Two sets that have at least one common element are called **overlapping sets**.

In case of overlapping sets:

- :math:`n(A \cup B) = n(A) + n(B) - n(A \cap B)`

- :math:`n(A \cup B) = n(A - B) + n(B - A) + n(A \cap B)`

- :math:`n(A) = n(A - B) + n(A \cap B)`

- :math:`n(B) = n(B - A) + n(A \cap B)`


.. admonition:: Example
    :class: hint

    Let :math:`A = \{ 1, 2, 6 \}` and :math:`B = \{ 6, 12, 42 \}`. There is a common element :math:`6`, hence these sets are overlapping sets.


Disjoint Set
^^^^^^^^^^^^

Two sets :math:`A` and :math:`B` are called **disjoin sets** if they do not have even one element in common. Therefore, disjoint sets have the following properties:

- :math:`n(A \cap B) = \emptyset`

- :math:`n(A \cup B) = n(A) + n(B)`


.. admonition:: Example
    :class: hint

    Let :math:`A = \{ 1, 2, 6 \}` and :math:`B = \{ 7, 9, 14 \}`, there is not a single common element, hence these sets are disjoint sets.


Venn Diagrams
+++++++++++++

Venn diagram, invented in 1880 by John Venn, is a schematic diagram that shows all possible logical relations between different mathematical sets.


.. figure:: https://www.tutorialspoint.com/discrete_mathematics/images/venn_diagram.jpg
    :align: center
    :width: 80%


Set Operations
++++++++++++++

Set operations include Set Union, Set Intersection, Set Difference, Complement of Set, and Cartesian Product.


Set Union
^^^^^^^^^

The union of sets :math:`A` and :math:`B` (denoted by :math:`A \cup B`) is the set of elements which are in :math:`A`, in :math:`B`, or in both :math:`A` and :math:`B`. Hence, :math:`A \cup B = \lbrace x \:| \: x \in A\ OR\ x \in B \rbrace`.


.. admonition:: Example
    :class: hint

    If :math:`A = \{ 10, 11, 12, 13 \}` and :math:`B = \{ 13, 14, 15 \}`, then :math:`A \cup B = \{ 10, 11, 12, 13, 14, 15 \}`. (The common element occurs only once.)


.. figure:: https://www.tutorialspoint.com/discrete_mathematics/images/set_union.jpg
    :align: center
    :width: 80%


Set Intersection
^^^^^^^^^^^^^^^^

The intersection of sets :math:`A` and :math:`B` (denoted by :math:`A \cap B`) is the set of elements which are in both :math:`A` and :math:`B`. Hence, :math:`A \cap B = \{ x | x \in A \text{AND} x \in B \}`.


.. admonition:: Example
    :class: hint

    If :math:`A = \{ 11, 12, 13 \}` and :math:`B = \{ 13, 14, 15 \}`, then :math:`A \cap B = \{ 13 \}`.


.. figure:: https://www.tutorialspoint.com/discrete_mathematics/images/set_intersection.jpg
    :align: center
    :width: 50%


Set Difference
^^^^^^^^^^^^^^

The set difference of sets :math:`A` and :math:`B` (denoted by :math:`A - B`) is the set of  elements which are only in :math:`A` but not in :math:`B`. Hence, :math:`A - B = \{ x | x \in A \text{AND} x \notin B \}`.


.. admonition:: Example
    :class: hint

    If :math:`A = \{ 10, 11, 12, 13 \}` and :math:`B = \{ 13, 14, 15 \}`, then :math:`A - B = \{ 10, 11, 12 \}` and :math:`B - A = \{ 14, 15 \}`. Here, we can see :math:`A - B \neq B - A`.


.. figure:: https://www.tutorialspoint.com/discrete_mathematics/images/set_difference.jpg
    :align: center
    :width: 80%


Symmetric Difference
~~~~~~~~~~~~~~~~~~~~

A special kind of difference is **symmetric difference**. It is the set-equivalent of "exclusive or" from propositional logic.

The **symmetric difference** of two sets :math:`A` and :math:`B` is the set of elements which are members of :math:`A` or members of :math:`B` but not both. The symmetric difference of :math:`A` and :math:`B` is denoted :math:`A \oplus B`.

The "symmetric" in symmetric difference comes from the following identity:


.. math::

    A \oplus B = (A \setminus B) \cup (B \setminus A)


However, a more intuitive way to think about symmetric difference is as the union of two sets minus their intersection.


.. math::

    A \oplus B = (A \cup B) \setminus (A \cap B)


Which leads to the following Venn diagram.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/VennSymmDiff.svg
    :align: center
    :class: bg-white
    :width: 50%

    The symmetric difference of two sets :math:`A` and :math:`B` is their union minus their intersection.


Complement of a Set
^^^^^^^^^^^^^^^^^^^

The complement of a set :math:`A` (denoted by :math:`A'`) is the set of elements which are not in set :math:`A`. Hence, :math:`A' = \{ x | x \notin A \}`.

More specifically, :math:`A' = U - A` where :math:`U` is a universal set which contains all objects.


.. admonition:: Example
    :class: hint

    If :math:`A = \{ x | x \text{belongs to set of odd integers} \}`, then :math:`A' = \{ y | y \text{does not belong to set of odd integers} \}`.


.. figure:: https://www.tutorialspoint.com/discrete_mathematics/images/complement_set.jpg
    :align: center
    :width: 50%


Cartesian Product
^^^^^^^^^^^^^^^^^

The **Cartesian product** of :math:`n` number of sets :math:`A_1, A_2, ..., A_n` denoted as :math:`A_1 \times A_2 \times ... \times A_n` can be defined as all possible oredered pairs :math:`(x_1, x_2, ..., x_n)` where :math:`x_1 \in A, x_2 \in A_2, ..., x_n \in A_n`.


.. admonition:: Example
    :class: hint

    If we take two sets :math:`A = \{ a, b \}` and :math:`B = \{ 1, 2 \}`;

    The Cartesian product of :math:`A` and :math:`B` is writted as:


    .. math::

        A \times B = \lbrace (a, 1), (a, 2), (b, 1), (b, 2)\rbrace


    The Cartesian product of :math:`B` and :math:`A` is writted as:

    
    .. math::

        B \times A = \lbrace (1, a), (1, b), (2, a), (2, b)\rbrace


Power Set
+++++++++

**Power set** of a set :math:`S` is the set of all subsets of :math:`S` including the empty set. The cardinality of a power set of a set :math:`S` of cardinality :math:`n` is :math:`2^n`. Power set is denoted as :math:`P(S)`.


.. admonition:: Example
    :class: hint

    For a set :math:`S = \{ a, b, c, d \}`, let us calculate the subsets:

    - Subsets with 0 elements: :math:`\{ \emptyset \}`

    - Subsets with 1 element: :math:`\lbrace a \rbrace, \lbrace b \rbrace, \lbrace c \rbrace, \lbrace d \rbrace`

    - Subsets with 2 elements: :math:`\lbrace a, b \rbrace, \lbrace a,c \rbrace, \lbrace a, d \rbrace, \lbrace b, c \rbrace, \lbrace b,d \rbrace,\lbrace c,d \rbrace`

    - Subsets with 3 elements: :math:`\lbrace a ,b, c\rbrace,\lbrace a, b, d  \rbrace, \lbrace a,c,d \rbrace,\lbrace b,c,d \rbrace`

    - Subsets with 4 elements: :math:`\lbrace a, b, c, d \rbrace`

    Hence, :math:`P(S) =`
    

    .. math::

        \lbrace \quad \lbrace \emptyset \rbrace, \lbrace a \rbrace, \lbrace b \rbrace, \lbrace c \rbrace, \lbrace d \rbrace, \lbrace a,b \rbrace, \lbrace a,c \rbrace, \lbrace a,d \rbrace, \lbrace b,c \rbrace, \lbrace b,d \rbrace, \lbrace c,d \rbrace, \lbrace a,b,c \rbrace, \lbrace a,b,d \rbrace, \lbrace a,c,d \rbrace, \lbrace b,c,d \rbrace, \lbrace a,b,c,d \rbrace \quad \rbrace


    :math:`| P(S) | = 2^4 = 16`


.. note::

    The power set of an empty set is also an empty set.

    :math:`| P (\lbrace \emptyset \rbrace) | = 2^0 = 1`


-----


.. admonition:: Sources
    :class: seealso

    `discrete.openmathbooks.org`_

    `Discrete Structures for Computing`_

    `tutorialspoint.com`_


.. _discrete.openmathbooks.org: https://discrete.openmathbooks.org/dmoi3/sec_intro-sets.html
.. _Discrete Structures for Computing: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/Chapter2/set-theory.html
.. _tutorialspoint.com: https://www.tutorialspoint.com/discrete_mathematics/discrete_mathematics_sets.htm