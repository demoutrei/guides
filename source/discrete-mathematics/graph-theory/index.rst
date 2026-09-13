:description: Graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects. A graph in this context is made up of vertices (also called nodes or points) which are connected by edges (also called arcs, links, or lines). A distinction is made between undirected graphs, where edges link two vertices symmetrically, and directed graphs, where edges link two vertices asymmetrically. Graphs are oen of the principal objects of study in discrete mathematics.


Graph Theory
============

**Graph theory** is the study of graphs, which are mathematical structures used to model pairwise relations between objects. A **graph** in this context is made up of **vertices** (also called **nodes** or **points**) which are connected by **edges** (also called **arcs**, **links**, or **lines**). A distinction is made between **undirected graphs**, where edges link two vertices symmetrically, and **directed graphs**, where edges link two vertices asymmetrically. Graphs are one of the principal objects of study in discrete mathematics.


.. toctree::
    :maxdepth: 1
    :caption: Topics

    graphs
    directed-graphs


Glossary
++++++++


.. glossary::

    Adjacent Vertices
      Two vertices joined by an edge.

    Binary Tree
      A rooted tree where each vertex has at most 2 children.

    Bipartite Graph
      A graph whose vertices can be partitioned into two disjoint sets :math:`V_1` and :math:`V_2` such that every edge in :math:`E` has one endpoint in :math:`V_1` and one endpoint in :math:`V_2`.

    Complete Bipartite Graph
      A bipartite graph whose vertices can be partitioned into two sets :math:`V_1` and :math:`V_2` and there is an edge for every vertex in :math:`V_1` to every vertex in :math:`V_2`. Where :math:`|V_1| = m` and :math:`|V_2| = n`, the complete bipartite graph is denoted :math:`K_{m, n}`.

    Complete Graph
      A special kind of connected graph; not only must the graph be connected---there must be a path from every vertex to every other vertex---but each path must be of length :math:`1`.

    Connected Vertices
      Two vertices :math:`u, v` in a graph if there exists a path from :math:`u` to :math:`v`.

    Cycle Graph
      A graph with exactly one cycle. The cycle graph of order :math:`n` is denoted :math:`C_n`.

    Degree
      The number of edges incident with it. Note that a loop contributes 2 to its degree.

    Directed Graph
      A pair :math:`(V, E)` consisting of a non-empty set of vertices :math:`V` and a set of directed edges :math:`E` with :math:`E \subseteq V \times V`.

    Edge
      A connection or link between two vertices (nodes) in a graph.

    Endpoint
      A vertex of an edge. 

    Full Binary Tree
      A binary tree where every vertex has exactly 2 children or 0 children.

    Graph
      A pair :math:`(V, E)` consisting of a non-empty set of vertices :math:`V` and a set of edges :math:`E`.

    Graph Coloring
      Some way of labeling or grouping vertices.

    Graph Theory
      The study of graphs, which are mathematical structures used to model pairwise relations between objects.

    In-Degree
      The number of edges edges which terminate at :math:`v`. It is denoted :math:`deg^-(v)`.

    Level
      The distance of a vertex from the root.

    Loop
      An edge that starts and ends at the same vertex.

    Multigraph
      A graph that allows multiple edges between vertices.

    Neighbourhood
      The set of all vertices adjacent to :math:`v` in :math:`G`.

    Out-Degree
      The number of edges which start at :math:`v`. It is denoted :math:`deg^+(v)`.

    Parallel Edges
      Two or more edges joining a pair of vertices.

    Planar Graph
      A graph that can be drawn with no overlapping edges.

    Root
      "Oldest" ancestor in a rooted tree.

    Rooted Tree
      A tree in which one of the vertices has been designated as the root.

    Tree
      A simple connected graph with no cycles.

    Vertex
      A discrete object of the graph.

    Weighted Graph
      A graph where each edge is assigned a numerical label or "weight".

    Wheel Graph
      A cycle graph in which one extra vertex has been added which connects to every other vertex in the cycle. The wheel graph of order :math:`n` is denoted :math:`W_n`.


-----


.. admonition:: Sources
    :class: seealso

    `Graph theory - Wikipedia`_


.. _Graph theory - Wikipedia: https://en.wikipedia.org/wiki/Graph_theory