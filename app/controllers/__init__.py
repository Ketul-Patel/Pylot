import importlib
import os

controllers_list = []
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py':
        continue
    elif module[-3:] != '.py':
        continue
    controllers_list.append("{}".format(module[:-3]))
