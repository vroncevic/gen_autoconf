#!/bin/bash
#
# @brief   gen_autoconf
# @version 2.8.0
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_autoconf
pylint gen_autoconf > gen_autoconf.report
echo "Done"
