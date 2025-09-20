from fastapi import FastAPI, APIRouter


class Application:
    def __init__(self):
        self.app = FastAPI(
            title="edsq",
            description="Api con diferentes tipos de usos",
            version="1.0.0"
        )
        self.routes = APIRouter(
            prefix="/api"
        )


application = Application()
app = application.app
routes = application.routes
