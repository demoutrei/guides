:description: Learn more about Privileged Intents and when to use them.

.. raw:: html

    <script id="discord:component-embed" type="application/json">
      {
        "component": {
          "type": 17,
          "accent_color": 3908956,
          "components": [
            {
              "type": 9,
              "components": [
                {
                  "type": 10,
                  "content": "# [Privileged Intents](https://guides.demoutrei.dev/discord/api/privileged_intents)\nLearn more about Privileged Intents and when to enable them."
                }
              ],
              "accessory": {
                "type": 11,
                "media": {
                  "url": "https://cdn.discordapp.com/embed/avatars/2.png"
                }
              }
            },
            {
              "type": 1,
              "components": [
                {
                  "type": 2,
                  "style": 5,
                  "label": "What are Privileged Intents?",
                  "url": "https://support-dev.discord.com/hc/en-us/articles/6207308062871-What-are-Privileged-Intents"
                },
                {
                  "type": 2,
                  "style": 5,
                  "label": "Getting Started with Privileged Intent Review",
                  "url": "https://docs.discord.com/developers/gateway/getting-started-with-privileged-intent-review"
                },
                {
                  "type": 2,
                  "style": 5,
                  "label": "You Might Not Need a Privileged Intent",
                  "url": "https://docs.discord.com/developers/gateway/you-might-not-need-a-privileged-intent"
                }
              ]
            }
          ]
        }
      }
    </script>


Privileged Intents
==================

.. important::

    Intents are optionally supported on the v6 gateway, but required as of v8.

**Privileged Intents** are Gateway intents that have additional requirements for access due to the nature of their data. Currently, these include:

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Guild Presences

        Controls access to presence update events, which include information about when users come online, go offline, or update their status.

    .. grid-item-card:: Guild Members

        Controls access to guild member events, like when members join, update their profile, or leave a server, as well as the ability to request guild member lists.

    .. grid-item-card:: Message Content

        Unlike other intents, this doesn't correspond to specific events but instead controls access to message content data across Discord's APIs, such as the ``content``, ``embeds``, ``attachments``, ``components``, and ``poll`` fields in message objects.

These intents are disabled by default due to the nature of their data and **should only be enabled as needed**. If your app doesn't have them enabled, it simply won't have access to the data they grant.


Application
+++++++++++

.. admonition:: Annual Application
    :class: important

    If your app already has Privileged Intents access granted from a prior review, you're good for now, but you will need to reapply annually.

    You will receive a notification when it's time to reapply. Keep track of your use-cases for each intent as they may evolve over time so the review process goes smoothly when the time comes for you to submit the latest information.

.. admonition:: How Discord Counts Users
    :class: tip

    Discord counts the number of unique users who have access to your app across all the servers it's installed in. When your app reaches the 10,000-user threshold, the app or team owner will receive a notification via e-mail and/or system DM. You will also see a message in the `Developer Portal`_ letting you know it's time to apply. You will have **90 days** to apply for Privileged Intents access.


User Count
^^^^^^^^^^

Under 10,000 users, you can turn Privileged Intents on and off from the `Developer Portal`_ as needed. No need to apply for access.

If your app reaches the 10,000-user threshold and has any Privileged Intents enabled (or attempts to enable a Privileged Intent), you'll receive a notification in the Developer Portal letting you know it's time to apply for access. You will have **90 days** from the date of the notification to apply. If you don't apply during this window, your app's current Privileged Intents access will be removed, but you can still apply at any time to request access again.

.. note::

    Your app can still continue joining servers and reaching new users while its submission is under review.


Audit Use-Cases
^^^^^^^^^^^^^^^

Before you apply for anything, jot down of what data your bot actually needs. Review your app to make sure its use-case requires Privileged Intent access and it is consistent with Discord's `Developer Policy`_ and `Developer Terms of Service`_.


Use-Case Decision
^^^^^^^^^^^^^^^^^

For each intent in your app is using, you can:

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: A: Remove the Dependency

        If you can accomplish the same thing without the Privileged Intent, remove the dependency. This is less work in the long run because you won't need to submit for review demonstrating that the access is required, you won't need to reapply annually, and you won't risk losing access.

        .. admonition:: Prefix Commands
            :class: important

            Prefix commands are **not** valid use-cases for the Message Content Privileged Intent; you must implement your commands as Slash commands instead.

    .. grid-item-card:: B: Apply for Privileged Intent Access

        If your bot genuinely needs the data that the Privileged Intent provides for a compliant use-case and there's no alternative, you can apply for access.

        .. grid:: 1
            :class-row: surface
            :gutter: 3

            .. grid-item-card:: Be specific about your use-case

                Explain what your bot does with the data and why interactions can't replace it.

            .. grid-item-card:: Only request what you need

                Requesting intents you can't demonstrate your bot needs hurts your submission.

            .. grid-item-card:: Explain how you handle the data responsibly.

                If you're storing the data, explain why it's necessary and describe your retention policy and security measures.


Enable the Intent
^^^^^^^^^^^^^^^^^

There are two places you need to enable a Privileged Intent if you have access: the `Developer Portal`_, and your code.

If you enable an intent in your code but not in the portal (or vice versa), you will get a ``[DisallowedIntents]`` error when your app tries to connect.


-----

.. admonition:: Sources
    :class: seealso

    `Getting Started with Privileged Intent Review`_

    `What are Privileged Intents?`_

.. _Developer Policy: https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy
.. _Developer Portal: https://discord.dev/
.. _Developer Terms of Service: https://support-dev.discord.com/hc/en-us/articles/8562894815383-Discord-Developer-Terms-of-Service
.. _Getting Started with Privileged Intent Review: https://docs.discord.com/developers/gateway/getting-started-with-privileged-intent-review
.. _What are Privileged Intents?: https://support-dev.discord.com/hc/en-us/articles/6207308062871-What-are-Privileged-Intents