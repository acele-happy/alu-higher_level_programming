#!/usr/bin/python3
import sys
import types

if __name__ == "__main__":
    # Import the hidden module from the .pyc file
    hidden_module = types.ModuleType("hidden_4")
    with open("hidden_4.pyc", "rb") as f:
        # Load the compiled Python code
        code = f.read()
        exec(compile(code, "hidden_4.pyc", "exec"), hidden_module.__dict__)

    # Get all names defined in the module, excluding those starting with "__"
    names = [name for name in dir(hidden_module) if not name.startswith('__')]

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)
