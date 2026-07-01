Create C project skeleton
--------------------------

**gen_autoconf** is tool for creating C project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_autoconf python checker| |gen_autoconf python package| |github issues| |documentation status| |github contributors|

.. |gen_autoconf python checker| image:: https://github.com/vroncevic/gen_autoconf/actions/workflows/gen_autoconf_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/actions/workflows/gen_autoconf_python_checker.yml

.. |gen_autoconf python package| image:: https://github.com/vroncevic/gen_autoconf/actions/workflows/gen_autoconf_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/actions/workflows/gen_autoconf_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_autoconf.svg
   :target: https://github.com/vroncevic/gen_autoconf/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_autoconf.svg
   :target: https://github.com/vroncevic/gen_autoconf/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-autoconf/badge/?version=latest
   :target: https://gen-autoconf.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_autoconf python3 build|

.. |gen_autoconf python3 build| image:: https://github.com/vroncevic/gen_autoconf/actions/workflows/gen_autoconf_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/actions/workflows/gen_autoconf_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_autoconf/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_autoconf-x.y.z.tar.gz
    cd gen_autoconf-x.y.z
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_autoconf

Dependencies
-------------

**gen_autoconf** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_autoconf** is based on OOP

Code structure

.. code-block:: bash

    gen_autoconf/
         ├── application/
         │   ├── __init__.py
         │   └── service.py
         ├── domain/
         │   ├── __init__.py
         │   ├── models.py
         │   └── ports/
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── gen_autoconf_bundle.py
         ├── infrastructure/
         │   ├── cli.py
         │   ├── cli_bundle.py
         │   ├── config/
         │   │   ├── gen_autoconf.cfg
         │   │   ├── gen_autoconf.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── gen_autoconf_command.py
         │   ├── icli.py
         │   ├── icli_command.py
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         └── py.typed

     6 directories, 22 files

Usage
-----

Install package

.. code-block:: bash

    pip3 install gen_autoconf

Prepare main entry point by downloading `main.py <https://raw.githubusercontent.com/vroncevic/gen_autoconf/master/main.py>`_ or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_autoconf/master/main.py

Running tool for creating new C autoconf project

.. code-block:: bash

    python3 main.py create --name mytool --output ./demo/

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2020 - 2026 by `vroncevic.github.io/gen_autoconf <https://vroncevic.github.io/gen_autoconf>`_

**gen_autoconf** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_autoconf/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
