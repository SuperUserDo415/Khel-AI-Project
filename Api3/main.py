from fastapi import FastAPI, HTTPException

from schemas import (
    MatchStateRequest,
    MatchStateResponse
)

from services import MatchStateService

app = FastAPI(
    title="Match State API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Match State API"
    }


@app.post(
    "/match-state",
    response_model=MatchStateResponse
)
def match_state(payload: MatchStateRequest):

    result = MatchStateService.get_match_state(
        payload.match_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found."
        )

    return result