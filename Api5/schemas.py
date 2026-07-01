from pydantic import BaseModel


class WinProbabilityRequest(BaseModel):
    match_id: int


class WinProbabilityResponse(BaseModel):
    match: str
    batting_team: str
    bowling_team: str
    current_score: str
    target: int
    balls_remaining: int
    required_run_rate: float
    win_probability: int
    label: str