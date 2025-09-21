from fastapi import FastAPI, APIRouter


app = FastAPI(
    title="edsq",
    description="Api con diferentes tipos de usos",
    version="1.0.0"
)
routes = APIRouter(
    prefix="/api"
)
