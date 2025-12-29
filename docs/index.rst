
======================================================
Welcome to Maykin Configuration Checks' documentation!
======================================================

:Version: 0.1.0
:Source: https://github.com/maykinmedia/config-checks
:Keywords: ``Django``, ``Maykin``, ``configuration``, ``health checks``
:PythonVersion: 3.12, 3.13

|build-status| |code-quality| |ruff| |coverage| 

|python-versions| |django-versions| |pypi-version|

This library aims to standardise how health checks for Maykin Django applications 
are run. The checks are meant to validate that the configuration that is normally
performed in the Admin or via ``django-setup-configuration`` is correct.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   development


.. |build-status| image:: https://github.com/maykinmedia/config-checks/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/config-checks/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/config-checks/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/config-checks/actions?query=workflow%3A%22Code+quality+checks%22

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. |coverage| image:: https://codecov.io/gh/maykinmedia/config-checks/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/config-checks
    :alt: Coverage status

.. |docs| image:: https://app.readthedocs.org/projects/config-checks/badge/?version=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/maykin-config-checks.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/maykin-config-checks.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/maykin-config-checks.svg
    :target: https://pypi.org/project/maykin-config-checks/
