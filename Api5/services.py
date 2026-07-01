class WinProbabilityService:

    matches = {

        1: {
            "match": "India vs Australia",
            "batting_team": "India",
            "bowling_team": "Australia",

            "runs": 152,
            "wickets": 3,

            "overs": 17,
            "balls": 2,

            "target": 181,
            "total_overs": 20
        },

        2: {
            "match": "England vs Pakistan",
            "batting_team": "Pakistan",
            "bowling_team": "England",

            "runs": 140,
            "wickets": 7,

            "overs": 18,
            "balls": 0,

            "target": 181,
            "total_overs": 20
        }

    }

    @staticmethod
    def get_probability(match_id):

        match = WinProbabilityService.matches.get(match_id)

        if match is None:
            return None

        total_balls = match["total_overs"] * 6
        balls_played = (match["overs"] * 6) + match["balls"]

        balls_remaining = total_balls - balls_played

        runs_needed = match["target"] - match["runs"]

        if balls_remaining <= 0:
            required_rr = 0
        else:
            required_rr = (runs_needed * 6) / balls_remaining

        # Simple heuristic model
        if required_rr <= 6:
            probability = 90
        elif required_rr <= 8:
            probability = 75
        elif required_rr <= 10:
            probability = 60
        elif required_rr <= 12:
            probability = 40
        else:
            probability = 20

        if probability >= 75:
            label = "High"
        elif probability >= 50:
            label = "Medium"
        else:
            label = "Low"

        return {

            "match": match["match"],

            "batting_team": match["batting_team"],
            "bowling_team": match["bowling_team"],

            "current_score": f'{match["runs"]}/{match["wickets"]}',

            "target": match["target"],

            "balls_remaining": balls_remaining,

            "required_run_rate": round(required_rr, 2),

            "win_probability": probability,

            "label": label

        }