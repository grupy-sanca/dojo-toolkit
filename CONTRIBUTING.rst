Contributing to Dojo Toolkit
============================

Dojo Toolkit is an open source projects. We welcome many type of contributions:

- Code patches (pull requests) and reviews
- Documentation improvements
- Bug reports and ideas for new features (via `Github Issues`__)
- New features

__ https://github.com/grupy-sanca/dojo-toolkit/issues


Asking For Help
---------------

You can ask for help by joining grupy-sanca's Slack: http://grupy-sanca.herokuapp.com/
Join the channel #opensource. There we discuss dojo-toolkit development among other things.


How to Setup Git
----------------

The `django contributing docs`__ has a nice and small tutorial explaining how to
install and setup a local repository and working with github.

__ https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/working-with-git/#working-with-git-and-github


How to Run Dojo-Toolkit for development
---------------------------------------

1. Clone the project
::
  
  $ git clone https://github.com/grupy-sanca/dojo-toolkit.git

2. (optional) Create the virtual environment
::
  
  $ python -m venv env
  $ source env/bin/activate

3. Install requirements
::

  $ (env) pip install -r requirements-test.txt

Done :-)


How to Run Tests
----------------
::

  $ pip install -r -U requirements-test.txt
  $ py.test


Coding Style
------------

`PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ with line lenght up to 99 characters.
