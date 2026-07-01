from pydantic import BaseModel
from typing import List


class BatterSummary(BaseModel):
    name: str
    runs: int
    balls: int


class BowlerSummary(BaseModel):
    name: str
    wickets: int
    runs_conceded: int
    overs: str


class InningsSummaryRequest(BaseModel):
    innings_id: int


class InningsSummaryResponse(BaseModel):
    innings_id: int

    total_runs: int
    wickets: int

    legal_balls: int
    overs: str

    run_rate: float

    batter_summaries: List[BatterSummary]
    bowler_summaries: List[BowlerSummary]

    top_batter: BatterSummary
    top_bowler: BowlerSummary

    recent_balls: List[str]