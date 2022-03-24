import os
from typing import Mapping

from src.exceptions import CommandNotFoundInPathError
from src.utils import p


# 输出和警告流重定向
NULL_DEV = '/dev/null 2>&1'

# 隔离环境安装位置
HOME = os.popen('echo $HOME').read().strip()
VSCODEE_HOME = f'{HOME}/.vscode/env'


def get_vscode_path():
    vscode = os.popen('which code').read().strip()
    if os.path.exists(vscode):
        return vscode
    else:
        raise CommandNotFoundInPathError('code')


def create_desktop_shortcut(name: str, options: Mapping[str, any]):
    home = os.popen('echo $HOME').read().strip()
    desktop = p(home, 'Desktop', name + '.desktop')
    content = [
        '[Desktop Entry]',
        'Name=' + name,
        f"Exec={options['path']} {options['arguments']}",
        'Icon=com.visualstudio.code',
        'Terminal=false',
        'Type=Application',
        # 'X-Deepin-Vendor=user-custom'
    ]
    
    with open(desktop, 'w') as wr:
        wr.write('\n'.join(content))
    
    return desktop