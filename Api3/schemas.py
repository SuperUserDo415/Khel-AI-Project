from pydantic import BaseModel
from typing import Optional


class MatchStateRequest(BaseModel):
    match_id: int


class MatchStateResponse(BaseModel):
    match: str
    innings_number: int

    batting_team: str
    bowling_team: str

    score: str
    overs: str
    wickets: int

    target: Optional[int] = None