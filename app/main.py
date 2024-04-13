from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.api.v1.todos import todo
from app.core.config import settings

description_txt = """
FASTAPI TODO API Demo
"""

app = FastAPI(title="todo demo",
              openapi_url="/openapi.json",
              description=description_txt,
              version=settings.API_VERSION,
              contact=settings.CONTACT,
              terms_of_service="https://www.ktechhub.com1/",
              )
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse("/docs")


@app.get("/ready", status_code=status.HTTP_200_OK, include_in_schema=True)
async def ready() -> str:
    return "ready"


app.include_router(
    todo.router,
    prefix="/api/v1",
    tags=["todos"]
)
