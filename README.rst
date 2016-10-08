Dojo Toolkit
============

.. image:: https://travis-ci.org/grupy-sanca/dojo-toolkit.svg?branch=master
  :target: https://travis-ci.org/grupy-sanca/dojo-toolkit

.. image:: https://coveralls.io/repos/github/grupy-sanca/dojo-toolkit/badge.svg?branch=master
  :target: https://coveralls.io/github/grupy-sanca/dojo-toolkit?branch=master


Toolkit for python coding dojos.

Source: https://github.com/grupy-sanca/dojo-toolkit


Features
--------
- Timer to determine the pilot's turn
- Display notifications on pilot's time up, tests passed and failed
- Dojo Semaphor through OS notifications
- Run tests after each save


How to use
----------
::

  $ pip install dojo-toolkit
  $ dojo /path/to/code/directory/


Contributing
------------

Check the `CONTRIBUING.rst <https://github.com/grupy-sanca/dojo-toolkit/blob/master/CONTRIBUTING.rst>`_ file to discover how you can help the development of dojo-toolkit.


Dependencies
------------
- Python 3
- `Libnotify <https://developer.gnome.org/libnotify>`_


Roadmap
-------
**0.5.0**

TDB


Changelog
---------

**0.4.0**

- Tests + CI (above 95% coverage)
- Sound notifications
- Minor bug fixes
- Minor improvements

**0.3.0**

- Major refactor
- Uses bumpversion

**0.2.0**

- Project improvements
- Release to PyPI

**0.1.0** (Initial version)

- Timer for managing rounds
- Watch code folder and run doctests on changes
- Show notifications using Libnotify
