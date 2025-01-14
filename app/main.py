# FastAPI
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Database and models
from database import engine, check_connection
from models.models import Base


# Routers
from api.andpoints.food import food_router
from api.andpoints.favorite_foods import favorite_foods_router
from api.andpoints.restaurant import restaurant_router
from api.andpoints.favorite_restaurants import favorite_restaurants_router
from api.andpoints.restaurant_work_time import restaurant_work_time_router
from api.auth.auth import auth_router
from api.auth.forgot_password import forgot_router
from api.andpoints.cards import card_router
from api.andpoints.drinks import drink_router


Base.metadata.create_all(bind=engine)
check_connection()

app = FastAPI()

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "OK"})


app.include_router(food_router)
app.include_router(favorite_foods_router)
app.include_router(restaurant_router)
app.include_router(favorite_restaurants_router)
app.include_router(restaurant_work_time_router)
app.include_router(drink_router)
app.include_router(auth_router)
app.include_router(forgot_router)
app.include_router(card_router)
