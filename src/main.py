import uvicorn
from fastapi import FastAPI
# from rich import print

from utils.import_routers import all_routers


app = FastAPI(
    title="Тест API"
)

for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
