class RequiredRunRateService:

    matches = {

        1: {
            "match": "India vs Australia",
            "runs": 152,
            "wickets": 3,
            "overs": 17,
            "balls": 2,
            "target": 181,
            "total_overs": 20
        },

        2: {
            "match": "England vs Pakistan",
            "runs": 198,
            "wickets": 4,
            "overs": 18,
            "balls": 5,
            "target": 220,
            "total_overs": 20
        }

    }

    @staticmethod
    def calculate_required_run_rate(match_id):

        match = RequiredRunRateService.matches.get(match_id)

        if match is None:
            return None

        total_balls = match["total_overs"] * 6

        balls_played = (match["overs"] * 6) + match["balls"]

        balls_remaining = total_balls - balls_played

        runs_needed = match["target"] - match["runs"]

        if runs_needed < 0:
            runs_needed = 0

        if balls_remaining == 0:
            required_rr = 0
        else:
            required_rr = (runs_needed * 6) / balls_remaining

        return {

            "match": match["match"],

            "target": match["target"],

            "current_score": f'{match["runs"]}/{match["wickets"]}',

            "runs_needed": runs_needed,

            "balls_remaining": balls_remaining,

            "required_run_rate": round(required_rr,2)

        }