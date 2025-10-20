import inspect

def get_all_tools(*modules):
    """Automatically collect all functions from the provided modules."""
    tools = []
    
    for module in modules:
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and not name.startswith('_'):
                tools.append(obj)
    
    return tools