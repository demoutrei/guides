Getting Started
===============

.. admonition:: Prerequisites
    :class: important

    .. tabs::

        .. tab:: Python

            1. A `Cloudflare`_ account.
            
            2. `Python`_, `uv`_, and `Node.JS`_ installed in your machine.


Setup
+++++

Navigate to the parent directory of where your project directory will reside. In the terminal, set up your development environment:

.. tabs::

    .. tab:: Python

        .. code-block:: bash

            uvx --from workers-py pywrangler init

        This will create a ``pyproject.toml`` file with ``workers-py`` as a development dependency, and ``pywrangler init`` will create a wrangler config file.


Deploy Worker to Cloudflare
+++++++++++++++++++++++++++

.. tabs::

    .. tab:: Python

        .. admonition:: Run Worker Locally
            :class: hint

            To run the worker locally, run ``pywrangler`` with:

            .. code-block:: bash

                uv run pywrangler dev

        To deploy a Python Worker to Cloudflare, run ``pywrangler deploy``:

        .. code-block:: bash

            uv run pywrangler deploy

        This will create and deploy a Cloudflare Worker in your logged in Cloudflare account. Navigate to your **Workers & Pages** page in your Cloudflare dashboard, and a new Worker is added, named exactly the same as what you named your local project. You can use the worker domain address assigned to it, or connect a domain or subdomain of your own.


.. _Cloudflare: https://cloudflare.com/
.. _Node.JS: https://nodejs.org/en
.. _Python: https://www.python.org/downloads/
.. _uv: https://docs.astral.sh/uv/#installation