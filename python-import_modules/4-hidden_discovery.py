#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Specify the path to the .pyc file
    pyc_file = "hidden_4.pyc"
    
    # Load the compiled Python module from the .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_file)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)

    # Get all names defined in the module, excluding those starting with "__"
    names = [name for name in dir(hidden_module)
