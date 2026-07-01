from pydantic import BaseModel


class RequiredRunRateRequest(BaseModel):
    match_id: int


class RequiredRunRateResponse(BaseModel):
    match: str
    target: int
    current_score: str
    runs_needed: int
    balls_remaining: int
    required_run_rate: float