import uvicorn
from . import app
from src.encode import routes_encode
from src.decode import routes_decode


def server_run():
    app.include_router(routes_encode)
    app.include_router(routes_decode)
    uvicorn.run(app, host="localhost", port=8000)

