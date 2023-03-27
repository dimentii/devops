from falcon.asgi import App

from .endpoints.products import ProductsEndpoint


def create_app() -> App:
    app = App(middleware=[])

    app.add_route('/products', ProductsEndpoint())

    return app
