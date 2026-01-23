.. _workspace-ident:

Your Identity
=============

Now that you are booted into Tails OS for the very first time, you are ready to
create your brand new online identity!

**Important:** Please take a moment to review our
:ref:`advice about online identities <advice-ident>`.

.. admonition:: **Take Your Time**
   :class: note

   The country has already fallen to tyranny and is quickly becoming a dictatorship.
   There is no reason to rush through this document. Please, **read it carefully**!

The :ref:`USB Flash Drive that you created <workspace-create>` is simply Tails OS
with a copy of the tools we use to manage this project. In order to contribute, you
must create an identity, so that it can be granted access to resources.

From a high-level overview, this is our approach to layered security:

=============  ==============  ==============
App/Service    Purpose         Target
=============  ==============  ==============
Tails OS       Privacy         People
Tor Network    Privacy         People
:ref:`advice`  Privacy         People
Email          Authorization   People/Project
GPG            Authentication  People/Project
SSH            Authentication  People/Project
GitHub         Authorization   Project
GitHub         Accounting      Project
=============  ==============  ==============

You may also wish to read more about the
:ref:`choices behind our toolset <advice-tools>`.

.. _account-passwords:

Remember Passwords
------------------

In order to be sure that your new identity is completely separate from yourself,
it is best to use brand new passwords. Tails OS comes with ``KeePassXC`` to help
keep track of these new passwords. You just need to keep track of the master
password and "password vault" (the saved file).

Although your Tails OS Flash Drive is a very secure place to keep your password
vault, it is not the safest. If your Flash Drive is lost or malfunctions, anything
stored on it will be gone. We recommend keeping a copy of this password file stored
in a more secure location, such as a separate flash drive stored in a safe.

TODO:

- Link to other keepassxc resources
- Find a video that shows the use of TOTP
- This file is encrypted, so you can call it anything and hide it "in plain view"

.. _account-email:

Email Account
-------------

Every reputable online identity begins with an email address. This identity will
be used to track your contributions, and so it is important to keep this separate
from yourself.

For example: ``mom4justice@webmail.com`` sounds anonymous, but it reveals that this
person is a mother and they are likely talking about justice in the real world.
Something like ``iamwitness12341111@webmail.com`` suggests someone recording on
the streets...somewhere.

Unfortunately, many online email providers now require a phone number for
registrations. We recommend the email service provider(s) listed here:

- **Atomicmail**

SSH and GPG
-----------

Although you have likely never heard of SSH or GPG, these are the standard tools
used for critical security, throughout all of technology. They continue to be used
because they are both reliable and flexible. When a security vulnerability is
discovered, it usually takes unrealistic preparation to execute and is quickly
resolved before anyone finds a practical exploit.

They both operate on a similar ``public and private key`` principal, where the
``public key`` is shared with other people and services, and the ``private key``
proves ownership of the ``public key``.

.. _account-ssh:

Create an SSH Key
-----------------

``SSH`` is an extremely flexible tool that functions exactly like a lock and key.

To create an SSH key pair:

1. Open up ``Console``
2. Run the command ``ssh-keygen -C <your-email>``
3. Press enter for the first prompt
4. Type a secure password, then press enter
5. Type the same password, and press enter again.

It should look similar to the following::

    # 2. Run the command ``ssh-keygen``
    amnesia@amnesia:~$ ssh-keygen -C iamwitness12341111@webmail.com
    Generating public/private ed25519 key pair.

    # 3. Press Enter
    Enter file in which to save the key (/home/amnesia/.ssh/id_ed25519): 

    # 4. Provide a password and press enter
    Enter passphrase for "/home/amnesia/.ssh/id_ed25519" (empty for no passphrase): 

    # 5. Provide the same password and press enter
    Enter same passphrase again: 

    # The rest is just information
    Your identification has been saved in /home/amnesia/.ssh/id_ed25519
    Your public key has been saved in /home/amnesia/.ssh/id_ed25519.pub
    The key fingerprint is:
    SHA256:pOBwoX+ft/09ekfXAffia0mYT9VfZ4Qz423jPWkUnig iamwitness12341111@webmail.com
    The key's randomart image is:
    +--[ED25519 256]--+
    |    .          . |
    |   . .       .=o.|
    |  o o   .    .=*=|
    |   = . o   E .o*X|
    |    o o S   .+o=X|
    |     . . .  o +=*|
    |        o .  +.+o|
    |         . o  =+.|
    |          . .++ +|
    +----[SHA256]-----+

That's all there is to it! The content of ``id_ed25519.pub`` now has your SSH
public key::

    amnesia@amnesia:~$ cat /home/amnesia/.ssh/id_ed25519.pub
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH+UB0Rkrq22QI4JazN4l6VHo7cP+JTD95a/pRPlSTfX iamwitness12341111@webmail.com

You should now save your secure password, ``id_ed25519``, and ``id_ed25519.pub``
into your password vault.

.. _account-gpg:

Create a GPG Key
----------------

When it comes to online identities, email is a great solution to uniquely identify
various contributors, but this is not enough to prove someone "owns" that email.

In order to **prove** that an identity is "owned" by someone, we use ``GPG``. This
is very similar to ``SSH``, except that it is designed to authenticate messages.

===========  =======
Using The    You Can
===========  =======
Private Key  Sign an email, or message, or any file at all
Public Key   Verify that a private key actually signed something
Public Key   Encrypt any email/message/file
Private Key  Decrypt anything that was encrypted with your public key
Private Key  Sign the Private Key of another person, showing trust
===========  =======

Even though it is possible to create multiple GPG Keys for the same identity (email),
each GPG Key has a unique identifier, making this the true unique identifier of
an anonymous contributor.

Creating a GPG Key is similar to creating an SSH Key:

1. Open up ``Console``
2. Run the command ``gpg --gen-key``
3. For the "Real name," the portion of your email before the '@' is fine, then press enter
4. Provide the email address that you just created, then press enter
5. Double check spelling, type ``O`` (letter) and press enter again
6. You will then need to provide a secure password

It should look similar to the following::

    # 2. Run the command ``gpg --gen-key``
    amnesia@amnesia:~$ gpg --gen-key
    gpg (GnuPG) 2.4.7; Copyright (C) 2024 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

    GnuPG needs to construct a user ID to identify your key.

    # 3. For the "Real name," the portion of your email before the '@' is fine, then press enter
    Real name: iamwitness12341111

    # 4. Provide the email address that you just created, then press enter
    Email address: iamwitness12341111@webmail.com
    You selected this USER-ID:
        "iamwitness12341111 <iamwitness12341111@webmail.com>"


    # 5. Double check spelling, type ``O`` (letter) and press enter again
    Change (N)ame, (E)mail, or (O)kay/(Q)uit? o

    # 6. You will then need to provide a secure password
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    gpg: /home/amnesia/.gnupg/trustdb.gpg: trustdb created
    gpg: directory '/home/amnesia/.gnupg/openpgp-revocs.d' created
    gpg: revocation certificate stored as '/home/amnesia/.gnupg/openpgp-revocs.d/8481BBC34CDD50801DEE42B8195CA29BFF5C92C0.rev'
    public and secret key created and signed.

    pub   ed25519 2026-01-21 [SC] [expires: 2029-01-20]
          8481BBC34CDD50801DEE42B8195CA29BFF5C92C0
    uid                      iamwitness12341111 <iamwitness12341111@webmail.com>
    sub   cv25519 2026-01-21 [E] [expires: 2029-01-20]

That long random string above the identity (email) is the ``GPG Key ID``::

    8481BBC34CDD50801DEE42B8195CA29BFF5C92C0

This is the actual ID that is used to build trust. When trust is violated, this
is also what allows us to review historical contributions and other key signatures.

To make a backup of this key, run::

    amnesia@amnesia:~$ gpg --export-secret-keys 8481BBC34CDD50801DEE42B8195CA29BFF5C92C0 > secret_key

You'll notice the console output also mentions a ``revocation certificate``::

    gpg: revocation certificate stored as '/home/amnesia/.gnupg/openpgp-revocs.d/8481BBC34CDD50801DEE42B8195CA29BFF5C92C0.rev'

This file should also be backed up. If your GPG key is ever lost or stolen, this
will allow you to tell the world that your previous key is no longer valid.

Key Server
~~~~~~~~~~

GPG supports "signing" another key, to show public trust that a key is owned
by a trusted identity. This builds something called a "web of trust" that allows
mutual trust between identities with no previous interaction.

Everything is cryptographically verified, so we can tell any public key server
about this key that we just created and it will synchronize with all other key
servers.

Telling the world about the unique key for this identity is as easy as:

1. Open up ``Console``
2. Run the command ``gpg --send-key <Key-ID-From-Above>``::

    amnesia@amnesia:~$ gpg --send-key 8481BBC34CDD50801DEE42B8195CA29BFF5C92C0
    gpg: sending key 0x195CA29BFF5C92C0 to hkp://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion

3. This will trigger an email bringing you to a page to verify key IDs
4. Click ``Send verification email`` next to your email
    (this may seem redundant--it is required because one key may have multiple emails)
5. Click the link in this verification email and the process should be complete::

    Your key 8481BBC34CDD50801DEE42B8195CA29BFF5C92C0 is now published for the identity iamwitness12341111@webmail.com.

Take a Breather
---------------

If you have never worked with security, SSH and GPG may seem like enough to make you
give up and walk away. Have no fear...

- This is as confusing as things get
- These are standard tools with lots of online documentation
- Your email address allows you to join our :ref:`discord` and ask for help

This is a great time to stop and take a break. Give your mind some time to recovery
from the key creation process.

.. _account-git:

Create Your GitHub Account
--------------------------

Although :ref:`git` itself is decentralized, it is extremely helpful to have a centralized
service like GitHub. This provides AAA (Authentication, Authorization, and Accounting)
that makes it easier to collaborate safely, with protection against spam and bad actors.

1. Go to https://github.com/
2. Follow the account creation process
3. We recommend making the following account changes (at https://github.com/settings/profile)

    1. **Check**: Make profile private and hide activity
    2. Click the "Update preferences" button below this checkbox
    3. **Uncheck**: Show Achievements on my profile
    4. Click the "Update preferences" button below this checkbox

4. Upload your ``SSH`` Key to: https://github.com/settings/keys

    1. Click "New SSH Key"
    2. Open ``Console``
    3. Run ``cat ~/.ssh/id_ed25519.pub``::

        amnesia@amnesia:~$ cat ~/.ssh/id_ed25519.pub
        ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIET0zknbWnxAT1m5kcUF54yFxdWC+ZeJeHSizWKKWNDN iamwitness12341111@webmail.com

    4. Copy and paste the line that follows your command (starting with "ssh") into the web browser
    5. Provide an optional title and click "Add SSH Key"

5. Upload your ``GPG`` Key to: https://github.com/settings/keys

    1. Click "New GPG Key"
    2. Open ``Console``
    3. Run ``gpg --armor --export <keyID-or-Email>``::

        amnesia@amnesia:~$ gpg --armor --export iamwitness12341111@webmail.com
        -----BEGIN PGP PUBLIC KEY BLOCK-----

        mDMEaXFPtBYJKwYBBAHaRw8BAQdAUQYOMl/ZPhLhiEcYpG2ryI2VIardSV6Ddd
        jv/4kP2Qkq1wzA8FAmlxT7QCGwwFCQmoAACgkQkP2Qkq1wzA85NAD/cmC568wy
        nic1nLG0M2lhbXdpdG5lc3MxMjM0MTExMSA8aWFtd2lmVzczEyMzQxMTExQHdl
        Ym1haWwuY29tPoiWBBMWCgA+FiEEnnM3a2+7LAjv/4kP2Qkq1wzA8FAmlxT7QC
        nOyOiVRgCl+AA2BPS6Opz2MNuDgEaXtBIKKwYBBAGXVQEFAQEHQMxkOKdB4IHK
        gEKL0T2goAHIgkUTKlogCarbaZ/7ZeV9VMHG8Pz/6sYIx7ckuXtpOMSYgQ9juf
        GwMFCQWjmoAFCwkIBwFQoJCAsCBBYCAwECHgECF4AACgkQkP2Qkq1wzA+UiAEA
        Eyobv9vjrzCNg2JH+kYr6FI3j1P4+HUjkBAOhOAV3jBxA0GQCrvhx+cQ1feQAv
        G63314baeZ303MsMMu9d4Gv5RQ5mp6AwEIB4h+BBgWCgAmFiEEnnM3a2+917LA
        0nJFdi4QX8qzMH
        =0k
        -----END PGP PUBLIC KEY BLOCK-----

    4. Copy and paste the line that follows your command (including all dashes) into the web browser
    5. Provide an optional title and click "Add GPG Key"

6. We recommend checking "Flag unsigned commits as unverified" (will automatically save)

That's it! Your GitHub account is now created, and it has all the security tokens
required to prove ownership of your identity, even though the identity is entirely
anonymous.

If we ever need to leave GitHub, you will be able to keep these security tokens and
use them to prove your identity on any future replacement. You can even change your
email address and username, and the GPG Key ID will be enough to verify any link to
your old email/username...unless you follow this process and start completely fresh.

Additional Accounts
-------------------

You will want to make more accounts, such as Reddit or Discord. As long as you
follow our :ref:`advice about online identities <advice-ident>`, you will be able
to keep these accounts safe.

The next section covers :ref:`actual usage of this workspace <workspace-usage>`.
