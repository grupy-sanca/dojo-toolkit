Contributing to Dojo Toolkit
============================

Dojo Toolkit is an open source project. We welcome many kinds of contributions:

- Code patches (pull requests) and reviews
- Documentation improvements
- Bug reports and ideas for new features (via `Github Issues`__)
- New features

__ https://github.com/grupy-sanca/dojo-toolkit/issues


Asking For Help
---------------

You can ask for help by joining grupy-sanca's Telegram group @grupysanca or find us in our facebook page https://www.facebook.com/grupysanca/
There we discuss dojo-toolkit development among other things.


How to Setup Git
----------------

The `django contributing docs`__ has a nice and small tutorial explaining how to install and setup a local repository and working with github.
 
__ https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/working-with-git/#working-with-git-and-github


How to Run Dojo-Toolkit for development
---------------------------------------

Minimal Python version: 3.9.x

1. Clone the project
::
  
  $ git clone https://github.com/grupy-sanca/dojo-toolkit.git

2. Create the virtual environment using `Poetry <https://python-poetry.org/>`_
::
  
  $ make install

3. Install the entrypoint script locally
::

  $ pip install -e .


Done :-)

How to Run Dojo-Toolkit Tests
-----------------------------

After installing the depencencies, simply run:
::

  $ make test


Coding Style
------------

To run the linters
::

  $ make lint

`PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ with line lenght up to 99 characters.
