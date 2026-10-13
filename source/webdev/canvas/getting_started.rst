Getting Started
===============

``<canvas>`` is an HTML elment which can be used to draw graphics via scripting (usually JavaScript). This can, for instance, be used to draw graphs, combine photos, or create simple animations.

.. code-block:: html

    <canvas width="200" height="200">
      An alternative text describing what your canvas displays.
    </canvas>

The canvas is initially blank. To display something, a script first needs to access the rendering context and draw on it. The ``<canvas>`` element has a method called ``getContext()``, used to obtain the rendering context and its drwaing functions. ``getContext()`` takes one parameter: the type of context. For 2D graphics, you specify ``"2d"`` to get a ``CanvasRenderingContext2D``.

.. code-block:: javascript

    const canvas = document.querySelector("canvas");
    const context = canvas.getContext("2d");