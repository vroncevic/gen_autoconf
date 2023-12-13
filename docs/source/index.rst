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

.. |documentation status| image:: https://readthedocs.org/projects/gen-avr8/badge/?version=latest
   :target: https://gen-avr8.readthedocs.io/en/latest/?badge=latest

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
        ├── conf/
        │   ├── gen_autoconf.logo
        │   ├── gen_autoconf.cfg
        │   ├── gen_autoconf_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── autogen.template
        │       ├── configure.template
        │       ├── Makefile.template
        │       ├── README.template
        │       └── src/
        │           ├── main.template
        │           └── Makefile.template
        ├── __init__.py
        ├── log/
        │   └── gen_autoconf.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_autoconf_run.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2020 - 2024 by `vroncevic.github.io/gen_autoconf <https://vroncevic.github.io/gen_autoconf>`_

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
