import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.routes.user import router as user

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Приложение запущено.")
    yield
    logger.info("Приложение остановлено.")


app = FastAPI(title="smart bookmark", lifespan=lifespan)
app.include_router(user, prefix="/api/v1")