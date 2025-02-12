# For Data Validations
from pydantic import BaseModel, EmailStr


class UserAdd(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone_number: str


class UserOut(BaseModel):
    name: str
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PasswordReset(BaseModel):
    email: str
    code: int
    new_password: str
    confirm_password: str


class UpdateRestaurant(BaseModel):
    restaurant_name: str
    restaurant_email: str
    phone_number: str
    rating: float


class UpdateFood(BaseModel):

    kind: str
    price: float
    cook_time: int
    food_name: str
    description: str
    rating: float
    restaurant_id: int


class RestaurantWorkTimeAdd(BaseModel):
    restaurant_id: str
    day_of_week: str
    opening_time: str
    closing_time: str


class AddCard(BaseModel):
    card_number: int
    card_valid_thru: str
    card_name: str
    card_cvv: int




class UpdateDrink(BaseModel):

    kind: str
    price: float
    drink_name: str
    description: str
    restaurant_id: int