### Reproducing the import error
Requires python3 in the path.

```
make run
```

This will install PyInstaller in a virtualenv, run it against `main.py`, and execute the resulting binary. The output will look like

```
...
dist/main/main
sys._MEIPASS ------------------------------
/home/entoentotto/workspace/pyinstaller-test/dist/main

importing plugin_0_longer_than_dist_main ------------------------------
/home/entoentotto/workspace/pyinstaller-test/p/plugin_0_longer_than_dist_main
Note: This plugin path will not reproduce the import error because it's longer than SYS_PREFIXLEN + 1
imported <module 'plugin_0_longer_than_dist_main' from '/home/entoentotto/workspace/pyinstaller-test/p/plugin_0_longer_than_dist_main/__init__.py'>

importing plugin_1 ------------------------------
/home/entoentotto/workspace/pyinstaller-test/p/plugin_1
Traceback (most recent call last):
  File "main.py", line 29, in <module>
    print('imported', __import__(d))
  File "/home/entoentotto/workspace/pyinstaller-test/p/plugin_1/__init__.py", line 1, in <module>
    from .app import hook
ImportError: cannot import name 'hook'
[12617] Failed to execute script main
Makefile:7: recipe for target 'run' failed
make: *** [run] Error 255
```

## Debugging

`make debug` will show you that running `main.py` directly suceeds without an issue.

Add `import pdb; pdb.set_trace()` as `p/plugin_1/__init__.py`'s very first line to see how PyInstaller's `FrozenImporter` handles the import:

```
(Pdb) import sys                                                                                    
(Pdb) b sys.meta_path[2].find_spec 
(Pdb) c
```
