Graphics Programming
====================

**Graphics programming** is the process of writing computer instructions that generate, manipulate, and display visual content on a screen or another output device.

Unlike traditional programs that primarily process text and numerical data, graphics programs also control how visual elements appear, including their position, size, shape, color, and orientation.

.. admonition:: Example
    :class: hint

    A program that calculates the average grade of a student produces a numerical result. A graphics program can display that result inside a colore dbox, draw a bar chart of student grades, or create an interactive dashboard.

.. admonition:: Objectives
    :class: tip

    Graphics programming is commonly used to accomplish the following tasks:

    - **Generate visual objects**: Create shapes, diagrams, icons, charts, and illustrations.

    - **Control object appearance**: Set colors, line thickness, fill styles, and transparency where supported.

    - **Position objects**: Determine where graphical elements appear on the screen.

    - **Manipulate graphics**: Move, rotate, resize, or otherwise transform objects.

    - **Create interactive applications**: Respond to mouse clicks, keyboard input, and other user actions.

    - **Present information visually**: Convert numerical or textual dat ainto charts, diagrams, and visual representations.


Applications
++++++++++++

.. grid:: 1 2 3 3
    :gutter: 3

    .. grid-item-card:: Game Development

        Drawing characters, obstacles, and backgrounds.

    .. grid-item-card:: User Interface Development

        Creating buttons, menus, icons, and windows.

    .. grid-item-card:: Data Visualization

        Displaying bar charts, line graphs, and pie charts.

    .. grid-item-card:: Computer-Aided Design (CAD)

        Drawing floor plans and engineering diagrams.

    .. grid-item-card:: Educational Software

        Creating interactive geometry lessons.

    .. grid-item-card:: Digital Illustration

        Producing shapes, patterns, and vector artwork.

    .. grid-item-card:: Simulation

        Displaying objects and movement in a simulated environment.


How It Works
++++++++++++

A basic graphics program follows a sequence of operations:

1. Define the objects.
    Choose the shapes, dimensions, and colors.

2. Specify coordinates.
    Determine where each object will appear.

3. Execute drawing commands.
    Use graphics functions to create the objects.

4. Render the image.
    The graphics system displays the final result.

In more advanced systems, graphics processing also involves clipping, transformations, rasterization, and rendering pipelines.


Languages and Libraries
+++++++++++++++++++++++

A programming language provides the instructions, while a graphics library or framework provides specialized functions for drwaing and manipulating visual objects.

.. admonition:: Example
    :class: hint

    C++ can be used for graphics programming, but a graphics library is generally needed to simplify drawing operations.

Some commonly used technologies include:

- **SFML**: A C++ multimedia library suitable for 2D graphics, games, and interactive applications.

- **SDL**: A cross-platform library for multiemedia and graphics applications.

- **OpenGL**: A graphics API used to specify rendering operations, including 2D graphics implemented through graphics primitives and shaders.

- **HTML Canvas**: A browser-based drawing interface that uses JavaScript to draw shapes and images.

- **p5.js**: A JavaScript library designed for creating coding and visual experimentation.


The 2D Coordinate System
++++++++++++++++++++++++

A two-dimensional coordinate system identifies the position of an object using two values:

- **X-coordinate**: Specifies the horizontal position.

- **Y-coordinate**: Specifies the vertical position.

A point is commonly represented as ``(x, y)``.

.. admonition:: Example
    :class: hint

    The coordinate ``(100, 50)`` identifies a position ``100`` unites horizontally and ``50`` units vertically from the coordiante system's origin, assuming a conventional screen-coordinate system.


Cartesian Coordiantes Versus Screen Coordinates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In mathematics, the Cartesian coordinate system normally places the origin at the center or another reference point, with positive ``y``-values extending upward.

Most computer screens use a different convention:

- The origin ``(0, 0)`` is usually at the upper-left corner.

- The X-coordinate increases toward the right.

- The Y-coordinate increases toward the bottom.

.. admonition:: Example
    :class: hint

    Imagine drawing a circle on an 800x600 pixel canvas.

    - Position A: ``(100, 100)``---near the upper-left corner.

    - Position B: ``(400, 300)``---near the center.

    - Position C: ``(700, 500)``---near the lower-right corner.

    The circle's exact location depends on how the graphics library interprets its coordinates. Some drawing functions use the center of the circle, while others use the top-left corner of its bounding rectangle.

.. admonition:: Why Coordinates Matter
    :class: tip

    Coordinates allow programmers to:

    - Place objects accurately;
    - Align multiple shapes;
    - Control spacing and margins;
    - Create symmetrical designs;
    - Animate objects by changing their coordinates;
    - Detect whether a mouse click occurs inside an object


2D Primitives
+++++++++++++

Two-dimensional primitives are the basic geometric elements used to construct graphical images. They serve as the building blocks of more complicated drawings.

A primitive may represent a single point, a straight line, a closed shape, or a collection of connected line segments.

.. admonition:: Example
    :class: hint

    A house can be drawn using a rectangle for the walls, a triangle for the roof, smaller rectangles for the door and windows, and lines for additional details.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Point

        A point identifies a specific location in a coordinate system. It has a position but no inherent width or height in the mathematical model. In computer graphics, a point is commonly represented by a pixel or a small visible mark.

        .. admonition:: Characteristics
            :class: tip

            Defined by an X-coordinate and a Y-coordinate.

            Used to mark locations or vertices.

            Can serve as a reference for other shapes.

            May be displayed with a particular color or size.

    .. grid-item-card:: Line

        A line primitive connects two points. In computer graphics, a line segment is commonly specified using a starting point and an ending point.

        .. admonition:: Characteristics
            :class: tip

            Defined by two endpoints.

            Can have a specified color.

            May support line thickness or stroke width.

            Used for borders, grids, diagrams, and geometric outlines.

        .. admonition:: Example Applications
            :class: hint

            Drawing the edges of a triangle.

            Creating chart axes.

            Connecting nodes in a network diagram.

            Drawing road segments in a map.

    .. grid-item-card:: Circle

        A circle is a two-dimensional shape whose points are all the same distance from a central point.

        A circle is defined by:

        - Center coordinates ``(cx, cy)``.
        - Radius ``r``.
        - Optional outline and fill properties.

        A circle's center and radius determine its geometry, while its outline and fill determine its appearance.

        .. admonition:: Applications
            :class: tip

            Buttons and icons.

            Wheels and clock faces.

            Game characters and targets.

            Balls and other round objects.

            Nodes in flowcharts and network diagrams.

    .. grid-item-card:: Rectangle

        A rectangle is a four-sided polygon with four right angles. In a typical 2D drawing API, a rectangle can be defined using its position, width, and height.

        The usual parameters are:

        - X-coordinate of the upper-left corner.
        - Y-coordinate of the upper-left corner.
        - Width.
        - Height.

        .. admonition:: Applications
            :class: tip

            Window and panel layouts.

            Buttons and menus.

            Buildings and floor plans.

            Game platforms and obstacles.

            Bar charts and tables.

    .. grid-item-card:: Ellipse

        An ellipse resembles a circle that has been stretched horizontally, vertically, or in both directions.

        It is defined by a center point and two radii:

        - Horizontal radius ``rx``
        - Vertical radius ``ry``

        When both radii are equal, the ellipse becomes a circle.

        .. admonition:: Applications
            :class: tip

            Eyes and facial features.

            Oval logos.

            Shadows and highlights.

            Planetary orbits in simplified diagrams.

            Decorative interface elements.

        In many graphics libraries, an ellipse is drawn by specifiying the bounding rectangle that contains it.

    .. grid-item-card:: Polygon

        A polygon is a closed shape formed by connecting three or more straight line segments.

        Common polygons include:

        - Triangle---three sides.
        - Quadrilateral---four sides.
        - Pentagon---five sides.
        - Hexagon---six sides.
        - Octagon---eight sides.

        .. admonition:: Applications
            :class: tip

            Roofs and building outlines.

            Icons and logos.

            Map regions.

            Game objects.

            Irregular geometric figures.

        Polygons are particularly important in computer graphics because more complex shapes can be approximated or constructed using many connected polygonal surfaces.


Fundamental Concepts
++++++++++++++++++++


Drawing Attributes
^^^^^^^^^^^^^^^^^^

Defining a shape determines its geometry, but drawing attributes determine how the shape looks.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Color

        Color can be used to distinguish objects, highlight important information, and improve visual communication. Many graphics systems support RGB color values, which combine red, green, and blue components.

        .. admonition:: Example
            :class: hint

            In a common 8-bit RGB system:

            - Red: ``(255, 0, 0)``
            - Green: ``(0, 255, 0)``
            - Blue: ``(0, 0, 255)``
            - White: ``(255, 255, 255)``
            - Black: ``(0, 0, 0)``

        Other graphics systems may use normalized RGB values between ``0`` and ``1`` or different color representations.

    .. grid-item-card:: Fill and Outline

        A shape's fill is the color or pattern applied to its interior. Its outline is the visible boundary around it.

        .. admonition:: Example
            :class: hint

            A rectangle can have a blue fill and a black outline. Some APIs treat filled shapes and outline shapes as separate drawing operations.

    .. grid-item-card:: Line Thickness

        Line thickness determines how wide a lien or shape outline appears. Thicker lines may emphasize important objects, while thinner lines are often used for details and grids.

    .. grid-item-card:: Transparency

        Transparency controls how much of the background can be seen through an object. It is often represented by an alpha component in addition to RGB.


The Graphics Canvas
+++++++++++++++++++

A **graphics canvas** is the area where graphical objects are displayed. It can represent a window, an image, a web canvas, or another drawable surface. A canvas has dimensions, commonly measured in pixels.

When creating a graphical scene, the programmer should consider:

- Canvas width and height.
- Object positions and dimensions.
- Available drawing boundaries.
- Background color.
- Object overlap and drawing order.


Drawing Order
^^^^^^^^^^^^^

In many 2D systems, objects drawn later can cover objects drawn earlier.

.. admonition:: Example
    :class: hint

    If a red circle is drawn first and a blue rectangle is drawn over it, the rectangle may hide part of the circle. This is commonly called the **painter's-order principle**.

Drawing order is important when building layered scenes, icons, interface components, and simple animations.