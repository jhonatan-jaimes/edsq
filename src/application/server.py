import uvicorn
from .application import app, routes


def server_run():
    app.include_router(routes)
    uvicorn.run(app, host="localhost", port=8000)

