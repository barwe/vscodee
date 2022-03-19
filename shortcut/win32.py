import os
from typing import Mapping
import winshell

def create_link(name: str, options: Mapping[str, any]):
    """Create a desktop link for Windows 10/11.

    Parameters
    ----------
    `name` : `str`
        Prefix of link file (after removing the `.lnk` extension).
    `options` : `Mapping[str, any]`
        Options of the object returned by `winshell.shortcut`.
    """     
    link_filepath = os.path.join(os.environ['USERPROFILE'], 'Desktop', name + '.lnk')
    with winshell.shortcut(link_filepath) as link:
        link.path = options['path']
        link.description = options['description']
        link.arguments = options['arguments']
        link.icon_location = options['icon_location']
        link.working_directory = options['working_directory']
    return link_filepath

def get_vscode_exe_path():
    # 默认安装路径
    default_path = os.path.join(os.environ['USERPROFILE'], 'AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
    if os.path.exists(default_path):
        return default_path
    else:
        raise FileNotFoundError(f'"{default_path}" not found')


create_desktop_shortcut = create_link
get_vscode_path = get_vscode_exe_path