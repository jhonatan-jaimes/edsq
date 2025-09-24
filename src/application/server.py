import uvicorn
from . import app
from src.encode import routes_encode
from src.decode import routes_decode
from src.short import routes_short


def server_run():
    app.include_router(routes_encode)
    app.include_router(routes_decode)
    app.include_router(routes_short)
    uvicorn.run(app, host="localhost", port=8000)

