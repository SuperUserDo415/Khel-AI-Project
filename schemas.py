from pydantic import BaseModel, Field
from typing import Optional


class RunRateRequest(BaseModel):
    current_runs: int = Field(..., ge=0, description="Runs scored by the batting team so far")
    wickets_lost: Optional[int] = Field(None, ge=0, le=10, description="Wickets lost so far")

    overs: int = Field(..., ge=0, description="Completed overs")
    balls: int = Field(..., ge=0, le=5, description="Balls in the current over, from 0 to 5")

    total_overs: int = Field(..., gt=0, description="Total overs in the match, e.g. 20 or 50")
    
    itarget : Optional[int] = Field(
        None, gt=0, 
        description="Imaginary target score for first team. Example: If the first team score 180, they can defend this target easily.")
    
    target: Optional[int] = Field(
        None,
        gt=0,
        description="Target score for chasing team. Example: if first team made 180, target is 181"
    )


class RunRateResponse(BaseModel):
    current_runs: int
    overs_played: float
    balls_played: int

    current_run_rate: float

    is_chasing: bool

    target: Optional[int] = None
    runs_required: Optional[int] = None
    balls_remaining: Optional[int] = None
    overs_remaining: Optional[float] = None
    required_run_rate: Optional[float] = None

    message: str
