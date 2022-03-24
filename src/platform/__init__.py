import sys

from src.exceptions import UnsupportedPlatformError

ALLOWED_PLATFORMS = ['win32', 'linux']

if sys.platform not in ALLOWED_PLATFORMS:
    raise UnsupportedPlatformError()

if sys.platform == 'win32':
    from .win32 import NULL_DEV
    from .win32 import VSCODEE_HOME
    from .win32 import get_vscode_path
    from .win32 import create_desktop_shortcut

if sys.platform == 'linux':
    from .linux import NULL_DEV
    from .linux import VSCODEE_HOME
    from .linux import get_vscode_path
    from .linux import create_desktop_shortcut