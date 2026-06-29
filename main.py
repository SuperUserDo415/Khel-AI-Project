from fastapi import FastAPI, HTTPException
from services import MatchScoreboardService

app = FastAPI(
    title="Match Scoreboard API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Match Scoreboard API"
    }

@app.get("/match-scoreboard/{match_id}")
def get_scoreboard(match_id: int):

    result = MatchScoreboardService.get_scoreboard(match_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found."
        )

    return result