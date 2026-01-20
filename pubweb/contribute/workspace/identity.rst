.. _workspace-ident:

Your Identity
=============

The :ref:`USB Flash Drive that you created <workspace-create>` is simply Tails OS
with a copy of the tools we use to manage this project. Please read more about the
:ref:`choices behind our toolset <advice-tools>`.

Now that you are booted into Tails OS for the very first time, you are ready to
create your brand new online identity!

**Important:** Please take a moment to review our
:ref:`advice about online identities <advice-ident>`.

.. _account-passwords:

Remember Passwords
------------------

You are **highly** encouraged to come up with brand new passwords. It is also wise
to use ``keepassxc`` (already installed) to create and maintain a password database.

We also encourage keeping a copy of this somewhere very safe. If you lose this, it
is likely that "your identity" will be permanently lost.

TODO:

- Link to other keepassxc resources
- Find a video that shows the use of TOTP
- This file is encrypted, so you can call it anything and hide it "in plain view"

.. _account-gpg:

Create a GPG Key
----------------

The actual "root authority" that owns the identify you create is called a GPG Key.

TODO: "Our bootstrap process (will soon) walked you through the process to create this.

.. _account-ssh:

Create an SSH Key
-----------------

TODO: "Our bootstrap process (will soon) walked you through the process to create this.

.. _account-email:

Email Account
-------------

Every online account begins with an email address or a phone number, and most
email address providers require a phone number.

These are our recommended email services provider(s):

- **Atomicmail** (captcha-only)

.. _account-git:

Create Your GitHub Account
--------------------------

Although ``git`` itself is decentralized, it is extremely helpful to have a centralized
service like GitHub. This provides AAA (Authentication, Authorization, and Accounting)
that makes it easier to collaborate safely, with protection agains spam and bad actors.

Your SSH and GPG keys should be uploaded to: https://github.com/settings/keys

We also maintain a mirror on https//Gitlab.com, in case there is ever any reason to
abandon https//GitHub.com. We recommend creating an account on both, so that you can
create your own mirrors.

TODO
----

At the moment, we are an anonymous group of online humans who happened to find each
other. Since "perfect is the enemy of good enough," documentating safe communication
options is a matter for another day.

See: :ref:`Usage <workspace-usage>`
