"""
    System Core Router File

    Defines the route function to make it easier for users to set up routes
"""
def route(app, route_name, pattern, controller, action, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(route_name, action), **kwargs)
