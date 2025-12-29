Development
===========

To develop the library locally, use:

.. code-block:: bash

    uv pip install -r pyproject.toml --all-extras

To run the test app, in the root of the repository run:

.. code:: bash

    export DJANGO_SETTINGS_MODULE=testapp.settings
    export PYTHONPATH=$PYTHONPATH:`pwd`

Then, you can run:

.. code:: bash

    django-admin runserver

Running tests
=============

To run the tests without tox, you can do the following (from the root of the repository):

.. code:: bash

    export DJANGO_SETTINGS_MODULE=testapp.settings
    export PYTHONPATH=$PYTHONPATH:`pwd`
    pytest tests

Release flow
============

#. Checkout a branch ``release/X.X.X`` (with the new version number).
#. In the root directory, use ``bump-my-version show-bump`` to show the possibilities, for example:

    .. code:: bash

        bump-my-version show-bump
            0.1.0 ── bump ─┬─ major ─ 1.0.0
                           ├─ minor ─ 0.2.0
                           ╰─ patch ─ 0.1.1

#. Bump the version. For example ``bump-my-version bump major``.
#. Update the CHANGELOG.md file.
#. Commit the changes and push the branch.
#. Once the branch is approved, merge it into main.
#. Create a tag with ``git tag -a 1.0.0 -m ":bookmark: Release 1.0.0"``.
#. Push the tag with ``git push origin 1.0.0``.
#. Once the new package has been pushed to Pypi, celebrate! 🎉