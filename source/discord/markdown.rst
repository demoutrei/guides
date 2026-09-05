.. role:: strikethrough
    :class: strikethrough

.. role:: underline
    :class: underline


Markdown
========

Discord supports the following markdown.


Text Formatting
+++++++++++++++

+--------------------------------+---------------+---------------+
| *Italics*                      | ``*italics*`` | ``_italics_`` |
+--------------------------------+---------------+---------------+
| **Bold**                       | ``**bold**``                  |
+--------------------------------+-------------------------------+
| :underline:`Underline`         | ``__underline__``             |
+--------------------------------+-------------------------------+
| :strikethrough:`Strikethrough` | ``~~Strikethrough~~``         |
+--------------------------------+-------------------------------+
| Spoilers                       | ``||text||``                  |
+--------------------------------+-------------------------------+

.. admonition:: Formatting Combination
    :class: tip

    Text formatting can be combined together.


Organizational
^^^^^^^^^^^^^^


Header
~~~~~~

.. important::

    Don't forget to add a space between the leading heading character (``#``, ``##``, ``###``) and your text.

To create a header you just need to include a specific number of the hash/pound sign character (``#``). One pound sign for a big header, two for a smaller header, and three for an even smaller header as the first character(s) in a new line to make a header.

.. code:: text

    # Big header (h1)

    ## Smaller header (h2)

    ### Even smaller header (h3)


Subtext
~~~~~~~

To create a subtext is similar to a header, except instead of just a pound (``#``), you prefix it with a dash (``-#``).

.. code:: text

    -# This is a subtext.


Masked Links
~~~~~~~~~~~~

You can use masked links to make a text a clickable or pressable hyperlink.

.. code:: text

    [Your Text Here](https://example.com)


.. tip::

    You can enclose your link with angle brackets (``<>``) to suppress its embed.

    .. code:: text

        [Your Text Here](<https://example.com>)


Lists
~~~~~

.. important::

    Don't forget to add a space between the list bullet (``-``, ``*``, ``1.``, etc) and your text!

You can create a bulleted list using either a dash (``-``) or an asterisk (``\*``) in the beginning of each line.

.. code:: text

    - List of stuff
    - and things
    * and more things


.. tip::

    You can also indent your list by adding 2 spaces before the dash or asterisk at the beginning of each line.

    .. code:: text

        * List of stuff
          * and things
          - and more things


Code Blocks
+++++++++++

You can make your own code blocks by wrapping your text in backticks (`````).

.. code:: text

    `This is an inline code block.`


If you want to create a multi-line code block, wrap your text in three backticks (```````) on each ends.

.. code:: text

    ```This is a
    multiline code block.```


.. admonition:: Syntax Highlighting
    :class: tip

    You can integrate syntax highlighting to your code block by adding a language syntax after the first three backticks (```````), and the start of your text shall be in a new line.

    .. code:: text

        ```py
        print("Hello, World!")
        ```

    .. seealso::

        `Rebane's Discord Colored Text Generator`_


Block Quotes
++++++++++++

.. important::

    Don't forget to add a space between the leading ``>`` and your text!

To use a block quote, prefix a ending angle bracket (``>``) at the beginning of a line of text.

.. code:: text

    > Sample text 1
    Sample text 2
    Sample text 3

.. tip::

    To add multiple lines to a single block quote, prefix three ending angle brackets (``>>>``) before the first line.

    .. code:: text

        >>> Sample text 1
        Sample text 2
        Sample text 3


.. _Rebane's Discord Colored Text Generator: https://rebane2001.com/discord-colored-text-generator/