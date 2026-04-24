import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI


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
    await app.state.dishka_container.close()
    logger.info("Приложение остановлено.")


app = FastAPI(title="smart bookmark", lifespan=lifespan)
