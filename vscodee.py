import os
import sys
import shutil
import logging
from os import path
from argparse import ArgumentParser

from src.utils import p
from src.environment import Environment
from src.platform import create_desktop_shortcut as creator
from src.exceptions import UnsupportedPlatformError

from settings import VSCODE_ENV_DIR
from settings import PRE_EXTENSIONS

EXTENSION_KEYS = list(PRE_EXTENSIONS.keys())

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
)


# 目前只实现 windows 下的隔离
def check_platform():
    if sys.platform == 'win32':
        return True
    else:
        raise UnsupportedPlatformError()


def create(args):
    # 检查待创建的环境是否存在
    env_path = p(VSCODE_ENV_DIR, args.env_name)
    if path.exists(env_path):
        x = input('检测到该环境已存在，是否先删除该环境? (y/n): ')
        if x == 'y':
            shutil.rmtree(env_path)
        else:
            return

    env = Environment(args.env_name)
    env.create_shortcut(creator)

    extension_keys = ['base']
    for k in args.extension_keys:
        if k not in extension_keys:
            extension_keys.append(k)
    
    for k in extension_keys:
        logging.info(f'Start installing {k} extensions ...')
        print('\n'.join(f' - {x}' for x in PRE_EXTENSIONS[k]))
        success = env.install_recommended_extensions(k)
        if not success:
            logging.error('Some unexpected error occurs!')
            break
    else:
        logging.info('Done!')

    print('Now check your desktop to see if there is a wonderful shortcut on it!')



def remove(args):
    pass


def list(args):
    all_envs = os.listdir(VSCODE_ENV_DIR)
    
    # 检查某个环境
    if args.env is not None:
        env = args.env
        env_dir = p(VSCODE_ENV_DIR, env)
        # 不合法的环境名
        if env not in all_envs:
            logging.error(f'"{env}" is not in installed environments!')
            return
        print(f'Environment: {env} ({env_dir})')
        print('Extensions:')
        extensions = os.listdir(p(env_dir, 'extensions'))
        extensions = [x for x in extensions if not x.startswith('.')]
        for ext in extensions:
            print(f' - {ext}')

    else:
        print('All available environments:')
        for env in all_envs:
            print(f' - {env}')


if __name__ == '__main__':
    check_platform()

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help="管理隔离环境")

    # 创建隔离环境
    create_parser = subparsers.add_parser('create', help="创建隔离环境")
    create_parser.set_defaults(func=create)
    create_parser.add_argument('env_name', help='新的隔离环境名称')
    create_parser.add_argument(
        '-i', 
        '--install-extensions-by-keys',
        dest='extension_keys',
        nargs='+', 
        choices=EXTENSION_KEYS,
        default=['base'],
        help='按预设 keys 安装扩展, base 默认安装'
    )

    # 移除隔离环境
    remove_parser = subparsers.add_parser('remove', help="移除隔离环境")
    remove_parser.set_defaults(func=remove)

    # 列出隔离环境
    list_parser = subparsers.add_parser('list', help="列出隔离环境")
    list_parser.set_defaults(func=list)
    list_parser.add_argument('-e', '--env', help='检查某个环境，打印其基本信息')

    args = parser.parse_args()
    args.func(args)
