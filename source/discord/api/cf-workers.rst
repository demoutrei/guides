:description: Learn how to integrate HTTP-interaction (serverless) Discord application with Cloudflare's Workers.


Cloudflare Workers
==================

This guidepage walks through the steps on how to integrate your HTTP-interaction (serverless) Discord application with Cloudflare's Workers.


Prerequisites
+++++++++++++

Before we proceed with the steps, there are prerequisites to prepare:


.. tabs::

    .. tab:: Python

        1. A `Cloudflare`_ and `Discord`_ account, and a Discord application and its public key (can be found in the **General Information** tab of your application in the Developer Portal).

        2. `Python installed <https://www.python.org/downloads/>`_ in your device/machine.

        3. `uv`_ and `Node.JS`_ are installed.


.. seealso::

    `How Do I Create an Application?`_


Setup
+++++


Navigate to the parent directory of where your project directory will reside. In the terminal, set up your development environment:


.. tabs::

    .. tab:: Python

        .. code-block:: bash

            uvx --from workers-py pywrangler init


        This will create a ``pyproject.toml`` file with ``workers-py`` as a development dependency, and ``pywrangler init`` will create a wrangler config file. When initializing a new Python Worker project and prompted to select a template, it's safe to select the ``Hello World`` template and ``Workers only`` template for now.

        Lastly, navigate to your project directory.

        Install the ``cryptography`` package for later:


        .. code-block:: bash

            uv add cryptography==47.0.0


        .. important::

            ``workers-py`` currently only supports version ``47.0.0`` of the ``cryptography``.

            Utilizing the ``pynacl`` package cannot be done as well, for the reason that libsodium internally uses ``eval``, which is currently disabled in workers for security purposes; this cannot be resolved right now unless libsodium drops EM_ASM and replace it to something else.


            .. admonition:: Source
                :class: seealso

                `GitHub issue #271 response <https://github.com/cloudflare/workers-py/issues/271#issuecomment-5771459989>`_

        
        Copy your Discord application's public key and paste it in to your ``wrangler.jsonc`` file within the ``"vars"`` key.


        .. code-block:: json

            {
              "vars": {
                "APPLICATION_PUBLIC_KEY": "paste your public key here"
              }
            }


Configuring Interactions Endpoint URL
+++++++++++++++++++++++++++++++++++++

An **Interactions Endpoint URL** is a public endpoint for your app where Discord can send your app HTTP-based interactions. If your app is using Gateway-based interactions, you don't need to configure an Interactions Endpoint URL.

Before you can add your Interactions Endpoint URL to your app, your endpoint must be prepared for two things ahead of time:

1. Validate security-related request headers (``X-Signature-Ed25519`` and ``X-Signature-Timestamp``).

2. Acknowledging ``PING`` requests from Discord.


Validating Security Request Headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To receive interactions via HTTP, there are some security steps you **must** take before your app is eligible to receive requests.

Each interaction is sent with the following headers:

- ``X-Signature-Ed25519`` as a signature

- ``X-Signature-Timestamp`` as a timestamp

Using your favorite security library, you **must validate the request each time you receive an interaction**. If the signature fails validation, your app should respond with a ``401`` error code.


.. tabs::

    .. code-tab:: python

        from cryptography.exceptions import InvalidSignature
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
        from workers import Response, WorkerEntryPoint
        import json


        class Default(WorkerEntryPoint):
          async def fetch(self, request):
            if request.method != "POST":
              return Response("Method Not Allowed", status = 405)
            body = await request.text()
            signature = request.headers["X-Signature-Ed25519"]
            timestamp = request.headers["X-Signature-Timestamp"]
            try:
              verify_key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(self.env.APPLICATION_PUBLIC_KEY))
              verify_key.verify(bytes.fromhex(signature), f"{timestamp}{body}".encode())
            except InvalidSignature:
              return Response("Invalid request signature", status = 401)


Acknowledging PING Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When adding your Interactions Endpoint URL, Discord will send a ``POST`` request with a ``PING`` payload with a ``type: 1`` to your endpoint. Your app is expected to acknowledge the request by returning a ``200`` response with a ``PONG`` payload (which has the same ``type: 1``).


.. tabs::

    .. code-tab:: python

        class Default(WorkerEntryPoint):
          async def fetch(self, request):
            # ...
            data = json.loads(body)
            if data["type"] == 1:
              return Response.json(
                { "type": 1 },
                headers = {
                  "Content-Type": "application/json"
                },
                status = 200
              )


Deploy Worker to Cloudflare
^^^^^^^^^^^^^^^^^^^^^^^^^^^


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


This will create and deploy a Cloudflare Worker in your logged in Cloudflare account. Navigate to your **Workers & Pages** page in your Cloudflare dashboard, and a new Worker is added, named exactly the same as what you named your local project. You can use the worker domain address assigned to it, or connect a domain or subdomain of your own. This domain address is what you'll be using for adding an Interactions Endpoint URL.


Adding an Interactions Endpoint URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After you have public endpoint to use as your app's Interactions Endpoint URL, you can add it to your app by going to your app's settings.

On the **General Information** tab of your Discord application, look for the **Interactive Endpoint URL** field. Paste your public URL that is set up to acknowledge ``PING`` messages and correctly handles security-related signature headers.


-----


.. admonition:: Sources
    :class: seealso

    `Interactions Overview - Documentation - Discord`_

    `Write Cloudflare Workers in Python - Cloudflare Workers docs`_


.. _Cloudflare: https://cloudflare.com
.. _Discord: https://discord.com
.. _How Do I Create an Application?: ./faq#how-do-i-create-an-application
.. _Interactions Overview - Documentation - Discord: https://docs.discord.com/developers/interactions/overview#validating-security-headers
.. _Node.JS: https://nodejs.org/en
.. _uv: https://docs.astral.sh/uv/#installation
.. _Write Cloudflare Workers in Python - Cloudflare Workers docs: https://developers.cloudflare.com/workers/languages/python/