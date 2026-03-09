from fastapi import APIRouter

router=APIRouter()

@router.get("/meal-plan")

def meal_plan():

    meals={

        "breakfast":"Oats with fruits",

        "lunch":"Dal Rice with salad",

        "dinner":"Paneer roti",

        "snack":"Nuts and fruits"

    }

    return meals