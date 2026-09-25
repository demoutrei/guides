:description: Discord utilizes a subset of markdown for rendering message content on its clients, while also adding some functionality to enable things like mentioning users and channels.


Message Formatting
==================

Discord utilizes a subset of `markdown <./markdown>`_ for rendering message content on its clients, while also adding some functionality to enable things like mentioning users and channels.


Formats
+++++++

+-----------------------------------------------+--------------------------------------------+
| Type                                          | Structure                                  |
+===============================================+============================================+
| User                                          | ``<@USER_ID>``                             |
+-----------------------------------------------+--------------------------------------------+
| Channel                                       | ``<#CHANNEL_ID>``                          |
+-----------------------------------------------+--------------------------------------------+
| Role                                          | ``<@&ROLE_ID>``                            |
+-----------------------------------------------+--------------------------------------------+
| Game profile                                  | ``<@$GAME_ID>``                            |
+-----------------------------------------------+--------------------------------------------+
| Slash command                                 | ``</NAME:COMMAND_ID>``                     |
+-----------------------------------------------+--------------------------------------------+
| Slash command with subcommand                 | ``</NAME SUBCOMMAND:ID>``                  |
+-----------------------------------------------+--------------------------------------------+
| Slash command with subcommand group           | ``</NAME SUBCOMMAND_GROUP SUBCOMMAND:ID>`` |
+-----------------------------------------------+--------------------------------------------+
| Standard emoji                                | Unicode characters                         |
+-----------------------------------------------+--------------------------------------------+
| Custom emoji                                  | ``<:NAME:ID>``                             |
+-----------------------------------------------+--------------------------------------------+
| Animated custom emoji                         | ``<a:NAME:ID>``                            |
+-----------------------------------------------+--------------------------------------------+
| Unix timestamp                                | ``<t:TIMESTAMP>``                          |
+-----------------------------------------------+--------------------------------------------+
| `Styled unix timestamp <#timestamp_styles>`_  | ``<t:TIMESTAMP:STYLE>``                    |
+-----------------------------------------------+--------------------------------------------+
| `Guild navigation <#guild-navigation-types>`_ | ``<id:TYPE>``                              |
+-----------------------------------------------+--------------------------------------------+

Using the markdown for users or roles will mention the target(s), and notify them depending on the sender's permissions. Standard emoji are currently rendered using `Twemoji`_ for Desktop and Android while iOS and devices use Apple's native emoji set.

Timestamps are expressed in **seconds** and display the given timestamp in the user's timezone and locale.


Timestamp Styles
++++++++++++++++

+-------------+-------------------------+--------------------------------------+
| Style       | Description             | Example Output                       |
+=============+=========================+======================================+
| t           | Short time              | ``16:20``                            |
+-------------+-------------------------+--------------------------------------+
| T           | Medium time             | ``16:20:30``                         |
+-------------+-------------------------+--------------------------------------+
| d           | Short date              | ``20/04/2021``                       |
+-------------+-------------------------+--------------------------------------+
| D           | Long date               | ``April 20, 2021``                   |
+-------------+-------------------------+--------------------------------------+
| f (default) | Long date, short time   | ``April 20, 2021 at 16:20``          |
+-------------+-------------------------+--------------------------------------+
| F           | Full date, short time   | ``Tuesday, April 20, 2021 at 16:20`` |
+-------------+-------------------------+--------------------------------------+
| s           | Short date, short time  | ``20/04/2021, 16:20``                |
+-------------+-------------------------+--------------------------------------+
| S           | Short date, medium time | ``20/04/2021, 16:20:30``             |
+-------------+-------------------------+--------------------------------------+
| R           | Relative time           | ``4 years ago``                      |
+-------------+-------------------------+--------------------------------------+


Guild Navigation Types
++++++++++++++++++++++

Guild navigation types link to the corresponding resource in the current server.

+--------------------------+-------------------------------------------------------------+
| Full Syntax              | Linked Resource                                             |
+==========================+=============================================================+
| ``<id:customize>``       | **Channel & Roles** tab with Onboarding prompts             |
+--------------------------+-------------------------------------------------------------+
| ``<id:browse>``          | **Browse Channels** tab                                     |
+--------------------------+-------------------------------------------------------------+
| ``<id:guide>``           | `Server Guide`_ tab                                         |
+--------------------------+-------------------------------------------------------------+
| ``<id:linked-roles>``    | `Linked Roles`_ tab                                         |
+--------------------------+-------------------------------------------------------------+
| ``<id:linked-roles:ID>`` | Specific linked role, opening the connection modal on click |
+--------------------------+-------------------------------------------------------------+


.. seealso::

    `Discord Developer Docs - Message Formatting`_


.. _Discord Developer Docs - Message Formatting: https://docs.discord.com/developers/reference#message-formatting
.. _Linked Roles: https://support.discord.com/hc/en-us/articles/10388356626711
.. _Server Guide: https://support.discord.com/hc/en-us/articles/13497665141655
.. _Twemoji: https://github.com/jdecked/twemoji