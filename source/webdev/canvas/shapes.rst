Shapes
======


Circle
++++++

The ``arc()`` method is used to define a circle.

**Parameters**:

- ``x`` -- The x-coordinate of the arc's center.
- ``y`` -- The y-coordinate of the arc's center.
- ``radius`` -- The radius of the arc.
- ``startAngle`` -- The angle where the arc starts in radians.
- ``endAngle`` -- The angle where the arc ends in radians.
- ``counterClockwise`` -- A boolean value. If set to ``true``, it draws the arc counter-clockwise between the stard and end angles. The default is ``false`` (clockwise).

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-1" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-1").getContext("2d");
              context.beginPath();
              context.arc(95, 50, 40, 0, 2 * Math.PI);
              context.stroke();
            </script>

    .. tab:: Code

        .. code-block:: html

            <canvas id="canvas" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              const context = document.querySelector("#canvas").getContext("2d");
              context.beginPath();
              context.arc(95, 50, 40, 0, 2 * Math.PI);
              context.stroke();
            </script>


Ellipse
+++++++

The ``ellipse()`` method of the Canvas 2D API adds an elliptical arc to the current sub-path.

**Parameters**:

- ``x`` -- The x-acis coordinate of the ellipse's center.
- ``y`` -- The y-axis coordinate of the ellipse's center.
- ``radiusX`` -- The ellipse's major-axis radius. Must be non-negative.
- ``radiusY`` -- The ellipse's minor-axis radius. Must be non-negative.
- ``rotation`` -- The rotation of the ellipse, expressed in radians.
- ``startAngle`` -- The eccentric angle at which the ellipse starts, measured clockwise from the positive x-axis and expressed in radians.
- ``endAngle`` -- The eccentric angle at which the ellipse ends, measured clockwise from the positive x-axis and expressed in radians.
- ``counterclockwise`` (optional) -- An optional boolean value which, if ``true``, dras the ellipse counterclockwise. The default value is ``false`` (clockwise).

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-4" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-4").getContext("2d");
              context.beginPath();
              context.ellipse(100, 100, 50, 75, 0, 0, 2 * Math.PI);
              context.stroke();
            </script>

    .. code-tab:: html

        <canvas id="canvas" width="300" height="300" style="background-color: white;"></canvas>
        <script>
          const context = document.querySelector("#canvas").getContext("2d");
          context.beginPath();
          context.ellipse(100, 100, 50, 75, ,0, 0, 2 * Math.PI);
          context.stroke();
        </script>


Line
++++

To draw a line in canvas, we use the following methods:

- ``beginPath()``---Declares that we are about to draw a new path.
- ``moveTo(x, y)``---Sets the start-point of the line in the canvas.
- ``lineTo(x, y)``--Sets the end-point of the line in the canvas.
- ``stroke()``---Draws the line. The default stroke color is black.

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-3" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-3").getContext("2d");
              context.beginPath();
              context.moveTo(0, 0);
              context.lineTo(300, 300);
              context.stroke();
            </script>

    .. tab:: Code

        .. code-block:: html

            <canvas id="canvas" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              const context = document.querySelector("#canvas").getContext("2d");
              context.beginPath();
              context.moveTo(0, 0);
              context.lineTo(300, 300);
              context.stroke();
            </script>


Rectangle
+++++++++

There are three functions that draw rectangles on canvas:

``fillRect()``---Draws a filled rectangle.

``strokeRect()``---Draws a rectangular outline.

``clearRect()``---Clears the specified rectangular area, making it fully transparent.

**Parameters**:

- ``x`` -- X-coordinate
- ``y`` -- Y-coordinate
- ``width`` -- Width of the rectangle.
- ``height`` -- Height of the rectangle.

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-0" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-0").getContext("2d");
              context.fillRect(25, 25, 100, 100);
              context.clearRect(45, 45, 60, 60);
              context.strokeRect(50, 50, 50, 50);
            </script>

    .. tab:: Code

        .. code-block:: html

            <canvas id="canvas" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              const context = document.querySelector("#canvas").getContext("2d");
              context.fillRect(25, 25, 100, 100);
              context.clearRect(45, 45, 60, 60);
              context.strokeRect(50, 50, 50, 50);
            </script>


Triangle
++++++++

.. tabs::

    .. tab:: Output

        .. raw:: html

            <canvas id="canvas-2" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              context = document.querySelector("#canvas-2").getContext("2d");
              context.beginPath();
              context.moveTo(75, 50);
              context.lineTo(100, 75);
              context.lineTo(100, 25);
              context.fill();
            </script>

    .. tab:: Code

        .. code-block:: html

            <canvas id="canvas" width="300" height="300" style="background-color: white;"></canvas>
            <script>
              const context = document.querySelector("#canvas").getContext("2d");
              context.beginPath();
              context.moveTo(75, 50);
              context.lineTo(100, 75);
              context.lineTo(100, 25);
              context.fill();
            </script>