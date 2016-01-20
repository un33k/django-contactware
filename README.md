Django Contactware
====================

**A Django application to handle contact forms**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]
[![download-image]][download-link]


Overview
====================

**Best attempt** to handle contact forms while keeping it **DRY**.


How to install
====================

    1. easy_install django-contactware
    2. pip install django-contactware
    3. git clone http://github.com/un33k/django-contactware
        a. cd django-contactware
        b. run python setup.py
    4. wget https://github.com/un33k/django-contactware/zipball/master
        a. unzip the downloaded file
        b. cd into django-contactware-* directory
        c. run python setup.py


How to use
====================

   ```python
   Include `contactware` in your `INSTALLED_APPS`, migrate, provide templates and enjoy.
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([BSD](LICENSE.md)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-contactware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-contactware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-contactware.svg
[version-link]: https://pypi.python.org/pypi/django-contactware

[coverage-image]: https://coveralls.io/repos/un33k/django-contactware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-contactware

[download-image]: https://img.shields.io/pypi/dm/django-contactware.svg
[download-link]: https://pypi.python.org/pypi/django-contactware
