from .functions import import_list


all_routers = [i.router for i in import_list('api', [])]
