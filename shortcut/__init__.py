import sys

ALLOWED_PLATFORMS = ['win32']

if sys.platform not in ALLOWED_PLATFORMS:
    raise Exception('Unsupported platform: %s' % sys.platform)

if sys.platform == 'win32':
    from .win32 import create_desktop_shortcut
    from .win32 import get_vscode_path