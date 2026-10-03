Foundations of Graphics and Visual Computing
============================================


Applications of Computer Graphics
+++++++++++++++++++++++++++++++++


What is Computer Graphics?
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Computer graphics** is the field of computing concerned with creating, manipulating, storing, and displaying visual information using computers.

Computer graphics allows computers to represent information using:

- Images
- Drawings
- Shapes
- Charts
- Diagrams
- Animations
- 3D models
- Simulations
- Visual effects


.. admonition:: Example
    :class: hint

    When a student creates a digital drawing using a graphics application, the computer is processing graphical information.


Major Applications
^^^^^^^^^^^^^^^^^^


.. grid:: 1 2 2 2
    :gutter: 3


    .. grid-item-card:: Entertainment

        Computer graphics is widely used in:

        - Video games
        - Movies
        - Animation
        - Visual effects
        - 3D characters
        - Virtual environments

        .. admonition:: Example
          :class: hint

          Modern games use real-time graphics to render characters, environments, lighting, shadows, and effects.


    .. grid-item-card:: Computer-Aided Design (CAD)

        CAD applications allow engineers, architects, and designers to create accurate digital models.

        - Building designs
        - Machine parts
        - Electrical layouts
        - Product designs
        - 3D models


    .. grid-item-card:: Education

        Graphics can make learning materials easier to understand.

        - Interactive diagrams
        - Educational animations
        - Simulations
        - 3D models
        - Graphs and charts


    .. grid-item-card:: Scientific Visualization

        Scientists use graphics to represent large or complex datasets.

        - Weather maps
        - Molecular structures
        - Astronomical images
        - Medical data
        - Climate models


    .. grid-item-card:: Business

        - Presentations
        - Reports
        - Dashboards
        - Data visualization
        - Marketing materials
        - Product demonstrations


    .. grid-item-card:: Medicine

        - Medical imaging
        - 3D anatomical models
        - Surgical planning
        - Medical simulations
        - Visualization of organs and tissues


    .. grid-item-card:: User Interfaces

        Graphical user interfaces (GUIs) use graphical elements such as:

        - Windows
        - Icons
        - Buttons
        - Menus
        - Dialog boxes

        .. admonition:: Example
            :class: hint

            Desktop operating systems, mobile applications, and web applications.


Graphics Systems
++++++++++++++++


What is a Graphics System?
^^^^^^^^^^^^^^^^^^^^^^^^^^

A **graphics system** is a combination of hardware and software used to create, process, store, and display graphical information.

A basic graphics system can be viewed as: **Input → Processing → Storage → Output**


Major Components
^^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :gutter: 3


    .. grid-item-card:: Input Devices

        Allows users to provide graphical information or instructions.


        .. admonition:: Example
            :class: hint

            - Mouse
            - Keyboard
            - Graphics tablet
            - Touchscreen
            - Scanner
            - Digital camera
            - 3D scanner


    .. grid-item-card:: Processing Unit

        The computer processes graphical information using components such as CPU, GPU, and RAM.

        The **CPU** performs general-purpose processing, while the **GPU** is designed to efficiently perform many graphics-related calculations.


    .. grid-item-card:: Graphics Software

        Graphics software provides tools for creating and manipulating graphical information.


        .. admonition:: Example
            :class: hint

            - Image editors
            - 3D modeling software
            - Animation software
            - CAD software
            - Game engines
            - Visualization software


    .. grid-item-card:: Display Devices

        Graphics must eventually be presented to the user.

        
        .. admonition:: Example
            :class: hint

            - Monitor
            - Projector
            - Smartphone display
            - Tablet display
            - VR headset


    .. grid-item-card:: Storage

        .. admonition:: Example
            :class: hint

            - Hard drives
            - SSDs
            - USB drives
            - Memory cards
            - Cloud storage


Pixels and Resolution
+++++++++++++++++++++


What is a Pixel?
^^^^^^^^^^^^^^^^

A **pixel**, short for **picture element**, is one of the smallest individual units of a digital raster image. An image can be represented as a grid of pixels.

A pixel can contain information such as **color**, **brightness**, and **transparency**.


Pixel Color
^^^^^^^^^^^

Digital images commonly represent colors using the **RGB color model**:

- **R** -- Red
- **G** -- Green
- **B** -- Blue

Different combinations of these values can produce many colors.


.. admonition:: Example
    :class: hint

    RGB(255, 0, 0) → Red
    RGB(0, 255, 0) → Green
    RGB(0, 0, 255) → Blue
    RGB(255, 255, 255) → White
    RGB(0, 0, 0) → Black


What is Resolution?
^^^^^^^^^^^^^^^^^^^

**Resolution** refers to the number of pixels used to represent an image or display.

A display resolution of **1920 x 1080** means: 1920 pixels horizontally, and 1080 pixels vertically.

Total pixels: **1920, 1080 = 2,073,600 pixels**

This is commonly called **1080p**.


Resolution and Image Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally, a higher pixel count can provide more detail, but image quality also depends on other factors such as:

- Pixel density
- Image source
- Compression
- Display quality
- Viewing distance


Pixel Density
^^^^^^^^^^^^^

**Pixel density** describes how many pixels are packed into a physical area of a display. It is commonly expressed in **PPI** (pixels per inch).

A higher PPI generally allows finer details to be displayed.


Raster vs. Vector Graphics
++++++++++++++++++++++++++

One of the fundamental distinctions in computer graphics is between **raster** and **vector graphics**.


Raster Graphics
^^^^^^^^^^^^^^^

A **raster image** represents an image using a grid of pixels.

Common raster formats include JPEG/JPG, PNG, GIF, BPM, and TIFF.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Advantages

        - Excellent for photographs
        - Can represent complex colors
        - Suitable for detailed images

    .. grid-item-card:: Disasdvantages

        - Enlarging the image can cause pixelation
        - File size can become large
        - Quality depends on resolution

.. admonition:: Example
    :class: hint

    - Photographs
    - Digital paintings
    - Screenshots
    - Scanned images

Vector Graphics
^^^^^^^^^^^^^^^

A **vector image** represents graphics using mathematical descriptions of shapes.

Instead of storing every pixel, a vector graphic can be described using points, lines, curves, shapes, and mathematical equations.

Common vector formats include SVG, AI, EPS, and PDF.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Advantages

        - Can be resized without losing sharpness
        - Suitable for logogs and illustrations
        - Objects can be individually edited
        - Often efficient for simple graphics

    .. grid-item-card:: Disadvantages

        - Not ideal for realistic photographs
        - Complex illustrations can become computationally demanding

.. admonition:: Example
    :class: hint

    - Logos
    - Icons
    - Diagrams
    - Technical drawings
    - Typography

Graphics Pipeline
+++++++++++++++++

What is a Graphics Pipeline?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **graphics pipeline** is a sequence of processing stages through which graphical data passes before being displayed on a screen.

A simplified graphics pipeline can be represented as:

3D model / input data → Modeling transformation → Viewing transformation → Projection → Clipping → Rasterization → Fragment / Pixel processing → Frame buffer → Display

The exact pipeline varies depending on the graphics system and API, but the general idea is that complex graphical data is progessively transformed into pixels that can be displayed.

Modeling Transformation
^^^^^^^^^^^^^^^^^^^^^^^

Objects are positioned, rotated, and scaled within a scene.

.. admonition:: Example
    :class: hint

    A 3D object may be moved to a different position, rotated, enlarged, or reduced.

Viewing Transformation
^^^^^^^^^^^^^^^^^^^^^^

The scene is transformed according to the position and orientation of the camera or viewer.

.. admonition:: Example
    :class: hint

    In a 3D game, the player's camera determines what part of the game world is visible.

Projection
^^^^^^^^^^

Three-dimensional objects need to be represented on a two-dimensional display.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Perspective Projection

        Objects farther away appear smaller. This resembles how humans normally perceive the world.

    .. grid-item-card:: Orthographic Projection

        Objects maintain their relative size regardless of distance. This is often useful for technical drawings and certain visualization applications.

Clipping
^^^^^^^^

Objects or parts of objects outside the visible area are removed or ignored.

.. admonition:: Example
    :class: hint

    If an object is completely outside the camera's view, there is no need to render it.

Rasterization
^^^^^^^^^^^^^

Converts geometric information into fragments/pixels that can eventually be displayed.

.. admonition:: Example
    :class: hint

    Vector / 3D Shape → Rasterization → Pixel Representation

This is a crucial stage in real-time computer graphics.

Frame Buffer
^^^^^^^^^^^^

The **frame buffer** stores information about the image that is going to be displayed. It contains the graphical information corresponding to the current frame. The display system uses this information to produce the visible image.

Areas of Visual Computing
+++++++++++++++++++++++++

What is Visual Computing?
^^^^^^^^^^^^^^^^^^^^^^^^^

**Visual computing** is a broader field involving the processing, analysis, generation, and understanding of visual information using computers.

It combines areas such as computer graphics, computer vision, image processing, visualization, animation, virtual reality, and augmented reality.

Computer Graphics
^^^^^^^^^^^^^^^^^

Computer graphics focuses primarily on **generating visual content**.

.. admonition:: Example
    :class: hint

    - 3D models
    - Games
    - Animation
    - Digital art
    - Simulations

Computer Vision
^^^^^^^^^^^^^^^

Computer vision focuses on enabling computers to interpret and understand images or videos.

.. admonition:: Example
    :class: hint

    - Object detection
    - Face detection
    - Image classification
    - Motion tracking
    - Medical image analysis

Image Processing
^^^^^^^^^^^^^^^^

Image processing involves manipulating or improving digital images.

.. admonition:: Example
    :class: hint

    - Brightness adjustment
    - Contrast enhancement
    - Noice reduction
    - Sharpening
    - Image resizing
    - Filtering

Data Visualization
^^^^^^^^^^^^^^^^^^

Data visualization represents information graphically to make patterns and relationships easier to understand.

.. admonition:: Example
    :class: hint

    - Bar charts
    - Line graphs
    - Pie charts
    - Heat maps
    - Interactive dashboards

Animation
^^^^^^^^^

Animation involves creating the appearance of movement by displaying a sequence of images or changing graphical objets over time.

.. admonition:: Example
    :class: hint

    - 2D animation
    - 3D animation
    - Character animation
    - Motion graphics

Virtual Reality
^^^^^^^^^^^^^^^

**Virtual reality** creates an immersive computer-generated environment. Users may interact with the environment through devices such sa VR headsets, motion controllers, and sensors.

Augmented Reality
^^^^^^^^^^^^^^^^^

**Augmented reality** adds computer-generated information or objects to the user's view of the real world.

.. admonition:: Example
    :class: hint

    An AR application may display a virtual object while the user is looking at a real environment through a camera.