from fastapi import FastAPI, HTTPException
from schemas import MatchScoreboardRequest, MatchScoreboardResponse
from services import MatchScoreboardService

app = FastAPI()

@app.post("/match-scoreboard", response_model=MatchScoreboardResponse)
def match_scoreboard(payload: MatchScoreboardRequest):
    result = MatchScoreboardService.get_scoreboard(payload.match_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Match not found.")

    return result