import sys

from src.exceptions import UnsupportedPlatformError

ALLOWED_PLATFORMS = ['win32']

if sys.platform not in ALLOWED_PLATFORMS:
    raise UnsupportedPlatformError()

if sys.platform == 'win32':
    from .win32 import create_desktop_shortcut
    from .win32 import get_vscode_path
    from .win32 import NULL_DEV