import sys

class EnvExistsError(Exception):
    '''要创建的环境已经存在'''
    pass

class DirNotFoundError(Exception):
    '''未找到指定目录'''
    pass

class UnsupportedPlatformError(Exception):
    '''不支持的操作系统'''
    def __init__(self, *args: object) -> None:
        super().__init__(sys.platform)
