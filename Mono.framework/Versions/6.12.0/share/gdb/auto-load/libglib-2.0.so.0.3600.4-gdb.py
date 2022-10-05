import sys
import gdb

# Update module path.
dir_ = '/Library/Frameworks/Mono.framework/Versions/6.12.0/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from glib import register
register (gdb.current_objfile ())
