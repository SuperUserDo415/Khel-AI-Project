from fastapi import FastAPI, HTTPException

from schemas import (
    InningsSummaryRequest,
    InningsSummaryResponse
)

from services import InningsSummaryService

app = FastAPI(
    title="Innings Summary API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Innings Summary API"
    }


@app.post(
    "/innings-summary",
    response_model=InningsSummaryResponse
)
def innings_summary(payload: InningsSummaryRequest):

    result = InningsSummaryService.get_summary(
        payload.innings_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Innings not found."
        )

    return result