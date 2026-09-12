:description: A graph is a pair (V, E) consisting of a non-empty set of vertices V and a set of edges E.


Graphs
======

A **graph** is a pair :math:`(V, E)` consisting of a non-empty set of **vertices** :math:`V` and a set of **edges** :math:`E`. :math:`E` is a subset of the set :math:`\{\{u, v\} | u, v \in V\}`.

:math:`V` can be any set of discrete elements. Often, it is a subset of the natural numbers. On the other hand, :math:`E` is a set of subsets of :math:`V`. That is, :math:`E \subset \mathcal{P}(V)`.

Each of the elements of :math:`E` have:

1. two elements, for example :math:`\{u, v\}`, where :math:`u, v \in V`, or;

2. one element, for example :math:`\{v, v\} = \{v\}` for some vertex :math:`v \in V`.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/graph2.svg
    :align: center
    :class: bg-white
    :width: 80%

    A graph of 5 vertices.


In the figure above, we have a graph with 5 vertices and 5 edges.


.. math::

    V = \{1,2,3,4,5\} \qquad
    E = \{\{1,3\}, \{3,4\}, \{1,4\}, \{4,5\}, \{2,4\}\}


Special Edges
+++++++++++++

Parallel edges
  Two or more edges joining a pair of vertices.


Loops
  An edge that starts and ends at the same vertex.


The Language of Graphs
++++++++++++++++++++++

**Theories and Terminologies**

- A **simple graph** is what we have defined already as a graph. There is at most one edge between any two vertices.

- A **multigraph** is what we call a graph which allows multiple edges between vertices.

- A **node** or **vertex** is a discrete object of the graph.

- The two vertices of an edge are called **endpoints**. That edge is said to **join** or **connect** the two vertices and the edge is **incident** to each of the vertices it joins.

- When two vertices are joined by an edge, those vertices are called **adjacent**.

- An edge which connects a vertex to itself is called a **loop**.

- In some contexts, simple graphs do not allow loops.

- A graph :math:`G = (V, E)` of order :math:`n` has :math:`|V| = n`.

- The **neighbourhood** of a vertex :math:`v`, :math:`N(v)`, of a graph :math:`G = (V, E)` is the set of all vertices adjacent to :math:`v` in :math:`G`.


.. math::

    N(v) = \{u \ |\ \{u,v\} \in E\}


- The **degree** of a vertex :math:`v`, :math:`deg(v)`, is the number of edges incident with it. Note that a loop contributes 2 to its degree.


.. admonition:: Example
    :class: hint


    .. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/graph5.svg
        :align: center
        :class: bg-white
        :width: 80%


    In this graph :math:`G`, we have:

    - The order of :math:`G` is :math:`6`.

    - The degree of node :math:`3` is :math:`3`.

    - The degree of node :math:`5` is :math:`1`.

    - The degree of node :math:`6` is :math:`3`.

    - The neighbourhood of node :math:`3` is :math:`\{2, 4, 6\}`.

    - The neighbourhood of node :math:`6` is :math:`\{1, 3, 5\}`.


Connectivity
++++++++++++

A path of a simple graph :math:`G = (V, E)` is a sequence of vertices :math:`(v_n)` where an edge exists between :math:`v_i` and :math:`v_{i + 1}` for :math:`1 \leq i < n`.

Two vertices :math:`u, v` in a graph are **connected** if there exists a path from :math:`u` to :math:`v`. Otherwise, :math:`u` and :math:`v` are said to be **disconnected**. A graph is connected if every pair of vertices in the graph is connected.


.. admonition:: Example
    :class: hint


    .. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/graph9.svg
        :align: center
        :class: bg-white
        :width: 80%

        A connected graph.


    The above graph as many paths. And, in particular, *every* vertex is connected to every other vertex. Thus, the graph is a connected graph. In contrast, the graph below is disconnected.


    .. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/graph6.svg
        :align: center
        :class: bg-white
        :width: 80%

        A disconnected graph.


Complete Graphs
^^^^^^^^^^^^^^^

A **complete graph** is a special kind of connected graph. Not only must the graph be connected---there must be a path from every vertex to every other vertex---but each path must be of length :math:`1`. That is, every vertex must be adjacent to every other vertex. A complete graph of order :math:`n` is denoted :math:`K_n`.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completegraph123.svg
    :align: center
    :class: bg-white
    :width: 80%

    The complete graphs :math:`K_1`, :math:`K_2`, :math:`K_3`.


A graph containing a single vertex is complete (vacuously so). A graph containing two vertices connected by a single edge is also complete. A graph of three connected into a triangle is also complete.

The first complete graphs are rather simple, but they quickly grow to be very complex.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completegraph4.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`K_4`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completegraph5.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`K_5`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completegraph6.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`K_6`


Why are these so complex? Precisely because of the definition of a complete graph. There must be an edge between *every* pair of verices. Of course, we can count how many edges there will be.

A complete graph of order :math:`n` has :math:`\frac{n(n-1)}{2}` edges.


.. admonition:: Proof
    :class: hint

    A complete graph has an edge between any two vertices. For a graph with :math:`n` vertices, if we choose any two vertices, there must be an edge between them. There are :math:`\binom{n}{2}` such choices.


    .. math::

        \binom{n}{2} = \frac{n!}{(n-2)!2!} = \frac{(n-1)(n)}{2}.


Special Graphs
++++++++++++++

We have already seen complete graphs as a special graph with a special name. There are many other useful graphs with special names and different properties.


Cycles
^^^^^^

A **cycle graph** is a graph with exactly one cycle. The cycle graph of order :math:`n` is denoted :math:`C_n`.

As a consequence of cycles, a cycle graph must have 3 or more vertices.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/cyclegraph3.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`C_3`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/cyclegraph4.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`C_4`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/cyclegraph5.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`C_5`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/cyclegraph6.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`C_6`


Wheels
^^^^^^

A **wheel graph** is a cycle graph in which one extra vertex has been added which connects to every other vertex in the cycle. The wheel graph of order :math:`n` is denoted :math:`W_n`.

We call these "wheels" because they look like a wheel: a central hub and a tire or rim. The single vertex connected to every other is the "hub", the cycle is the "rim".


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/wheel4.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`W_4`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/wheel5.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`W_5`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/wheel6.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`W_6`


Notice that :math:`W_n` is :math:`C_{n - 1}` with the added hub vertex. Moreover, notice that :math:`W_4` is the same as :math:`K_4`.


Planar Graphs
^^^^^^^^^^^^^

A **planar** graph is a graph that can be drawn with no overlapping edges.

Every cycle graph is planar. Every wheel graph is planar. In contrast, every complete graph of order :math:`5` or higher is *not* planar.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/wheel6.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`W_6` is planar.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/cyclegraph6.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`C_6` is planar.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completegraph4.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`K_4` is planar, even if it does not look like it.


.. important::

    Just because planar graphs *can* be drawn with overlapping edges, does not mean that they are necessarily *not* planar.


:math:`K_4` is planar even though its typical way of drawing has crossed edges. Indeed, :math:`K_4` and :math:`W_4` are the same graph, and :math:`W_4` is obviously planar.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completegraph4.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`K_4` is planar.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/wheel4.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`W_4` is planar.


So, a graph is planar if there is *at least one way* of drawing it so that there are no crossed edges.


Bipartite Graphs
^^^^^^^^^^^^^^^^

A **bipartite graph** is a graph :math:`G = (V, E)` whose vertices can be partitioned into two disjoint sets :math:`V_1` and :math:`V_2` such that every edge in :math:`E` has one endpoint in :math:`V_1` and one endpoint in :math:`V_2`.

In a bipartite graph with vertices partitioned into :math:`V_1` and :math:`V_2`, there cannot be any edges within a partition.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/bipartite-cycle.svg
    :align: center
    :class: bg-white
    :width: 40%

    :math:`C_4` is a bipartite graph.


:math:`C_4` is a bipartite graph because its vertices can be partitioned into two groups so that there are no edges within either partition. In the case of :math:`C_4`, opposite corners are in the same partition, as indicated by the coloring above.

Bipartite graphs are highly related to the problem of **graph coloring**. Graph coloring is just some way of labeling or grouping vertices. Since graphs are highly visual, we usually use colors. But, "coloring" can mean any form of labeling of vertices.


.. tip::

    A graph is bipartite if its vertices can be colored using exactly two colors so that now two adjacent vertices have the same color.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/bipartite1.svg
    :align: center
    :class: bg-white
    :width: 80%

    A bipartite graph :math:`G`.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/bipartite1-2.svg
    :align: center
    :class: bg-white
    :width: 80%

    A coloring of :math:`G` with two colors.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/bipartite1-3.svg
    :align: center
    :class: bg-white
    :width: 80%

    Moving the vertices to explicitly show edges between colors.


.. tip::

    A simple graph is a bipartite graph if and only if it does not contain any cycles of odd length.


    .. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/oddcycle.svg
        :align: center
        :class: bg-white
        :width: 50%

        A graph with a cycle of length :math:`3` cannot be bipartite.


Complete Bipartite Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~

A **complete bipartite graph** is a bipartite graph whose vertices can be partitioned into two sets :math:`V_1` and :math:`V_2` and there is an edge for every vertex in :math:`V_1` to every vertex in :math:`V_2`. Where :math:`|V_1| = m` and :math:`|V_2| = n`, the complete bipartite graph is denoted :math:`K_{m, n}`.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completebip33.svg
    :align: center
    :class: bg-white
    :width: 50%

    :math:`K_{3, 3}`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completebip34.svg
    :align: center
    :class: bg-white
    :width: 80%

    :math:`K_{3, 4}`


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/completebip53.svg
    :align: center
    :class: bg-white
    :width: 80%

    :math:`K_{5, 3}`


Weighted Graph
^^^^^^^^^^^^^^

A graph where each edge is assigned a numerical label or "weight".


.. figure:: https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/
    :align: center
    :width: 80%


Trees
+++++

A **tree** is a simple connected graph with no cycles.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/tree1.svg
    :align: center
    :class: bg-white
    :width: 80%

    A tree with 9 vertices.


Rooted Trees and Children
^^^^^^^^^^^^^^^^^^^^^^^^^

A **rooted tree** is a tree in which one of the vertices has been designated as the **root**.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/tree1-root1.svg
    :align: center
    :class: bg-white
    :width: 80%

    A tree rooted at node :math:`1`.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/tree1-root3.svg
    :align: center
    :class: bg-white
    :width: 80%

    A tree rooted at node :math:`3`.


Designating a root in a tree includes special relationships between vertices. It derives from the fact that there is a unique simple path from any vertex to any other vertex in a tree. The terminology used most commonly is based on **ancestry**.

- The root is the "oldest" ancestor.

- Each of the **children** of the root are the vertices which have a path of length :math:`1` from the root.

- The children of those children are vertices which have a path of length :math:`2` from the root.

- Conversely, the children of the root tree have the root as their **parent**.

- To speak about a vertex's children and children's children, etc. we say **descendants**.

Visually, rooted trees are almost always drwan with the root at the top. Then, children are always drawn lower than their parents.

If we wanted to be very precise with the drawing of a rooted tree, we would draw every child at the same *level* of a tree at the same y-position. The **level** of a vertex in a tree is its distance from the root.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/tree1-root3-levels.svg
    :align: center
    :class: bg-white
    :width: 80%

    A "properly drawn" tree rooted at node :math:`3`.


A very important property of tree is that they admit a recursive description. For every non-root vertex :math:`v` in a tree, there is a subtree rooted at :math:`v`.

Given a non-root vertex :math:`v` of a rooted tree, the subtree rooted at :math:`v` is the subgraph rooted at :math:`v` and induced by :math:`v` and all its descendants.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/subtrees1.svg
    :align: center
    :class: bg-white
    :width: 80%

    Three subtrees of the previous tree figure: the subtree rooted at node :math:`7`, the subtree rooted at node :math:`8`, and the subtree rooted at node :math:`2`.


Binary Trees
^^^^^^^^^^^^

A **binary tree** is a rooted tree where each vertex has at most 2 children. A **full binary tree** is a binary tree where every vertex has exactly 2 children or 0 children.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/binarytree1.svg
    :align: center
    :class: bg-white
    :width: 80%

    A binary tree.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/binarytree1-full.svg
    :align: center
    :class: bg-white
    :width: 80%

    A full binary tree.


-----


.. admonition:: Sources
    :class: seealso

    `7.1 Graphs --- Discrete Structures for Computing`_

    `Graphs -- Discrete Math | PPT`_


.. _7.1 Graphs --- Discrete Structures for Computing: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/Chapter7/graphs.html
.. _Graphs -- Discrete Math | PPT: https://www.slideshare.net/slideshow/graphs-discrete-math/55596313