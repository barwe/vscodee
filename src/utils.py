import logging
import subprocess
from pathlib import Path
from typing import  Sequence

def _exec_by_subprocess(cmd: str) -> int:
    return subprocess.run(cmd, shell=True).returncode == 0

def exec_linear_commands(cmd_list: Sequence[str], use_error_intercept = True):
    """线性执行命令行指令

    Args:
        cmd_list (Sequence[str]): 指令列表
        use_error_intercept (bool, optional): 当首次执行出错时结束任务. Defaults to True.

    Returns:
        List[int]: 是否执行成功
    """    
    for cmd in cmd_list:
        if _exec_by_subprocess(cmd):
            logging.info(f'{cmd}')
        else:
            logging.error(f'{cmd}')
            if use_error_intercept:
                return False
    return True


def p(*parts: Sequence[str]) -> str:
    return Path('/'.join(parts)).as_posix()


class Table:
    def __init__(self, rows, columns, header=None, show_title=True) -> None:
        self.rows = rows
        self.columns = columns
        self.header = header
        self.show_title = show_title
        self.total_width = None
        self.calc_width()

    def calc_width(self):
        """计算每列的宽度和总宽度"""
        total_width = 0
        for d in self.columns:
            if 'width' not in d.keys():
                d['width'] = max([len(r[d['key']]) for r in self.records])
            total_width += d['width']
        self.total_width = total_width

    def draw(self):
        ds = self.columns
        tw = self.total_width

        lines = []
        # 有大标题时
        if self.header is not None:
            hw = tw + len(ds) - 1
            # 顶线
            lines.append('┌' + '─' * hw + '┐')
            # 大标题
            lines.append('│' + '{:{}}'.format(self.header, tw) + '│')

            # lines.append('┌' + '┬'.join('─' * d['width'] for d in ds) + '┐')

        print('\n'.join(lines))


