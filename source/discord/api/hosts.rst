Bot & Server Hosts
==================

.. seealso::

    `Inbestigator's Hosting List`_, based off the original mega thread.


.. grid:: 1 2 2 2
    :gutter: 3


    .. grid-item-card:: Serverless

        - `AWS Lambda`_

        - `CF Workers`_

        - `Deno Deploy`_

        - `GCP Run`_

        - `Netlify Functions`_


        .. attention::

            See `Shared IP Warning <#shared-ip-warning>`_ before using anything serverless.


    .. grid-item-card:: VPS / Dedicated

        - `Aruba Cloud`_

        - `Aurologic`_

        - `AWS EC2`_

        - `AWS Lightsail`_

        - `Contabo`_

        - `Digital Ocean`_

        - `GalaxyGate`_
        
        - `GCP VMs`_
        
        - `Hetzner`_
        
        - `Linode / Akamai Cloud`_
        
        - `Netcup`_
        
        - `Oracle Cloud`_
        
        - `Orihost`_
        
        - `OVHCloud`_
        
        - `Racknerd`_
        
        - `Railway`_
        
        - `Scaleway`_
        
        - `Time4VPS`_
        
        - `Vultr`_
        
        - `Webdock`_
        
        - `Wispbyte`_


Knowledgebase
+++++++++++++


Shared IP Warning
^^^^^^^^^^^^^^^^^

Discord employs Cloudflare, amongst other methods, to limit bad requests on a per IP address basis. It's highly recommended to `read through their documentation on the matter <https://docs.discord.com/developers/topics/rate-limits?ref=refactored.blog#invalid-request-limit-aka-cloudflare-bans>`_.

This is important to understand because while services like `Railway`_, `Vercel`_, `Netlify`_, and even `AWS Lambda`_ s are amazing pieces of technology, they **do not guarantee the IP address**. This means that you and 100 other developers could be using the same IP address, and if one of you exceeds the failed request threshold then it's a Cloudflare IP ban for the entire IP and it means that you and all 100 other developers will be temporarily restricted.

If you're encountering issues with rate limits and/or Cloudflare bans, your best bet is to get a VPS or server with a dedicated IP.


Identifying Scam Hosts
^^^^^^^^^^^^^^^^^^^^^^

If it's too good to be true, it is. Compute is not free, electricity is not free. While hosts can offer it really cheap (`OVHCloud`_ has some as low as a couple USD a month), it's never going to be free.


Never accept free hosting inside Discord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may get DMs or people offering to host your bot for free, these are almost always scams. They could be trying to hijack your bot token and take control of it or farm your code/data.


If it's free, you're the product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While not true for every host, 99% of the ones we've seen come through this server are outright scams or `summerhosts <https://www.urbandictionary.com/define.php?term=summerhost>`_.


"Vibe coded" hosts
~~~~~~~~~~~~~~~~~~

These kinda hosts combine panels like `Pterodactyl`_ with a vibe coded website to try to quickly gain traction with zero effort.

Once you start seeing the common outputs from AI in terms of webdesign, you tend to spot them anywhere.

.. admonition:: Example
    :class: hint

    .. figure:: https://i.imgur.com/mFXsWRo.png
        :align: center
        :width: 80%

        Clearly AI-made landing page


    .. figure:: https://i.imgur.com/3uGCCBe.png
        :align: center
        :width: 80%
        
        AI loves emojis and em-dashes
        

    .. figure:: https://i.imgur.com/iSQQeQP.png
        :align: center
        :width: 80%

        Can't even have a proper logo


Common Software Scams Run
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    While none of these software on their own are bad, they *can* be indicative of a potential scam due to how common they or how they're free/open-source.


`WHMCS`_--Very common in the web hosting space for billing, customer management, and automation. Scam sites (and even some legitimate hosts) runs nulled/cracked copies of `WHMCS`_ which is obviously illegal and also a security risk. `WHMCS`_ runs a service that you can `very any license yourself <https://www.whmcs.com/members/verifydomain.php>`_.

`Pterodactyl`_ **/ Pelican Panel**--An open-source game control panel that is amazing software, however many scams or smaller hosting companies will use this panel to deploy "eggs" (Docker containers) as a service they sell. Other panels include: `FeatherPanel`_.


Referral Systems
~~~~~~~~~~~~~~~~

These are not inherently bad, but people will try to use these systems to grow their scam or bad hosting service. You should always question the intent about someone recommending a service to you, especially if they're smaller operations.

If you're ever not sure about a link someone posts, then you can right-click (or press-and-hold) the message and click "Copy Text". Markdown links will look as `masked links <../markdown#masked-links>`_ which is a way people can try to hide bad links behind text that masks them.


Dedicated Discord Bot Hosting Services
++++++++++++++++++++++++++++++++++++++

Some hosting companies offer specifically Discord bot hosting. This section is a factual breakdown of the realistic cost per GB of RAM and per CPU/vCPU compared to traditional hosting as well as providing lose cost/free alternatives that even some of those same hosts base their systems on.


Cost Calculations
^^^^^^^^^^^^^^^^^

To make it fair, we'll only account for RAM and CPU since everything else differs. We'll provide that as a breakdown, provide information on the host, as well as any need to knows regarding IP addresses. For example if `Hetzner`_ provides 2vCPUs and 2GB of RAM for $5 a month (we'll convert everything to USD) then we'll assume 50% of cost is CPU and 50% of the cost is RAM. Which means it's $1.25 per CPU and $1.25 per GB of RAM. There's a lot more to the cost, yes, but for simplicity sake it's easier to break it down this way.

Obviously companies charge a premium because they manage the resources, but we believe you should know the cost. If you manage the panels yourself you'll get cheaper month to month, but you'll spend time maintaining and updating...for many this is optimal trade-off for a low-cost solution. This also doesn't account for how many bots you can run, some hosts will charge you per bot while VPS-based approaches do not restrict you past the purchased resource limits.


Baseline
^^^^^^^^

For simplicity we will take the median cost of entry level shared CPU VPS plans from `Hetzner`_, `OVHCloud`_, and `Contabo`_; basically the hosts you'll see heavily recommended. We'll use USD, East-coast region pricing (as available). Most bot hosts that have been researched has usually gone up to only 8GB RAM, but for outliers we'll also consider 12GB pricing. We will also be doing only monthly pricing excluding all sale costs as not every provider is running sales or offers annual options.

Also something to note: some places will use "xx% CPU" in their pricing. This is standard in cloud hosting space and 100% = 1vCPU, so 50% CPU = 0.5CPU.

Media costs per provider:

- `OVHCloud`_: $0.54 per CPU, $0.27 per GB RAM

- `Contabo`_: $0.64 per CPU, $0.33 per GB RAM

- `Hetzner`_ (added the +$1.9 cost per IPv4 to total): $1.16 per CPU, $0.58 per GB RAM

Median overall cost:

- **CPU**: $0.78 per

- **RAM**: $0.39 per GB


Self-Hosting / Cloud Panels
^^^^^^^^^^^^^^^^^^^^^^^^^^^

By far this is the best option, there's plenty of self-hosted panels that are fantastic and can replicate a lot of what these dedicated hosts provide at a fraction of the cost (or completely free! You just pay for the server) and with no real limitations (besides resource usage). However the trade-off for free panel is you update it yourself.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Self-Hosted

        - `Pelican`_

        - `Pterodactyl`_

        - `Coolify`_

    .. grid-item-card:: Cloud Hosted

        - `Coolify Cloud`_, $5 per month for 2 servers

        - `Dokploy`_, $4.50 per month for 1 server

        - `Wisp`_, $5 per server per month (coming soon: a free option for personal use)


Verdict
~~~~~~~

No matter what you choose, in most every case any combination of the above will *always* be cheaper than any dedicated Discord bot host.

Here's some example configs compared to the highest tier plan on a bot hoster:

Bot Host, $10/m:
  3vCPUs, 7GB RAM, 100GB SSD, maximum 13 bots, low traffic IP (not dedicated IP)

`OVHCloud`_:
  - VPS-1, $9.20/m:
      $5 `Coolify`_, 4vCPUs, 8GB RAM, 75GB SSD, dedicated IP, no max limit on anything besides resources

  - VPS-2, $11.75/m:
      $5 `Coolify`_, 8vCPUs, 16GB RAM, 160GB SSD, add-on IP

As you can see even accounting for the hosted panel cost and dedicated IP address (not shared) the median is $1.10 per CPU, $0.54 per GB RAM. Much lower than the hosts $1.66 per CPU, $0.71 per GB RAM for the plan.


Sparked Host
^^^^^^^^^^^^

Plan Pricing Breakdown
~~~~~~~~~~~~~~~~~~~~~~

- **Basic**: $1 per CPU, $1 per GB RAM

- **Advanced**: $1.33 per CPU, $1 per GB RAM

- **Advanced+**: $1.81 per CPU, $0.66 per GB RAM

- **Ultimate**: $1.66 per CPU, $0.71 per GB RAM

Median:
- **CPU**: $1.50 per CPU, **92% above** `baseline <#baseline>`_
- **RAM**: $0.85 per GB, **118% above** `baseline <#baseline>`_

It also appears that anything below Ultimate does not come with a low traffic IP and based on the `help articles provided <https://help.sparkedhost.com/en/article/what-is-a-low-traffic-dedicated-ip-and-how-do-i-order-it-qe02mm/>`_ the cost of a low traffic is ~$1.69 a month and a dedicated is $7.93 a month (**239% to 317% markup**), `Hetzner`_ is $1.90 a month per additional with a $6 setup feee and OVH is $2.34 a month.


IP Address Limitation
~~~~~~~~~~~~~~~~~~~~~

They use a pool of IP addresses that bots are proxied through. Quote from their own employee on how it works:

  Each IP is limited to max 20 bots. If your bot gets rate limited, the support team will assign you a new IP address (usually within 10--30 minutes depending on the time of day).

  -- `Source <https://discord.com/channels/613425648685547541/1478860733365354687/1479462800681337035>`_, `Imgur backup <https://imgur.com/a/XHJwN8s>`_

This means that you could drop requests during any period of downtime. So be sure your library supports automatic retries and that you're using some logging to ensure you're capturing issues.


Features
--------

**Pros**:

- Backups.

- Provides MySQL databases.

- Offers dedicated IPv4 addons, despite the over 200% markup.

- Managed resources.


**Cons**:

- IP address rotation still requires human intervention (CEO states its usually within a minute though).

- The markup per CPU and GB is extremely high above baseline.

- Limited language support (only Java, Python, and JavaScript).

- Maintains support for long EOL'd language versions (Node v12 ended support April 2022).

- Doesn't support latest Node LTS versions (22, 24, 26), based on their FAQ.

- IPv4 addon is almost $6 higher than standard hosting providers.


-----

**Source thread**: `Bot & Server Host Mega Thread`_

**Thread OP**: `MatthewSH@github <https://github.com/MatthewSH>`_

**OG Thread OP**: `Soheab@github <https://github.com/Soheab>`_


.. _Aruba Cloud: https://www.arubacloud.com/
.. _Aurologic: https://aurologic.com/
.. _AWS EC2: https://aws.amazon.com/ec2/
.. _AWS Lambda: https://aws.amazon.com/lambda/
.. _AWS Lightsail: https://aws.amazon.com/lightsail/
.. _Bot & Server Host Mega Thread: https://canary.discord.com/channels/613425648685547541/1478860733365354687
.. _CF Workers: https://workers.cloudflare.com/
.. _Contabo: https://contabo.com/en-us/
.. _Coolify: https://coolify.io/
.. _Coolify Cloud: https://coolify.io/pricing
.. _Deno Deploy: https://deno.com/deploy
.. _Digital Ocean: https://www.digitalocean.com/
.. _Dokploy: https://dokploy.com/pricing
.. _FeatherPanel: https://featherpanel.com/
.. _GalaxyGate: https://galaxygate.net/
.. _GCP Run: https://cloud.google.com/run?hl=en
.. _GCP VMs: https://cloud.google.com/products/compute?hl=en
.. _Hetzner: https://www.hetzner.com/
.. _Inbestigator's Hosting List: https://inbestigator.vercel.app/hosting
.. _Linode / Akamai Cloud: https://www.linode.com/
.. _Netcup: https://www.netcup.com/en
.. _Netlify: https://www.netlify.com/
.. _Netlify Functions: https://www.netlify.com/platform/core/functions/
.. _Oracle Cloud: https://www.oracle.com/cloud/
.. _Orihost: https://orihost.com/
.. _OVHCloud: https://us.ovhcloud.com/
.. _Pelican: https://pelican.dev/
.. _Pterodactyl: https://pterodactyl.io/
.. _Racknerd: https://www.racknerd.com/
.. _Railway: https://railway.com/
.. _Scaleway: https://www.scaleway.com/en/
.. _Time4VPS: https://www.time4vps.com/
.. _Vercel: https://vercel.com/
.. _Vultr: https://www.vultr.com/
.. _Webdock: https://webdock.io/en
.. _WHMCS: https://www.whmcs.com/
.. _Wisp: https://wisp.gg/
.. _Wispbyte: https://wispbyte.com/