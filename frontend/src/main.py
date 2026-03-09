from fastapi import FastAPI
from .routers import user_router,workout_router,nutrition_router
from .database import Base,engine

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(user_router.router)
app.include_router(workout_router.router)
app.include_router(nutrition_router.router)


@app.get("/")
def home():

    return {"message":"ArogyaMitra API Running"}