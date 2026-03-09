from fastapi import APIRouter

router=APIRouter()

@router.get("/workout")

def generate_workout():

    workout_plan={

        "day1":["Jumping Jacks","Pushups","Squats"],

        "day2":["Running","Plank","Lunges"],

        "day3":["Rest"],

        "day4":["Burpees","Mountain Climbers"],

        "day5":["Yoga","Stretching"],

        "day6":["Cycling"],

        "day7":["Rest"]

    }

    return workout_plan