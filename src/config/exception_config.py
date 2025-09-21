from fastapi import Request
from fastapi.responses import JSONResponse
from src.application import app

@app.exception_handler(RuntimeError)
async def runtime_error_handler(request: Request, exc: RuntimeError):
    return JSONResponse(
        status_code=400,  # lo traducimos a Bad Request
        content={"detail": str(exc)}  # mensaje de error
    )

