from os import path
import logging
import os
import shutil
import sys
from argparse import ArgumentParser

from environment import Environment

from shortcut import create_desktop_shortcut as creator

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
)

def main(args):

    # 检查环境保存目录
    if 'VSCODE_ENV_DIR' not in os.environ.keys():
        if sys.platform == 'win32':
            os.environ['VSCODE_ENV_DIR'] = 'D:/.vscode/env'
        else:
            raise Exception(f'Unsupport platform: {sys.platform}')

    # 检查待创建的环境是否存在
    env_dir = os.environ['VSCODE_ENV_DIR']
    env_path = path.join(env_dir, args.env_name)
    if path.exists(env_path):
        x = input('检测到该环境已存在，是否先删除该环境? (y/n): ')
        if x == 'y':
            shutil.rmtree(env_path)
        else:
            return

    # 创建新的环境
    env = Environment(args.env_name)
    env.create_shortcut(creator)
    env.install_recommended_extensions('base')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('env_name', help='环境名称')
    # parser.add_argument('-p', '--project', default=None, help='项目名称')
    args = parser.parse_args()
    main(args)
