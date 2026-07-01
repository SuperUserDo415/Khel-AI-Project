from fastapi import FastAPI, HTTPException

from schemas import (
    RequiredRunRateRequest,
    RequiredRunRateResponse
)

from services import RequiredRunRateService

app = FastAPI(
    title="Required Run Rate API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Required Run Rate API"
    }


@app.post(
    "/required-run-rate",
    response_model=RequiredRunRateResponse
)
def required_run_rate(payload: RequiredRunRateRequest):

    result = RequiredRunRateService.calculate_required_run_rate(
        payload.match_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found."
        )

    return result