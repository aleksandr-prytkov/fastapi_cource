from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from router import router as tasks_router

# Depends дает красивые и удобные поля для редактирования в docs
# Annotated нужно прочитать обязательн


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(router=tasks_router)
