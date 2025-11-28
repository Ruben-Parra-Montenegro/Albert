import inspect

def get_all_tools(*modules):
    """Automatically collect all functions from the provided modules."""
    tools = []
    
    for module in modules:
        for name, obj in inspect.getmembers(module):

            # Skip if it doesn't have a docstring, some imports may not have docstrings
            
            if not obj.__doc__:
                continue
            if inspect.isfunction(obj) and not name.startswith('_'):
                tools.append(obj)
    
    return tools