import logging
import subprocess
from pathlib import Path
from typing import  Sequence

def _exec_by_subprocess(cmd: str) -> int:
    return subprocess.run(cmd, shell=True, timeout=5).returncode == 0

def exec_linear_commands(cmd_list: Sequence[str], use_error_intercept = True):
    """线性执行命令行指令

    Args:
        cmd_list (Sequence[str]): 指令列表
        use_error_intercept (bool, optional): 当首次执行出错时结束任务. Defaults to True.

    Returns:
        List[int]: 是否执行成功
    """    
    for cmd in cmd_list:
        try:
            if _exec_by_subprocess(cmd):
                logging.info(f'{cmd}')
            else:
                logging.error(f'{cmd}')
                if use_error_intercept:
                    return False
        except subprocess.TimeoutExpired as e:
            logging.error('Timeout')
    return True


def p(*parts: Sequence[str]) -> str:
    return Path('/'.join(parts)).as_posix()
