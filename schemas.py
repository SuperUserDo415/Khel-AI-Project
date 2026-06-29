from pydantic import BaseModel
from typing import List
class MatchScoreboardRequest(BaseModel):
    match_id: int

class Batter(BaseModel):
    name: str
    runs: int


class Bowler(BaseModel):
    name: str
    wickets: int


class MatchScoreboardResponse(BaseModel):
    match: str
    venue: str

    innings_number: int

    batting_team: str
    bowling_team: str

    score: str
    overs: str
    run_rate: float

    top_batter: Batter
    top_bowler: Bowler

    recent_balls: List[str]