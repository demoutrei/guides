Styling
=======


Fill Style
++++++++++

``CanvasRenderingContext2D.fillStyle`` property is set to change the color, gradient, or pattern to use inside shapes. The default style is ``black``.

The value must either be of the following:

- A string parsed as CSS color value.
- A ``CanvasGradient`` object (a linear or radial gradient).
- A ``CanvasPattern`` object (a repeating image).

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-0" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-0").getContext("2d");
              context.fillStyle = "blue";
              context.fillRect(50, 50, 200, 200);
            </script>

    .. code-tab:: javascript

        const context = document.querySelector("#canvas").getContext("2d");
        context.fillStyle = "blue";
        context.fillRect(50, 50, 200, 200);


Stroke Style
++++++++++++

``CanvasRenderingContext2D.strokeStyle`` property specifies the color, gradient, or pattern to use for the strokes (outlines) around shapes. The default is ``black``.

The value must either be of the following:

- A string parsed as CSS color value.
- A ``CanvasGradient`` object (a linear or radial gradient).
- A ``CanvasPattern`` object (a repeating image).

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-1" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-1").getContext("2d");
              context.strokeStyle = "blue";
              context.strokeRect(50, 50, 200, 200);
            </script>

    .. code-tab:: javascript

        const context = document.querySelector("#canvas").getContext("2d");
        context.strokeStyle = "blue";
        context.strokeRect(50, 50, 200, 200);


Line Width
++++++++++

``CanvasRenderingContext2D.lineWidth`` property sets the thickness of lines.

The value must be a number specifying the line width, in coordinate space units. Zero, negative, ``Infinity``, and ``NaN`` values are ignored. Default is ``1.0``.

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-2" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-2").getContext("2d");
              context.lineWidth = 10;
              context.strokeRect(50, 50, 200, 200);
            </script>

    .. code-tab:: javascript

        const context = document.querySelector("#canvas").getContext("2d");
        context.lineWidth = 10;
        context.strokeRect(50, 50, 200, 200);