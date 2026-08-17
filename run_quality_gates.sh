#!/bin/bash
#
# @brief   gen_autoconf
# @version 2.8.0
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_autoconf
python3 gates/gates/isp_checker.py gen_autoconf
python3 gates/gates/limits_checker.py gen_autoconf
python3 gates/gates/srp_checker.py gen_autoconf

echo "Done"
