:description: Discord API Frequently Asked Questions.


Frequently Asked Questions
==========================

Discord API Frequently Asked Questions.


How Do I Get A Bot Token?
+++++++++++++++++++++++++

Go to your `Developer Portal`_ in a browser of your choice, and select your desired application. Navigate to your application's **Bot** tab from the left sidebar.

.. figure:: /_static/discord/api/faq/DPortal_BotTab.png
    :align: center
    :width: 40%

Just below the bot's username, you'll find a **Token** section. To fetch and copy a bot token, you'll have to click on the ``Reset Token`` button.

.. figure:: /_static/discord/api/faq/token_placement.png
    :align: center
    :width: 80%

.. important::

    Store your bot's token in a secure place, e.g. in a password manager or in a ``.env`` file. **Never, ever, share it to anyone you don't trust. Anyone who has access/stored your bot token can do anything with your bot in their behalf**.

    
    .. admonition:: What To Do If My Bot Token's Leaked/Hacked?
        :class: hint

        Immediately reset your bot's token and store the new one more properly and secured.


How Do I Invite My Bot?
+++++++++++++++++++++++

Go to your `Developer Portal`_ in a browser of your choice, and select your desired application. Multiple ways you can get an invite of your bot.


Method 1
^^^^^^^^

Navigate to your application's **OAuth2** tab from the left sidebar, and scroll down to the **OAuth2 URL Generator**.


.. figure:: /_static/discord/api/faq/DPortal_OAuth2Tab.png
    :align: center
    :width: 80%


Under the **Scopes** area, tick ``bot`` and, if your bot utilizes application commands, ``applications.commands`` scopes.

Ticking the ``bot`` scope will prompt the **Bot Permissions** area. Select the scopes necessary for your bot to function.


.. danger::

    Under no circumstances does your bot **needs** the Administrator permission. Giving your bot the Administrator permission may lead to worse consequences when you get your bot token compromised.


In the **Integration Type** portion, select ``Guild Install`` if you want to invite your bot to a Discord server/guild; or ``User Install`` if you want to install it to your account.

Once things are set, you will be given with an invite URL under **Generated URL** below that you can copy and paste to your browser.


.. admonition:: Issue: It's not giving me an invite URL
    :class: tip

    You could be refused from be given an invite link for a few reasons.

    Case 1: Redirect URI
      If it's prompting your to enter a redirect URI, you may have the **Requires OAuth2 Code Grant** setting enabled.

      To fix this, navigate to the **Bot** tab from the left sidebar, and scroll down to the **Authorization Flow** section.


      .. figure:: /_static/discord/api/faq/DPortal_AuthFlow_CodeGrant.png
          :align: center
          :width: 80%

      
      Disable **Requires OAuth2 Code Grant** setting and save changes. Re-doing the steps should prompt you an invite URL now.


.. admonition:: Misconception
    :class: attention

    The **OAuth2 General URL** does **NOT** function as settings and will **NOT** save as you go on.


Method 2
^^^^^^^^

Navigate to your application's **Installation** tab from the left sidebar.


.. figure:: /_static/discord/api/faq/DPortal_InstallationTab.png
    :align: center
    :width: 80%


Under the **Installation Contexts**: to be able to invite to a Discord server/guild, the **Guild Install** method must be ticked; to be able to install the app to your account, the **User Install** method must be ticked.

In the **Install Link** portion, select upon the ``Discord Provided Link`` option.


.. admonition:: Issue: I cannot see that option
    :class: tip

    If you cannot see the option, you likely have the **Public Bot** setting disabled.

    To fix this, navigate to the **Bot** tab from the left sidebar, and scroll down to the **Authorization Flow** section.


    .. figure:: /_static/discord/api/faq/DPortal_AuthFlow_PublicBot.png
        :align: center
        :width: 80%


    Enable **Public Bot** setting and save changes.


Scrolling down, a **Default Install Settings** section is prompted. For you to invite your bot with a :term:`bot user`, the scopes under **Guild Install** must include the ``bot`` scope.

Afterward, select the permissions necessary for your bot to function. Save changes.

Once things are set, an invite URL will be generated in the **Install Link** section---you can copy it and paste it to your browser.


.. note::

    Setting an install link will append an "Add App" button in your app's profile that other users can use to invite your app to their servers or install to their accounts, depending on the configuration.


Glossary
++++++++


.. glossary::

    Bot user
      Physical manifestation of your application---the user/member that you see in the Members List in a channel.


.. seealso::

    `Discord API Documentation`_


.. _Discord API Documentation: https://discord.dev
.. _Developer Portal: https://discord.com/developers/applications