:description: Rules of Inference are standard logical templates used to build valid arguments and prove conclusions from given premises in propositional logic.


Rules of Inference
==================

To deduce new statements from the statements whose truth that we already know, **rules of inference** are used.

**Rules of inference** are standard logical templates used to build valid arguments and prove conclusions from given premises in propositional logic.


Addition
++++++++

If :math:`P` is a premise, we cna use Addition rule to derive :math:`P \vee Q`.


.. math::

    \begin{matrix}
    P \\
    \hline
    \therefore P \lor Q
    \end{matrix}


.. admonition:: Example
    :class: hint

      Let :math:`P`: *"He studies very hard"*

      Therefore: *"Either he studies very hard or he is a very bad student."*

    Here, :math:`Q` is the proposition *"He is a very bad student"*.


Conjunction
+++++++++++

If :math:`P` and :math:`Q` are two premises, we can use conjunction rule to derive :math:`P \wedge Q`.


.. math::

    \begin{matrix}
    P \\
    Q \\
    \hline
    \therefore P \land Q
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P`: *"He studies very hard."*

    Let :math:`Q`: *"He is the best boy in the class."*

    Therefore: *"He studies very hard and he is the best boy in the class."*


Simplification
++++++++++++++

If :math:`P \wedge Q` is a premise, we can use simplification rule to derive :math:`P`.


.. math::

    \begin{matrix}
    P \land Q\\
    \hline
    \therefore P
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P \wedge Q`: *"He studies very hard and he is the best boy in the class."*

    Therefore: *"He studies very hard."*


Modus Ponens
++++++++++++

If :math:`P` and :math:`P \rightarrow Q` are two premises, we can use modus ponens to derive :math:`Q`.


.. math::

    \begin{matrix}
    P \rightarrow Q \\
    P \\
    \hline
    \therefore Q
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P \rightarrow Q`: *"If you have a password, then you can log on to Facebook."*

    Let :math:`P`: *"You have a password."*

    Therefore: *"You can log on to Facebook."*


Modus Tollens
+++++++++++++

If :math:`P \rightarrow Q` and :math:`\lnot Q` are two premises, we can use modus tollens to derive :math:`\lnot P`.


.. math::

    \begin{matrix}
    P \rightarrow Q \\
    \lnot Q \\
    \hline
    \therefore \lnot P
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P \rightarrow Q`: *"If you have a password, then you can log on to Facebook."*

    Let :math:`\lnot Q`: *"You cannot log on to Facebook."*

    Therefore: *"You do not have a password."*


Disjunctive Syllogism
+++++++++++++++++++++

If :math:`\lnot P` and :math:`P \vee Q` are two premises, we can use disjunctive syllogism to derive :math:`Q`.


.. math::

    \begin{matrix}
    \lnot P \\
    P \lor Q \\
    \hline
    \therefore Q
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`\lnot P`: *"The ice cream is not vanilla flavored."*

    Let :math:`P \vee Q`: *"The ice cream is either vanilla flavored or chocolate flavored."*

    Therefore: *"The ice cream is chocolate flavored."*


Hypothetical Syllogism
++++++++++++++++++++++

If :math:`P \rightarrow Q` and :math:`Q \rightarrow R` are two premises, we can use hypothetical syllogism to derive :math:`P \rightarrow R`.


.. math::

    \begin{matrix}
    P \rightarrow Q \\
    Q \rightarrow R \\
    \hline
    \therefore P \rightarrow R
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P \rightarrow Q`: *"If it rains, I shall not go to school."*

    Let :math:`Q \rightarrow R`: *"If I don't go to school, I won't need to do homework."*

    Therefore: *"If it rains, I won't need to do homework."*


Constructive Dilemma
++++++++++++++++++++

If :math:`(P \rightarrow Q) \wedge (R \rightarrow S)` and :math:`P \vee R` are two premises, we can use constructive dilemma to derive :math:`Q \vee S`.


.. math::

    \begin{matrix}
    ( P \rightarrow Q ) \land (R \rightarrow S) \\
    P \lor R \\
    \hline
    \therefore Q \lor S
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P \rightarrow Q`: *"If it rains, I will take a leave."*

    Let :math:`R \rightarrow S`: *"If it is hot outside, I will go for a shower."*

    Let :math:`P \vee R`: *"Either it will rain or it is hot outside."*

    Therefore: *"I will take a leave or I will go for a shower."*


Destructive Dilemma
+++++++++++++++++++

If :math:`(P \rightarrow Q) \wedge (R \rightarrow S)` and :math:`\lnot Q \vee \lnot S` are two premises, we can use destructive dilemma to derive :math:`\lnot P \vee \lnot R`.


.. math::

    \begin{matrix}
    (P \rightarrow Q) \land (R \rightarrow S) \\
    \lnot Q \lor \lnot S \\
    \hline
    \therefore \lnot P \lor \lnot R
    \end{matrix}


.. admonition:: Example
    :class: hint

    Let :math:`P \rightarrow Q`: *"If it rains, I will take a leave."*

    Let :math:`R \rightarrow S`: *"If it is hot outside, I will go for a shower."*

    Let :math:`\lnot Q \vee \lnot S`: *"Either I will not take a leave or I will not go for a shower."*

    Therefore: *"Either it does not rain or it is not hot outside."*


-----

.. admonition:: Sources
    :class: seealso
  
    `Discrete Mathematics - Rules of Inference`_


.. _Discrete Mathematics - Rules of Inference: https://www.tutorialspoint.com/discrete_mathematics/rules_of_inference.htm