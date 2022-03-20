import os
import logging
from os import path
from typing import Sequence

from settings import PRE_EXTENSIONS
from settings import VSCODE_ENV_DIR

from src.platform import get_vscode_path
from src.platform import NULL_DEV
from src.exceptions import EnvExistsError
from src.exceptions import DirNotFoundError
from src.utils import exec_linear_commands


class Environment:
    """为不同的开发环境或者项目隔离不同的 vscode 环境"""
    def __init__(self, env: str, open_dir: str = None):
        self.__env_name = env
        self.__env_path = f"{VSCODE_ENV_DIR}/{env}"

        self.__open_dir = open_dir
        if self.__open_dir is not None and not path.exists(self.__open_dir):
            raise DirNotFoundError(self.__open_dir)

        if not path.exists(self.__env_path):
            os.makedirs(self.__env_path)
            logging.info(f'创建新的环境目录 {self.__env_path}')
        else:
            logging.error(f'已存在环境目录 {self.__env_path}')
            raise EnvExistsError(self.__env_path)

        self.__user_data_dir = f"{self.__env_path}/data"
        logging.info(f'创建用户数据目录 {self.__user_data_dir}')
        os.mkdir(self.__user_data_dir)

        self.__extensions_dir = f"{self.__env_path}/extensions"
        logging.info(f'创建扩展存储目录 {self.__extensions_dir}')
        os.mkdir(self.__extensions_dir)

    @property
    def vscode_args(self):
        args = [
            '--user-data-dir',
            self.__user_data_dir,
            '--extensions-dir',
            self.__extensions_dir
        ]
        if self.__open_dir is not None:
            args.append(self.__open_dir)
        return args

    @property
    def shortcut_name(self):
        """快捷方式文件的名称"""
        if self.__open_dir is not None:
            return os.path.basename(self.__open_dir)
        else:
            return self.__env_name

    def create_shortcut(self, creator):
        """创建桌面快捷方式
        @param creator 根据平台不同需要使用不同的快捷方式创建器
        """
        vscode_path = get_vscode_path()
        link_filepath = creator(self.shortcut_name, {
            "path": vscode_path,
            "description": f"A vscode environment named {self.__env_name}",
            "arguments": ' '.join(self.vscode_args),
            "icon_location": ('', 0),
            "working_directory": os.path.dirname(vscode_path)
        })
        logging.info(f'创建桌面快捷方式 {link_filepath}')

    def install_extensions(self, extension_ids: Sequence[str]):
        """安装扩展"""
        cmd_list = []
        prefix = f'code --extensions-dir {self.__extensions_dir}'
        for id in extension_ids:
            cmd_list.append(f'{prefix} --install-extension {id} > {NULL_DEV}')
        return exec_linear_commands(cmd_list)


    def install_recommended_extensions(self, key: str):
        """安装预设集合中的扩展"""
        return self.install_extensions(PRE_EXTENSIONS[key])
