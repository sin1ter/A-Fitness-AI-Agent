from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    VERY_ACTIVE = "very_active"
    ATHLETIC = "athletic"

class FitnessGoal(str, Enum):
    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"
    ENDURANCE = "endurance"
    STRENGTH = "strength"

class FitnessProfile(BaseModel):
    age: int
    weight: float
    height: float
    gender: str
    activity_level: ActivityLevel
    fitness_goal: FitnessGoal
    dietary_restrictions: List[str] = []
    injuries: List[str] = []
    preferred_workout_time: str
    available_equipment: List[str] = []
    workout_days_per_week: int

class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    rest_time: int = Field(..., description="Rest time in seconds")

class Meal(BaseModel):
    name: str
    calories: str
    protien: str
    carbs: str
    fats: float
    timing: str = Field(..., description="breakfast, lunch, dinner, snack")

class FitnessReportResult(BaseModel):
    workout_plan: List[Exercise] = Field(description="Customized workout plan")
    meal_plan: List[Meal] = Field(description="Daily Meal Plan")
    daily_calories: int = Field(description="Recommended daily caloric intake")
    macros: dict = Field(description="Recommened macro split(protin, carbs, fat)")
    tips: List[str] = Field(description="Personalized fitness and nutritions tips")
    weekly_schedule: dict = Field(description="Weekly workout and meal plan")
    motivational_quote: str = Field(description="Motivational Quote")

