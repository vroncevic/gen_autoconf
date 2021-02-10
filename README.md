<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_autoconf/dev/docs/gen_autoconf_logo.png" width="25%">

# Create C project skeleton

**gen_autoconf** is tool for creating C project skeleton.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_autoconf/workflows/Python%20package%20gen_autoconf/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_autoconf.svg)](https://github.com/vroncevic/gen_autoconf/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_autoconf.svg)](https://github.com/vroncevic/gen_autoconf/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Library structure](#library-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_autoconf/workflows/Install%20Python2%20Package%20gen_autoconf/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_autoconf/workflows/Install%20Python3%20Package%20gen_autoconf/badge.svg?branch=master)

Navigate to **[release page](https://github.com/vroncevic/gen_autoconf/releases)** download and extract release archive.

To install modules, locate and run setup.py, type the following:
```
tar xvzf gen_autoconf-x.y.z.tar.gz
cd gen_autoconf-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/gen_autoconf
copying gen_autoconf/__init__.py -> build/lib.linux-x86_64-2.7/gen_autoconf
creating build/lib.linux-x86_64-2.7/gen_autoconf/pro
copying gen_autoconf/pro/__init__.py -> build/lib.linux-x86_64-2.7/gen_autoconf/pro
copying gen_autoconf/pro/write_template.py -> build/lib.linux-x86_64-2.7/gen_autoconf/pro
copying gen_autoconf/pro/read_template.py -> build/lib.linux-x86_64-2.7/gen_autoconf/pro
copying gen_autoconf/pro/gen_pro.py -> build/lib.linux-x86_64-2.7/gen_autoconf/pro
creating /usr/local/lib/python2.7/dist-packages/gen_autoconf
copying build/lib.linux-x86_64-2.7/gen_autoconf/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_autoconf
creating /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro
copying build/lib.linux-x86_64-2.7/gen_autoconf/pro/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro
copying build/lib.linux-x86_64-2.7/gen_autoconf/pro/write_template.py -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro
copying build/lib.linux-x86_64-2.7/gen_autoconf/pro/read_template.py -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro
copying build/lib.linux-x86_64-2.7/gen_autoconf/pro/gen_pro.py -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_autoconf/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro/write_template.py to write_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro/read_template.py to read_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_autoconf/pro/gen_pro.py to gen_pro.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating gen_autoconf.egg-info
writing requirements to gen_autoconf.egg-info/requires.txt
writing gen_autoconf.egg-info/PKG-INFO
writing top-level names to gen_autoconf.egg-info/top_level.txt
writing dependency_links to gen_autoconf.egg-info/dependency_links.txt
writing manifest file 'gen_autoconf.egg-info/SOURCES.txt'
reading manifest file 'gen_autoconf.egg-info/SOURCES.txt'
writing manifest file 'gen_autoconf.egg-info/SOURCES.txt'
Copying gen_autoconf.egg-info to /usr/local/lib/python2.7/dist-packages/gen_autoconf-1.0.0.egg-info
```

Install lib data
```
python setup.py install_data
running install_data
copying gen_autoconf/run/gen_autoconf_run.py -> /usr/local/bin/
creating /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf
copying gen_autoconf/conf/gen_autoconf.cfg -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/
copying gen_autoconf/conf/gen_autoconf_util.cfg -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template
copying gen_autoconf/conf/template/README.md -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/
copying gen_autoconf/conf/template/Makefile.am -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/
copying gen_autoconf/conf/template/configure.ac -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/
creating /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/src
copying gen_autoconf/conf/template/src/Makefile.am -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/src/
copying gen_autoconf/conf/template/src/main.c -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/src/
creating /usr/local/lib/python2.7/dist-packages/gen_autoconf/log
copying gen_autoconf/log/gen_autoconf.log -> /usr/local/lib/python2.7/dist-packages/gen_autoconf/log/

```

Or You can use docker to create image/container.

[![gen_autoconf docker checker](https://github.com/vroncevic/gen_autoconf/workflows/gen_autoconf%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_autoconf/actions?query=workflow%3A%22gen_autoconf+docker+checker%22)

### Dependencies

**gen_autoconf** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Library structure

**gen_autoconf** is based on OOP:

Library structure:
```
.
├── conf/
│   ├── gen_autoconf.cfg
│   ├── gen_autoconf_util.cfg
│   └── template/
│       ├── configure.ac
│       ├── Makefile.am
│       ├── README.md
│       └── src/
│           ├── main.c
│           └── Makefile.am
├── __init__.py
├── log/
│   └── gen_autoconf.log
├── pro/
│   ├── gen_pro.py
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_autoconf_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_autoconf/badge/?version=latest)](https://gen_autoconf.readthedocs.io/projects/gen_autoconf/en/latest/?badge=latest)

More documentation and info at:
* [gen_autoconf.readthedocs.io](https://gen_autoconf.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/gen_autoconf](https://vroncevic.github.io/gen_autoconf/)

**gen_autoconf** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_autoconf/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
