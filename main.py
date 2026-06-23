from fastapi import FastAPI, HTTPException
from schemas import RunRateRequest, RunRateResponse
from services import RunRateService

app = FastAPI(
    title="Cricket Run Rate API",
    description="API to calculate current run rate and required run rate in cricket.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Cricket Run Rate API",
        "endpoints": {
            "calculate_run_rate": "/run-rate"
        }
    }


@app.post("/run-rate", response_model=RunRateResponse)
def calculate_run_rate(payload: RunRateRequest):
    try:
        result = RunRateService.calculate_run_rate(payload)
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while calculating run rate."
        )
schemas.py 
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
