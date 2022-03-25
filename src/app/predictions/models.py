from typing import Optional

from sqlmodel import SQLModel, Field


class Prediction(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    bs64_image: str
    result: str
    confidence: float

class PredictionCreate(SQLModel):
    bs64_image: str


class PredictionUpdate(SQLModel):
    result: str
    confidence: float