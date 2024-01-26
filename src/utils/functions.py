import os
import sys
from importlib import import_module

sys.path.insert(1, os.getcwd() + r"\src")

def import_list(directory: str, deletion: list = None) -> list:
    items = []
    with os.scandir(os.path.join(sys.path[1], directory)) as iterator:
        for item in iterator:
            if not item.is_dir() and item.name not in deletion:
                name_ = f'{item.name[:-3]}'
                items.append(import_module(f'{directory}.{name_}'))
    return items