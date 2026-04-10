===========
Quick start
===========

Requirements
============

* Python 3.12 or above
* Django 4.2 or newer


Install
=======

.. code-block:: bash

    pip install maykin-config-checks

Add ``maykin_config_checks`` to the Django ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        "maykin_config_checks",
        ...
    ]

Usage
=====

Implementing checks
-------------------

This library is based on the following components:

* The :class:`ConfigCheck` which implements the logic of a particular configuration check.
* The :class:`ConfigCheckResult`, which is the result of running a :class:`ConfigCheck`.
  It contains information about whether the check succeeded and additional information in case the check failed.
* The :func:`run_checks`, which runs all the :class:`ConfigCheck` that are retrieved by a collector
  function and returns an iterable of :class:`ConfigCheckResult`.

You can see dummy implementations of all of these components below:

.. literalinclude:: ../testapp/checks.py
    :language: python

View
----

To have an API view that returns the results of the performed config checks,
add the following to the ``urlpatterns``:

.. literalinclude:: ../testapp/urls.py
    :language: python

Where the argument ``checks_collector`` is a ``Callable[[], Iterable[ConfigCheck]]``. It is used to retrieve which config checks should
be performed by the view. You can also add the view multiple times to the ``urlpatters`` with different ``checks_collector`` arguments 
if you want to have multiple config check views that run different checks.

Management command
------------------

There is also a management command that can be used to run config checks from the CLI.

.. code-block:: bash

    django-admin config_checks --checks-collector dotted.path.to.checks_collector_fn


