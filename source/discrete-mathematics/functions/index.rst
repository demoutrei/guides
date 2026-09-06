Functions
=========

A **function** is a rule that assigns each input exactly one output. We call the output the **image** of the input. The set of all inputs for a function is called the **domain**. The set of all allowable outputs is called the **codomain**. We would write :math:`f : X → Y` to describe a function with name :math:`f`, domain :math:`X` and codomain :math:`Y`. This does not tell us *which* function :math:`f` is though. To define the function, we must describe the rule. This is often done by giving a formula to compute the output for any input (although this is certainly not the only way to describe the rule).

For example, consider the function :math:`f : ℕ → ℕ` defined by :math:`f(x) = x ^ 2 + 3`. Here the domain and codomain are the same set (the natural numbers). The rule is: take your input, multiply it by itself and add :math:`3`.This works because we can apply this rule to every natural number (every element of the domain) and the result is always a natural number (an element of the codomain). Notice though that not every natural number is actually an output (there is no way to get :math:`0`, :math:`1`, :math:`2`, :math:`5`, etc.). The set of natural numbers that *are* outputs is called the **range** of the function (in this case, the range is :math:`\{ 3, 4, 7, 12, 19, 28, ... \}`, all the natural numbers that are 3 or more than a perfect square).

The key thing that makes a rule a *function* is that there is *exactly one* output for each input. That is, it is important that the rule be a good rule. What output do we assign to the input :math:`7`? There can only be one answer for any particular.


.. admonition:: Function Properties
    :class: tip

    1. `Injection <./injection>`_
    2. `Surjection <./surjection>`_
    3. `Bijection <./bijection>`_


.. admonition:: How To Find Domain of a Function
    :class: tip

    For **polynomial functions**, the domain is :math:`D(-∞, ∞)`.

    For **rational functions**, equate the denominator not equal to :math:`0`, and solve to isolate :math:`x`. Example:

    .. math::

        f(x) = \frac{5}{x - 2}

        x - 2 ≠ 0

        x ≠ 2

    Therefore, the domain of :math:`f(x)` is :math:`D(-∞, 2) ∪ D(2, ∞)`.

    For **radical functions**, equate the radicand not equal to :math:`0`, and solve to isolate :math:`x`.


Arithmetic Operations
^^^^^^^^^^^^^^^^^^^^^


Addition
~~~~~~~~

To add two functions, you combine their outputs for the same input by writing :math:`(f + g)(x) = f(x) + g(x)`.


.. admonition:: How To Add Functions
    :class: tip

    Write the rule
      Express the sum as the two individual function rules added together.

    Substitute expressions
      Replace :math:`f(x)` and :math:`g(x)` with their algebraic formulas.

    Combine like terms
      Group matching variable powers and constants to simplify the final expression.


.. admonition:: Example
    :class: hint

    Given :math:`f(x) = 2x + 1` and :math:`g(x) = 3x ^ 2 - 5`:

    Set up the addition:

    .. math::

        (f + g)(x) = (2x + 1) + (3x ^ 2 - 5)

    Order by powers:

    .. math::

        (f + g)(x) = 3x^2 + 2x + 1 - 5

    Simplify constants:

    .. math::

        (f + g)(x) = 3x^2 + 2x - 4


Subtraction
~~~~~~~~~~~

Subtracting two functions means creating a new function by taking the output of the second function away from the first, written as :math:`(f - g)(x) = f(x) - g(x)`.


.. admonition:: How To Subtract Functions
    :class: tip

    Write the rule
      Express the operation as :math:`(f - g)(x) = f(x) - g(x)`

    Use parentheses
      Put the second function :math:`g(x)` inside parentheses.

    Distribute the negative
      Multiply every term inside the second function's parentheses by :math:`-1`.

    Combine like terms
      Add or subtract matching power terms to simplify the final expression.


.. admonition:: Example
    :class: hint

    Given :math:`f(x) = 3x - 4` and :math:`g(x) = x^2 + 1`:

    Set up the subtraction:

    .. math::

        (f - g)(x) = (3x - 4) - (x^2 + 1)

    Distribute the negative sign:

    .. math::

        (f - g)(x) = 3x - 4 - x^2 - 1

    Combine like terms and rearrange:

    .. math::

        (f - g)(x) = -x^2 + 3x - 5


Multiplication
~~~~~~~~~~~~~~

To multiply two functions, you multiply their individual outputs together for any given input :math:`x`, written as :math:`(f ⋅ g)(x) = f(x) ⋅ g(x)`.


.. admonition:: How To Multiply Functions
    :class: tip

    Write the rule
      The product of two functions is written as :math:`(f ⋅ g)(x)` or :math:`f(x) ⋅ g(x)`.

    Substitute the expressions
      Replace :math:`f(x)` and :math:`g(x)` with their given algebraic formulas.

    Expand and distribute
      Use the distributive property, FOIL (First, Outer, Inner, Last), or a multiplication grid to multiple the terms.

    Combine like-terms
      Add or subtract any matching power terms to simplify the final polynomial expression.


.. admonition:: Example
    :class: hint

    Given :math:`f(x) = 2x - 3` and :math:`g(x) = x + 1`, find :math:`(f ⋅ g)(x)`:

    Set up the product:

    .. math::

        (f ⋅ g)(x) = (2x - 3)(x + 1)

    Distribute each term and multiply:

    .. math::

        (f ⋅ g)(x) = 2x^2 + 2x - 3x - 3

    Combine like-terms:
    
    .. math::
        (f ⋅ g)(x) = 2x^2 - x - 3


Division
~~~~~~~~

The division of two functions, :math:`f(x)` and :math:`g(x)`, is written as :math:`(f / g)(x)` and equals :math:`\frac{f(x)}{g(x)}`, provided that the denominator :math:`g(x)` is not equal to zero.


.. admonition:: How To Divide Functions
    :class: tip

    Notation
      Write the first function over the second function as a fraction.

    Domain restrictions
      Exclude any x-values that make the denominator :math:`g(x) = 0`.

    Simplification
      Factor the numerator and denominator when possible to reduce the rational expression to its simplest form.


.. admonition:: Example
    :class: hint

    Given :math:`f(x) = 2x^2 + 15x - 8` and :math:`g(x) = x^2 + 10x + 16`:

    Divide:

    .. math::

        \frac{f(x)}{g(x)} = \frac{2x^2 + 15x - 8}{x^2 + 10x + 16}

    Factor:

    .. math::

        \frac{f(x)}{g(x)} = \frac{(2x - 1)(x + 8)}{(x + 2)(x + 8)}

    Simplify:

    .. math::

        \frac{f(x)}{g(x)} = \frac{2x - 1}{x + 2}

    With the restriction :math:`x ≠ -8` and :math:`x ≠ -2`.


Composite
~~~~~~~~~

A composite function is a new function created by using the output of one function as the input for another function.


.. admonition:: How It Works
    :class: tip

    Inside Out
      Always evaluate the inner function first, then plug that result into the other function.

    Notation
      Written as :math:`(f ∘ g)(x)` or :math:`f(g(x))`, which means :math:`g(x)` goes inside :math:`f(x)`

    Order matters
      In most cases, :math:`f(g(x))` is different from :math:`g(f(x))`.


.. admonition:: Example
    :class: hint

    Given :math:`f(x) = x^2` and :math:`g(x) = x + 3`:

    To find :math:`f(g(x))`, replace the :math:`x` in :math:`f(x)` with the expression for :math:`g(x)`:

    .. math::

        (f ∘ g)(x) = x ^ 2

        (f ∘ g)(x) = g(x) ^ 2

    Substitute :math:`x + 3` into :math:`x ^ 2`:

    .. math::

        (f ∘ g)(x) = (x + 3) ^ 2

    Expand the result:

    .. math::

        (f ∘ g)(x) = x^2 + 6x + 9


Inverse
~~~~~~~

An inverse function is a mathematical operation that reverses or "undoes" the actions of an original function, written as :math:`f^{-1}(x)`.


.. admonition:: How To Find the Inverse
    :class: tip

    1. Replace :math:`f(x)` with :math:`y`.

    2. Swap every :math:`x` with :math:`y`  and every :math:`y` with :math:`x`.

    3. Solve the new equation to get :math:`y` by itself.
    
    4. Replace :math:`y` with the inverse notation :math:`f^{-1}(x)`.


.. admonition:: Example
    :class: hint

    Find the inverse of :math:`f(x) = 2x - 7`:

    Step 1: Replace :math:`f(x)` with :math:`y`:

    .. math::

        f(x) = 2x - 7

        y = 2x - 7

    Step 2: Swap :math:`x` and :math:`y`:

    .. math::

        x = 2y - 7

    Step 3: Add :math:`7` to both sides, the ndivide by :math:`2`:

    .. math::

        x + 7 = 2y

        y = \frac{x + 7}{2}

    Step 4: Replace :math:`y` with the inverse notation:

    .. math::

        f^{-1}(x) = \frac{x + 7}{2}


Types of Functions
^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 3
    
    injection
    surjection
    bijection
    many-to-one
    identity
    constant


Glossary
^^^^^^^^

A **function** is a rule that assigns each element of a set, called the **domain**, to exactly one element of a second set, called the **codomain**.

Notation :math:`f:X→Y` is the way of saying that the function is called :math:`f`, the domain is the set :math:`X`, and the codomain is the set :math:`Y`.

To specify the rule for a function with small domain, user **two-line notation** by writing a matrix with each output directly below its corresponding input, as in:

.. math::

    f = \begin{pmatrix}1 & 2 & 3 & 4 \\ 2 & 1 & 3 & 1 \end{pmatrix}

:math:`f(x)=y` means the element :math:`x` of the domain (input) is assigned to the element :math:`y` of the codomain. We say :math:`y` is an output. Alternatively, we call :math:`y` the **image of** :math:`x` **under** :math:`f`.

The **range** is a subset of the codomain. It is the set of all elements which are assigned to at least one element of the domain by the function. That is, the range is the set of all outputs.

A function is `injective <./injection>`_ if every element of the codomain is the image of at most one element from the domain.

A function is `surjective <./surjection>`_ if every element of the codomain is the image of at least one element from the domain.

A `bijection <./bijection>`_ is a function which is both an `injection <./injection>`_ and `surjection <./surjection>`_. In other words, if every element of the codomain is the image of exactly one element from the domain.

The **image** of an element :math:`x` in the domain is the element :math:`y` in the codomain that :math:`x` is mapped to. That is, the image of :math:`x` under :math:`f` is :math:`f(x)`.

The **complete inverse image** of an element :math:`y` in the codomain, written :math:`f^{-1}(y)`, is the set of all elements in the domain which are assigned to :math:`y` by the function.

The **image** of a subset :math:`A` of the domain is the set :math:`f(A) = \{ f(a) \in Y:a \in A \}`.

The **inverse image** of a subset :math:`B` of the codomain is the set :math:`f^{-1}(B) = \{ x \in X:f(x) \in B \}`.


-----


*Sources*
  `discrete.openmathbooks.org <https://discrete.openmathbooks.org/dmoi3/sec_intro-functions.html>`_