"""
    Routes Initialization file

    Loads all of the routes from the configuration file and register them with the appropriate controller methods

    Supports 5 http verbs (GET, POST, PUT, PATCH, DELETE)
"""
import importlib
import inspect
from types import FunctionType
from app.config.routes import routes
from app.controllers import controllers_list

def _set_route(app, route_name, pattern, controller, action, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(route_name, action), **kwargs)

_routed_methods = []
_verbs = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

def initialize_routes(app):
    """ Set up routes based on routing rules outlined in routes config file """
    for key in routes:
        """ sets up default controller, and all routes listed on the routes dictionary """
        if key == 'default_controller':
            controller = getattr(importlib.import_module('app.controllers.'+routes['default_controller']), routes['default_controller'])
            _set_route(app, 'default_index', '/', controller, 'index')
            _routed_methods.append(routes['default_controller'] + '#index')
        else:
            if key in _verbs:
                for route in routes[key]:
                    route_handler = routes[key][route].split("#", 1)
                    controller = getattr(importlib.import_module('app.controllers.'+route_handler[0]), route_handler[0])
                    _set_route(app, routes[key][route], route, controller, route_handler[1], methods=[key])
                    _routed_methods.append(routes[key][route])
            else:
                route_handler = routes[key].split("#", 1)
                controller = getattr(importlib.import_module('app.controllers.'+route_handler[0]), route_handler[0])
                _set_route(app, routes[key], key, controller, route_handler[1])
                _routed_methods.append(routes[key])
    """ Set up default routes based on controllers, their methods, and the method parameters """
    for controller_name in controllers_list:
        _controller_auto_router(app, controller_name, _routed_methods)
""" Helper function that sets up routes for a given controller excluding all methods that are listed in "routed_methods" """
def _controller_auto_router(app, controller_name, routed_methods):
    controller = getattr(importlib.import_module('app.controllers.'+controller_name), controller_name)
    methods = dict((x, inspect.getargspec(y).args) for x,y in controller.__dict__.items() if type(y) == FunctionType and not x.startswith('_'))
    for method in methods:
        if controller_name+'#'+method not in routed_methods:
            parameters = '/'.join(['<'+param+'>' for param in methods[method] if param != 'self'])
            route = '/'+controller_name.lower()
            route += '/'+method if method != 'index' else ''
            route += '/'+parameters if len(parameters) > 1 else ''
            _set_route(app, controller_name+'#'+method, route, controller, method, methods=list(_verbs))

