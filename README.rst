Dojo Toolkit
============

Toolkit for python coding dojos.

Source: https://github.com/grupy-sanca/dojo-toolkit

Features
--------
- Timer to determine the pilot's turn
- Run tests automatically and notify when people can or cannot talk

How to use
----------
::

  $ pip install dojo-toolkit
  $ python -m dojo_toolkit /path/to/code/directory/

Dependencies
------------
- Python 3
- `Libnotify <https://developer.gnome.org/libnotify>`_

Roadmap
---------
**0.4.0**

- Tests + CI
- Minor bug fixes
- Sound notifications
- Minor improvements

Changelog
---------

**0.3.0**

- Major refactor
- Uses bumpversion

**0.2.0**

- Project improvements
- Release to PyPI

**0.1.0** (Initial version)

- Timer for managing rounds
- Watch code folder and run ``doctest``s on changes
- Show notifications using Libnotify
