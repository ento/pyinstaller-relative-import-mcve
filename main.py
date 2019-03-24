import os
import os.path
import sys

# This puts 'app' in PyInstaller's TOC
import app

cwd = os.getcwd()
plugins_dir = os.path.join(cwd, 'p')
sys.path.insert(0, plugins_dir)

if hasattr(sys, '_MEIPASS'):
    SYS_PREFIXLEN = len(sys._MEIPASS) + 1
    print('sys._MEIPASS', '-' * 30)
    print(sys._MEIPASS)
    print('')
else:
    SYS_PREFIXLEN = None


plugin_names = sorted(os.listdir(plugins_dir))
for d in plugin_names:
    plugin_dir = os.path.join(plugins_dir, d)
    print('importing', d, '-' * 30)
    print(plugin_dir)
    if SYS_PREFIXLEN and len(plugin_dir) > SYS_PREFIXLEN + 1:
        print('Note: This plugin path will not reproduce the import error '
              'because it\'s longer than SYS_PREFIXLEN + 1')
    print('imported', __import__(d))
    print('')
