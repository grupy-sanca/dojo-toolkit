Dojo Toolkit
============

.. image:: https://github.com/grupy-sanca/dojo-toolkit/actions/workflows/test_push.yaml/badge.svg?branch=main
  :target: https://github.com/grupy-sanca/dojo-toolkit/actions/workflows/test_push.yaml?query=branch%3Amain

.. image:: https://coveralls.io/repos/github/grupy-sanca/dojo-toolkit/badge.svg?branch=main
  :target: https://coveralls.io/github/grupy-sanca/dojo-toolkit?branch=main


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

Installation:
::

  $ pip install dojo-toolkit


Running:
::

  $ dojo /path/to/code/directory/


For detailed information about running from source: `CONTRIBUING.rst <https://github.com/grupy-sanca/dojo-toolkit/blob/main/CONTRIBUTING.rst>`_
To see the options available use:
::

  $ dojo --help


Contributing
------------

Check the `CONTRIBUING.rst <https://github.com/grupy-sanca/dojo-toolkit/blob/main/CONTRIBUTING.rst>`_ file to discover how you can help the development of dojo-toolkit.


Dependencies
------------
- Python 3
- `Libnotify <https://developer.gnome.org/libnotify>`_


Roadmap
-------

**0.5**

TDB


Changelog
---------

**0.4**

- Tests + CI
- Sound notifications
- Minor bug fixes
- Minor improvements

**0.3**

- Major refactor
- Uses bumpversion

**0.2**

- Project improvements
- Release to PyPI

**0.1**

- Timer for managing rounds
- Watch code folder and run doctests on changes
- Show notifications using Libnotify
