Public Website
==============

The domain we use to stay organized is https://AmericanPanthers.org.
This ``pubweb`` directory builds the static content backing this website.

Technology Choices
------------------

Great effort was put into choosing FOSS solutions that will can grow with the project.

We chose:

- **Static Website Generators:** For lightweight and consistent deployment
- **Sphinx Doc:** Extremely flexible with complexity kept separate from content
- **reST:** Very modular approach to documentation that remains readable
- **bin/pubweb:** For portability
- **falkon:** Lightweight browser for Tails OS that supports ``file://...``

Browser Security
~~~~~~~~~~~~~~~~

Tails OS discourages local connections, however we need `file://`` to be able
to view/test the website we just created. Rather than decrease browser security,
our `setup page <https://AmericanPanthers.org/workspace/setup.html>` installs
``falkon``, which ignores all sorts of security on Tails OS.

We recommend using falkon for to review/test changes to the site, however this
browser should never be used to connect to any website on the interet.

**DO NOT USE FALKON (ON TAILS) FOR ANY OTHER PURPOSE**

How to Make Changes
-------------------

All changes happen in three stages:

1. Open ``.rst`` files in a text editor, make changes, and then save the file
2. Build the new site, using ``pubweb -b`` and view with ``pubweb -v``
    - If ``falkon`` is already running, it will automatically reload after making changes
3. Push your changes to Codeberg (will auto-fork) and create a ``Pull Request``
    - Codeberg will provide instructions for this in response to failed ``commit+push``

To learn more about making content changes:

- `Breeze Documentation (theme features)
  <https://sphinx-breeze-theme.readthedocs.io/>`__
- `Sphinx-Doc reST Primer (quick intro)
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
- `reStructuredText Guide (online book)
  <https://restructuredtext-guide.readthedocs.io/en/latest/index.html>`__
- `Every Single Feature of RestructuredText (advanced)
  <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`__
