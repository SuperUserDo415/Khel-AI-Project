from fastapi import FastAPI, HTTPException

from schemas import (
    WinProbabilityRequest,
    WinProbabilityResponse
)

from services import WinProbabilityService

app = FastAPI(
    title="Win Probability Label API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Win Probability Label API"
    }


@app.post(
    "/win-probability",
    response_model=WinProbabilityResponse
)
def win_probability(payload: WinProbabilityRequest):

    result = WinProbabilityService.get_probability(
        payload.match_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found."
        )

    return result