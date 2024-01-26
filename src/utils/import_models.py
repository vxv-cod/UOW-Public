import os
import sys
from .functions import import_list
from rich import print

models_import = import_list('models', [])
# items = [i.models_classes for i in models_import]
# all_models_classes = [g for i in items for g in i]
# print(f"{all_models_classes = }")


all_models_classes = []

for module in models_import:
    for name in dir(module):
        value = getattr(module, name)
        if isinstance(value, type) and value.__module__ == module.__name__:
            all_models_classes.append(value)
# print(f'import_models == {all_models_classes = }')





# import models
# all_models_classes = []
# # module = sys.modules['models']
# package = sys.modules['models']
# # print(f'import == {module.__name__ = }')
# for name in dir(package):
#     module = getattr(package, name)
#     # Проверяем наличие атрибута __name__ и сравниваем его с дочерним элементом
#     if hasattr(module, '__name__'):
#         for name in dir(module):
#             value = getattr(module, name)
#             if isinstance(value, type) and value.__module__ == module.__name__:
#                 all_models_classes.append(value)
# print(f'888888888 == {all_models_classes = }')
# print(f'{sys.modules = }')
