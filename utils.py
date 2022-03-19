import logging
import os
from typing import Sequence


def exec_linear_commands(cmd_list: Sequence[str]):
    for cmd in cmd_list:
        code = os.system(cmd)
        if code == 0:
            logging.info(f'Success: {cmd}')
        else:
            logging.error(f'Error: {cmd}')