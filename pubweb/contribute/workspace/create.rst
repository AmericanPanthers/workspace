.. _workspace-create:

First-Time Setup
================

[this is a summary of other documentation]
[this is the hardest part, please read carefully]

.. _workspace-init:

Prepare a Flash Drive
---------------------

This is a quick summary of upstream instructions, focusing on our recommendations:

1. Copy the `Tails OS <https://tails.net/install/>`__ image onto a Flash Drive
    - Short Version: Download the image and use Rufus to copy it onto a Flash Drive
2. Boot your computer using this newly-prepared Flash Drive
    - If you know how to verify Secure Boot is enabled, this is wise
    - Most laptops require tapping ``F12`` to select a custom boot device
3. If all goes well, you will be prompted to make some choices:
    - If you change language or formate, it is helpful to "Save" for future reboots
    - Enable the option to "Create Persistent Storage"
    - Open "Additional Settings" and configure an "Administrative Password"
       *(this password is temporary, and simple is fine)*
4. The next screen will guide you through preparing encrypted storage
    - Take some time to pick out a **VERY STRONG** password
       *(store this password in a personal password vault)*
    - The larger the Flash Drive, the longer this first startup will take (be patient)
5. When your Encrypted ``Persistent`` Storage is prepared, you will have a list of options:
    1. **We recommend enabling:**
       - Persistent Folder
       - GnuPG
       - SSH Client
       - Tor Browser Bookmarks
       - Additional Software
    2. You should **NOT** enable:
       - Dotfiles
    3. When all sliders turn blue, close this window using the "X" in the top-right

.. _workspace-prepare:

Copy Our Tools
--------------

6. Connect to the Tor network:
    1. Click the Onion (with the white x) in the top-right of your desktop screen
    2. Click "Open Tor Connection Assistant," then click "Open Wifi Settings"
    3. Follow on-screen steps to connect to a wifi network
    4. Once connected, close the "Wi-Fi" window using the "X" in the top-right
    5. Return to the Tor Connection assistant and proceed with on-screen instructions
        (Connect to Tor automatically WITHOUT a Tor bridge is typically sufficient)
    6. Establishing a connection can take some time, wait until this completes
    7. Once successfully connected, close this window using the "X" in the top-right
7. Open a "Console"
    1. Click "Apps" in the top-left of your screen
    2. Hover over "System Tools"
    3. Click "Console"
    4. OR: Top ``Super (Windows)`` key > type ``cons`` > Tap ``Enter``
8. Copy and paste (or carefully type) this text into the black window::

    curl -Ss https://codeberg.org/AmericanPanthers/workspace/raw/branch/main/.bin/bootstrap | sh

9. Double check caps (only the first S), punctuation, and spacing, then press ``Enter``
10. Follow the on-screen instructions
     - The temporary admin password you set at startup will be required

Now that you are running Tails OS with a copy of our basic tools, head to the next
section to :ref:`create a unique (and private) online identity <workspace-ident>`.
