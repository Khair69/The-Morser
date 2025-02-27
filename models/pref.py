import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = ""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        # Go up one folder from models to the project root
        base_path = os.path.dirname(os.path.dirname(__file__))

    return os.path.join(base_path, relative_path)