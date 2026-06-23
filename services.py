from schemas import RunRateRequest


class RunRateService:
    """
    Service class for calculating cricket run rates.
    """

    @staticmethod
    def calculate_run_rate(payload: RunRateRequest):
        current_runs = payload.current_runs
        overs = payload.overs
        balls = payload.balls
        total_overs = payload.total_overs
        target = payload.target

        total_match_balls = total_overs * 6
        balls_played = (overs * 6) + balls

        if balls_played == 0:
            current_run_rate = 0
        else:
            overs_played_decimal = balls_played / 6
            current_run_rate = current_runs / overs_played_decimal

        overs_played = balls_played / 6

        response = {
            "current_runs": current_runs,
            "overs_played": round(overs_played, 2),
            "balls_played": balls_played,
            "current_run_rate": round(current_run_rate, 2),
            "is_chasing": target is not None,
            "target": target,
            "runs_required": None,
            "balls_remaining": None,
            "overs_remaining": None,
            "required_run_rate": None,
            "message": ""
        }

        if balls_played > total_match_balls:
            raise ValueError("Balls played cannot be greater than total match balls.")

        if target is not None:
            runs_required = target - current_runs
            balls_remaining = total_match_balls - balls_played
            overs_remaining = balls_remaining / 6

            if runs_required <= 0:
                response["runs_required"] = 0
                response["balls_remaining"] = balls_remaining
                response["overs_remaining"] = round(overs_remaining, 2)
                response["required_run_rate"] = 0
                response["message"] = "Target has already been achieved."

            elif balls_remaining == 0:
                response["runs_required"] = runs_required
                response["balls_remaining"] = 0
                response["overs_remaining"] = 0
                response["required_run_rate"] = None
                response["message"] = "Innings is over. Target was not achieved."

            else:
                required_run_rate = runs_required / overs_remaining

                response["runs_required"] = runs_required
                response["balls_remaining"] = balls_remaining
                response["overs_remaining"] = round(overs_remaining, 2)
                response["required_run_rate"] = round(required_run_rate, 2)
                response["message"] = (
                    f"Team needs {runs_required} runs from {balls_remaining} balls "
                    f"at {round(required_run_rate, 2)} runs per over."
                )

        else:
            response["message"] = (
                f"Current run rate is {round(current_run_rate, 2)} runs per over."
            )

        return response
