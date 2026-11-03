Animation and Interaction
=========================

Modern computer graphics is not limited to displaying static images, shapes, and objects. Graphics can also move, respond to user input, and change their appearance based on different events.

Two important concepts that make computer graphics more dynamic are **animation** and **interaction**.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Animation

        **Animation** is the process of creating the illusion of movement by displaying a sequence of images or changing the properties of graphical objects over time.

        In computer graphics, animation is commonly achieved by continuously updating the position, size, rotation, color, or other properties of an object.

        .. admonition:: Example
            :class: hint

            - A ball bouncing up and down.
            - A character walking across the screen.
            - A car moving along a road.
            - A logo rotating continuously.
            - A game character jumping when a button is pressed.

    .. grid-item-card:: Interaction

        **Interaction** refers to the ability of a computer graphics application to respond to actions performed by the user.

        Unlike static graphics, interactive graphics allow users to control or influence what happens on the screen.

        .. admonition:: Examples
            :class: hint

            - Clicking a button to change an object's color.
            - Moving the mouse to control an object.
            - Pressing keyboard keys to move a character.
            - Dragging an object from one location to another.
            - Clicking a shape to display information.

    .. grid-item-card:: Difference between Animation and Interaction

        .. grid:: 1 2 2 2
            :class-row: surface
            :gutter: 3

            .. grid-item-card:: Animation

                Creates movement over time.

                Can operate automatically.

                Uses time-based updates.

                .. admonition:: Example
                    :class: hint

                    A rotating circle.

            .. grid-item-card:: Interaction

                Responds to user actions.

                Usually requries user input.

                Uses events and input handling.

                .. admonition:: Example
                    :class: hint

                    Clicking a circle changes its color.


Types of Animation
++++++++++++++++++

There are several types of animation used in computer graphics and multimedia applications.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: 2D Animation

        2D animation involves creating movement using objects that exist in a two-dimensional environment.

        Objects are represented using:

        - **X-coordinate** -- horizontal position
        - **Y-coordinate** -- vertical position

        .. admonition:: Examples
            :class: hint

            - Cartoon animations.
            - Animated icons.
            - Moving objects in 2D games.
            - Animated advertisements.

    .. grid-item-card:: 3D Animation

        3D animation involves creating movement using objects with three dimensions:

        - **X-axis** -- horiznotal position
        - **Y-axis** -- vertical position
        - **Z-axis** -- depth
        
        Unlike 2D animation, 3D animation provides a sense of depth and volume.

        .. admonition:: Examples
            :class: hint

            - Animated movies
            - 3D video games
            - Architectural walkthroughs
            - Product demonstrations

    .. grid-item-card:: Frame-by-Frame Animation

        Frame-by-frame animation creates movement by displaying a sequence of individually created images. Each image represents a slightly different position or appearance of an object. Virtual reality environments.

    .. grid-item-card:: Keyframe Animation

        Keyframe animation defines important positions or states of an object at specific points in time.

        The computer generates the intermediate frames between the keyframes. THis process is called **tweening** or **in-betweening**.

        .. admonition:: Examples
            :class: hint

            - At 0 seconds: A ball is on the left.
            - At 2 seconds: A ball is at the center.
            - At 4 seconds: A ball is on the right.

        .. admonition:: Commonly Used In
            :class: tip

            - Adobe Animate
            - Blender
            - Adobe After Effects
            - CSS animations

    .. grid-item-card:: Motion Graphics

        Motion graphics involve animating text, shapes, icons, and graphical elements to communicate information or create visual effects.

        .. admonition:: Example
            :class: hint

            - Animated presentation titles
            - Logo animations
            - Animated infographics
            - Video introductions
            - Promotional advertisements


Principles of Animation
+++++++++++++++++++++++

The principles of animation help develoeprs create movements that appear natural, realistic, and visually appealing.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Squash and Stretch

        Squash and stretch give objects a sense of flexibility, weight, and movement.

        .. admonition:: Example
            :class: hint

            When a ball hits the ground, it becomes slightly flattened. When it moves upward, it stretches.

    .. grid-item-card:: Anticipation

        Anticipation prepares the viewer for an upcoming action.

        .. admonition:: Example
            :class: hint

            Before a character jumps, it bends it knees. This movement signals that a jump is about to happen.

    .. grid-item-card:: Timing

        Timing refers to the amount of time required to perform an action. It determines how fast or slow an object moves.

        .. admonition:: Examples
            :class: hint

            - A fast-moving ball may appear lightweight.
            - A slowly moving heavy object may appear to have more weight.

    .. grid-item-card:: Slow In and Slow Out

        Objects do not always move at a constant speed. **Slow in** means an object gradually accelerates from a stationary position. **Slow out** means an object gradually decelerates before stopping. This creates more natural movement.

    .. grid-item-card:: Follow Through and Overlapping Action

        **Follow through** refers to the continuation of movement after the main action has stopped.

        .. admonition:: Example
            :class: hint

            When a character stops running, its hair or clothing may continue moving briefly.

        **Overlapping action** occurs when different parts of an object move at different rates.

    .. grid-item-card:: Arc

        Most natural movmeents follow curved paths instead of perfectly straight lines.

        .. admonition:: Example
            :class: hint

            When a person throws a ball, the ball generally follows a curved trajectory.

    .. grid-item-card:: Exaggeration

        **Exaggeration** makes actions more notiveable to improve visual communication.

        .. admonition:: Example
            :class: hint

            A cartoon character may open its eyes extremely wide when surprised.


Animation Techniques in JavaScript
++++++++++++++++++++++++++++++++++

JavaScript allows developers to create animations directly in a web browser.

One of the most common technologies used for 2D animation is the HTML Canvas API.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: HTML Canvas

        HTML Canvas is an HTML element that provides a drwaing area where developers can create graphics using JavaScript.

        It can be used to draw lines, rectangles, circles, ellipses, images, text, and animated objects.

        .. admonition:: Example
            :class: hint

            .. tabs::

                .. code-tab:: html

                    <canvas id="myCanvas" width="600" height="400"></canvas>

            JavaScript can access the canvas using:

            .. tabs::

                .. code-tab:: javascript

                    const canvas = document.querySelector("#myCanvas");
                    const ctx = canvas.getContext("2d");

    .. grid-item-card:: The requestAnimationFrame() Method

        The ``requestAnimationFrame()`` method tells the browser to execute a function before the next screen repaint. It is commonly used to create smooth animations.

        .. admonition:: Example
            :class: hint

            .. tabs::

                .. code-tab:: javascript

                    function animate() {
                      // Animation code goes here
                      requestAnimationFrame(animate);
                    }

            **Explanation**:

            1. The ``animate()`` function contains the animation instructions.
            2. ``requestAnimationFrame(animate)`` schedules another execution of the function.
            3. The function repeatedly executes, producing continuous animation.

    .. grid-item-card:: Clearing the Canvas

        Before drawing the next animation frame, developers usually clear the previous frame.

        .. tabs::

            .. code-tab:: javascript

                ctx.clearRect(0, 0, canvas.width, canvas.height);

        This removes previously drawn content from the canvas. Without clearing the canvas, moving objects may leave visible trails.

    .. grid-item-card:: Updating Object Position

        To animate an object, its coordinates must change over time.

        .. admonition:: Example
            :class: hint

            .. tabs::

                .. code-tab:: javascript

                    let x = 50;

                    function animate() {
                      ctx.clearRect(0, 0, canvas.width, canvas.height);
                      
                      ctx.beginPath();
                      ctx.arc(x, 100, 25, 0, Math.PI * 2);
                      ctx.fillStyle = "blue";
                      ctx.fill();

                      x += 2;

                      requestAnimationFrame(animate);
                    }

                    animate();


User Interaction in JavaScript
++++++++++++++++++++++++++++++

JavaScript allows graphics applications to respond to user actions through events. An **event** is an action or occurence that the browser can detect.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Mouse Events

        Mouse events allow users to interact with graphical objects using a mouse.

        +----------------+-------------------------------------------+
        | Event          | Description                               |
        +================+===========================================+
        | ``click``      | Occurs when an element is clicked.        |
        +----------------+-------------------------------------------+
        | ``dblclick``   | Occurs when an element is double-clicked. |
        +----------------+-------------------------------------------+
        | ``mousemove``  | Occurs when the mouse moves.              |
        +----------------+-------------------------------------------+
        | ``mousedown``  | Occurs when a mouse button is pressed.    |
        +----------------+-------------------------------------------+
        | ``mouseup``    | Occurs when a mouse button is released.   |
        +----------------+-------------------------------------------+
        | ``mouseenter`` | Occurs when the mouse enters an element.  |
        +----------------+-------------------------------------------+
        | ``mouseleave`` | Occurs when the mouse leaves an element.  |
        +----------------+-------------------------------------------+

    .. grid-item-card:: Keyboard Events

        Keyboard events allow users to control objects using keyboard keys.

        +-------------+--------------------------------+
        | Event       | Description                    |
        +=============+================================+
        | ``keydown`` | Occurs when a key is pressed.  |
        +-------------+--------------------------------+
        | ``keyup``   | Occurs when a key is released. |
        +-------------+--------------------------------+

    .. grid-item-card:: Drag and Drop Interaction

        Drag and drop allows users to move graphical objects from one location to another.

        .. admonition:: Examples
            :class: hint

            - Moving shapes around a canvas.
            - Rearranging objects in a drawing application.
            - Moving game objects.
            - Organizing items in a visual interface.

    .. grid-item-card:: Interactive Buttons

        Buttons allow users to perform specific ations.

        .. admonition:: Example
            :class: hint

            .. tabs::

                .. code-tab:: html

                    <button onclick="changeColor();">Change Color</button>

                .. code-tab:: javascript

                    function changeColor() {
                      ctx.fillStyle = "red";
                    }


Combining Animation and Interaction
+++++++++++++++++++++++++++++++++++

One of the most important applications of animation and interaction is the development of interactive graphics and games.

Consider a simple game where a player controls a ball.

The application should have the following features:

- A ball is displayed on the canvas.
- The ball continuously moves horizontally.
- The user can control the ball using arrow keys.
- The ball changes color when clicked.
- The ball bounces when it reaches the canvas boundaries.

This example combines:

- Animation through continuous movement.
- Keyboard interaction through arrow keys.
- Mouse interaction through clicking.
- Boundary detection through conditional statements.
- Grpahics rendering through the Canvas API.