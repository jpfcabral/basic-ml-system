from fastapi import APIRouter

from predictions.models import PredictionCreate

router = APIRouter()

@router.post('/')
def run_prediction(pred: PredictionCreate):
    ## TODO: create run function
    return {'to':'do'}