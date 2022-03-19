from fastapi import FastAPI, APIRouter

from predictions.views import router as predictions

app = FastAPI()
router = APIRouter()

@app.get('/')
def index():
    return {'status':'ok'}

router.include_router(predictions, prefix='/predict', tags=['Predictions'])
app.include_router(router)