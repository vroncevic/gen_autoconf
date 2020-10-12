Create C project skeleton
--------------------------

**gen_autoconf** is tool for creating C project skeleton.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_autoconf/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_autoconf.svg
   :target: https://github.com/vroncevic/gen_autoconf/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_autoconf.svg
   :target: https://github.com/vroncevic/gen_autoconf/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_autoconf/badge/?version=latest
   :target: https://gen_autoconf.readthedocs.io/projects/gen_autoconf/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_autoconf/workflows/Install%20Python2%20Package%20gen_autoconf/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/workflows/Install%20Python2%20Package%20gen_autoconf/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_autoconf/workflows/Install%20Python3%20Package%20gen_autoconf/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/workflows/Install%20Python3%20Package%20gen_autoconf/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_autoconf/releases

To install this set of modules type the following:

.. code-block:: bash

    tar xvzf gen_autoconf-x.y.z.tar.gz
    cd gen_autoconf-x.y.z/
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data

You can use Docker to create image/container.

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_autoconf/workflows/gen_autoconf%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_autoconf/actions?query=workflow%3A%22gen_autoconf+docker+checker%22

Dependencies
-------------

**gen_autoconf** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Library structure
------------------

**gen_autoconf** is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_autoconf/dev/docs/arch_flow_usage.png

Code structure:

.. code-block:: bash

    .
    ├── gen_autoconf/
    │   ├── abstract/
    │   │   └── __init__.py
    │   ├── ats_info.py
    │   ├── cfg_base.py
    │   ├── config/
    │   │   ├── base_read_config.py
    │   │   ├── base_write_config.py
    │   │   ├── cfg/
    │   │   │   ├── cfg2object.py
    │   │   │   ├── __init__.py
    │   │   │   └── object2cfg.py
    │   │   ├── check_base_config.py
    │   │   ├── config_context_manager.py
    │   │   ├── file_checking.py
    │   │   ├── ini/
    │   │   │   ├── ini2object.py
    │   │   │   ├── __init__.py
    │   │   │   └── object2ini.py
    │   │   ├── __init__.py
    │   │   ├── json/
    │   │   │   ├── __init__.py
    │   │   │   ├── json2object.py
    │   │   │   └── object2json.py
    │   │   ├── xml/
    │   │   │   ├── __init__.py
    │   │   │   ├── object2xml.py
    │   │   │   └── xml2object.py
    │   │   └── yaml/
    │   │       ├── __init__.py
    │   │       ├── object2yaml.py
    │   │       └── yaml2object.py
    │   ├── console_io/
    │   │   ├── error.py
    │   │   ├── __init__.py
    │   │   ├── success.py
    │   │   ├── verbose.py
    │   │   └── warning.py
    │   ├── exceptions/
    │   │   ├── ats_attribute_error.py
    │   │   ├── ats_bad_call_error.py
    │   │   ├── ats_file_error.py
    │   │   ├── ats_key_error.py
    │   │   ├── ats_lookup_error.py
    │   │   ├── ats_type_error.py
    │   │   ├── ats_value_error.py
    │   │   └── __init__.py
    │   ├── ini_base.py
    │   ├── __init__.py
    │   ├── json_base.py
    │   ├── logging/
    │   │   ├── ats_logger_base.py
    │   │   ├── ats_logger_file.py
    │   │   ├── ats_logger_name.py
    │   │   ├── ats_logger.py
    │   │   ├── ats_logger_status.py
    │   │   └── __init__.py
    │   ├── option/
    │   │   ├── ats_option_parser.py
    │   │   └── __init__.py
    │   ├── register/
    │   │   └── __init__.py
    │   ├── xml_base.py
    │   └── yaml_base.py
    └── setup.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/gen_autoconf <https://vroncevic.github.io/gen_autoconf>`_

**gen_autoconf** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_autoconf/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
