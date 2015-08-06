"""
    Routes Initialization file

    Loads all of the routes from the configuration file and register them with the appropriate controller methods

    Supports 5 http verbs (GET, POST, PUT, PATCH, DELETE)
"""
import importlib
from app.config.routes import routes

def _set_route(app, route_name, pattern, controller, action, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(route_name, action), **kwargs)

def initialize_routes(app):
    verbs = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')
    for key in routes:
        if key == 'default_controller':
            controller = getattr(importlib.import_module('app.controllers.'+routes['default_controller']), routes['default_controller'])
            _set_route(app, 'default_index', '/', controller, 'index')
        else:
            if key in verbs:
                for route in routes[key]:
                    route_handler = routes[key][route].split("#", 1)
                    controller = getattr(importlib.import_module('app.controllers.'+route_handler[0]), route_handler[0])
                    _set_route(app, routes[key][route], route, controller, route_handler[1], methods=[key])
            else:
                route_handler = routes[key].split("#", 1)
                controller = getattr(importlib.import_module('app.controllers.'+route_handler[0]), route_handler[0])
                _set_route(app, routes[key], key, controller, route_handler[1])

