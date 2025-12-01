"""Agent tools package for file operations and web search."""

import inspect
from . import user_tools
from . import serpapiwrapper
# forgot to add vecor tools import but its working, wont touch for now.
# the vector tools module isnt imported here but we can use it? I will take a look at this later. I might not understand something about python packages/modules

# Automatically collect all callable functions from tool modules, so users can just add functions.

__all__ = []

for module in [user_tools, serpapiwrapper]:
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and not name.startswith('_'):
            globals()[name] = obj
            __all__.append(name)