from src.application import app, routes
from src.decode import routes_decode


def run():
    routes.include_router(routes_decode)
    app.include_router(routes)


if __name__ == '__main__':
    run()
