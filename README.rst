
README for Pylint - https://pylint.pycqa.org/
=============================================

.. image:: https://github.com/PyCQA/pylint/actions/workflows/tests.yaml/badge.svg?branch=main
    :target: https://github.com/PyCQA/pylint/actions

.. image:: https://coveralls.io/repos/github/PyCQA/pylint/badge.svg?branch=main
    :target: https://coveralls.io/github/PyCQA/pylint?branch=main


.. image:: https://img.shields.io/pypi/v/pylint.svg
    :alt: Pypi Package version
    :target: https://pypi.python.org/pypi/pylint

.. image:: https://readthedocs.org/projects/pylint/badge/?version=latest
    :target: https://pylint.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. image:: https://results.pre-commit.ci/badge/github/PyCQA/pylint/main.svg
   :target: https://results.pre-commit.ci/latest/github/PyCQA/pylint/main
   :alt: pre-commit.ci status

.. |tideliftlogo| image:: https://raw.githubusercontent.com/PyCQA/pylint/main/doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White.png
   :width: 75
   :height: 60
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for pylint is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-pylint?utm_source=pypi-pylint&utm_medium=referral&utm_campaign=readme


======
Pylint
======

**It's not just a linter that annoys you!**

Pylint is a Python static code analysis tool which looks for programming errors,
helps enforcing a coding standard, sniffs for code smells and offers simple refactoring
suggestions.

It's highly configurable, having special pragmas to control its errors and warnings
from within your code, as well as from an extensive configuration file.
It is also possible to write your own plugins for adding your own checks or for
extending pylint in one way or another.

It's a free software distributed under the GNU General Public Licence unless
otherwise specified.

Development is hosted on GitHub: https://github.com/PyCQA/pylint/

You can use the code-quality@python.org mailing list to discuss about
Pylint. Subscribe at https://mail.python.org/mailman/listinfo/code-quality/
or read the archives at https://mail.python.org/pipermail/code-quality/

Pull requests are amazing and most welcome.

Install
-------

Pylint can be simply installed by running::

    pip install pylint

If you are using Python 3.6.2+, upgrade to get full support for your version::

    pip install pylint --upgrade

If you want to install from a source distribution, extract the tarball and run
the following command ::

    python setup.py install


Do make sure to do the same for astroid, which is used internally by pylint.

For debian and rpm packages, use your usual tools according to your Linux distribution.

More information about installation and available distribution format
can be found here_.

Documentation
-------------

The documentation lives at https://pylint.pycqa.org/.

Pylint is shipped with following additional commands:

* pyreverse: an UML diagram generator
* symilar: an independent similarities checker
* epylint: Emacs and Flymake compatible Pylint


Testing
-------

We use tox_ and pytest-benchmark_ for running the test suite. You should be able to install it with::

    pip install tox pytest pytest-benchmark


To run the test suite for a particular Python version, you can do::

    tox -e py37


To run individual tests with ``tox``, you can do::

    tox -e py37 -- -k name_of_the_test


We use pytest_ for testing ``pylint``, which you can use without using ``tox`` for a faster development cycle.

If you want to run tests on a specific portion of the code with pytest_, (pytest-cov_) and your local python version::

    # ( pip install pytest-cov )
    # Everything:
    python3 -m pytest tests/
    # Everything in tests/message with coverage for the relevant code:
    python3 -m pytest tests/message/ --cov=pylint.message
    coverage html
    # Only the functional test "missing_kwoa_py3":
    python3 -m pytest "tests/test_functional.py::test_functional[missing_kwoa_py3]"


Do not forget to clone astroid_ and install the last version::


    git clone https://github.com/PyCQA/astroid.git

    # From source
    python3 astroid/setup.py build sdist
    pip3 install astroid/dist/astroid*.tar.gz

    # Using an editable installation
    cd astroid
    python3 -m pip install -e .

Show your usage
-----------------

You can place this badge in your README to let others know your project uses pylint.

    .. image:: https://img.shields.io/badge/linting-pylint-yellowgreen
        :target: https://github.com/PyCQA/pylint

Use the badge in your project's README.md (or any other Markdown file)::

    [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

Use the badge in your project's README.rst (or any other rst file)::

    .. image:: https://img.shields.io/badge/linting-pylint-yellowgreen
        :target: https://github.com/PyCQA/pylint


If you use GitHub Actions, and one of your CI workflows begins with "name: pylint", you
can use GitHub's `workflow status badges <https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge#using-the-workflow-file-name>`_
to show an up-to-date indication of whether pushes to your default branch pass pylint.
For more detailed information, check the documentation.

.. _here: https://pylint.pycqa.org/en/latest/user_guide/installation.html
.. _tox: https://tox.readthedocs.io/en/latest/
.. _pytest: https://docs.pytest.org/en/latest/
.. _pytest-benchmark: https://pytest-benchmark.readthedocs.io/en/latest/index.html
.. _pytest-cov: https://pypi.org/project/pytest-cov/
.. _astroid: https://github.com/PyCQA/astroid

License
-------

pylint is, with a few exceptions listed below, `GPLv2 <https://github.com/PyCQA/pylint/blob/main/LICENSE>`_.

The icon files are licensed under the `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_ license:

- `doc/logo.png <https://raw.githubusercontent.com/PyCQA/pylint/main/doc/logo.png>`_
- `doc/logo.svg <https://raw.githubusercontent.com/PyCQA/pylint/main/doc/logo.svg>`_
