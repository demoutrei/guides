:description: A directed graph is a pair (V, E) consisting of a non-empty set of vertices and a set of directed edges.


Directed Graphs
===============

A **directed graph** is a pair :math:`(V, E)` consisting of a non-empty set of **vertices** :math:`V` and a set of **directed edges** :math:`E` with :math:`E \subseteq V \times V`.

- A directed edge is sometimes called an **arc**.

- A directed edge :math:`(u, v)` starts at :math:`u` and ends at :math:`v`. In other words, the directed edge has **initial vertex** :math:`u` and **terminal vertex** :math:`v`.

- Note that "simple directed graphs", "directed multigraphs", "simple (undirected) graphs", and "(undirected) multigraphs" are all different.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/digraph1.svg
    :align: center
    :class: bg-white
    :width: 80%

    A directed graph with 7 vertices and 8 directed edges.


The **in-degree** of a vertex :math:`v` in a directed graph is the number of edges which terminate at :math:`v`. It is denoted :math:`deg^-(v)`.

The **out-degree** of a vertex :math:`v` in a directed graph is the number of edges which start at :math:`v`. It is denoted :math:`deg^+(v)`.

- When a vertex in a directed graph has out-degree :math:`0`, we call that vertex a **sink**.

- When a vertex in a directed graph has in-degree :math:`0`, we call that vertex a **source**.


.. admonition:: Proof
    :class: hint

    Every edge in the graph has an initial vertex and a terminating vertex. Therefore, the total number of incoming edges in the graph is equal to the sum of the in-degrees of all vertices. The total number of outgoing edges is also equal to the sum of the out-degrees of all vertices.


Directed Connectivity
+++++++++++++++++++++

A **directed path** (or simply **path**) of a directed graph :math:`G = (V, E)` is a sequence of vertices :math:`(v_n)` where :math:`(v_i, v_{i+1}) \in E` for :math:`1 \leq i < n`.

In a directed graph, you must "follow the arrows". Edges can only be traversed *from* its initial vertex *to* its terminal vertex. We thus have the first kind of connectivity for a directed graph, which is the same definition (although different meaning) for a directed graph.

A directed graph is **strongly connected** if there is a directed path from every vertex to very other vertex.

In particular, as a corollary of this definition, a strongly connected directed graph cannot have any sink vertices or any source vertices. This is a natural consequence of the definitions.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/digraph-strong.svg
    :align: center
    :class: bg-white
    :width: 50%

    A strongly connected graph.


The graph shown above is strongly connected since a path exists from every vertex to every other vertex. It may be a rather complex path, a path exists nonetheless. For example, the path :math:`(3, 4, 2, 1)` connects node :math:`3` to node :math:`1`, the path :math:`(1, 2, 3)` connects node :math:`1` to node :math:`3`, etc.

Given a directed graph :math:`G = (V, E)`, its **underlying graph** is the undirected graph obtained by replacing every directed edge with an undirected edge.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/digraph2.svg
    :align: center
    :class: bg-white
    :width: 50%

    A directed graph with 7 vertices and 7 edges.


.. figure:: https://www.csd.uwo.ca/~abrandt5/teaching/DiscreteStructures/_images/digraph2-underlying.svg
    :align: center
    :class: bg-white
    :width: 50%

    The underlying graph. Notice that the edges :math:`(1, 5)` and :math:`(5, 1)` collapsed to :math:`\{1, 5\}`.


A directed graph is **weakly connected** if its underlying graph is connected.

