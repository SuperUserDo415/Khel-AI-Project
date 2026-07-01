class InningsSummaryService:

    innings = {

        1: {
            "total_runs": 185,
            "wickets": 6,
            "legal_balls": 120,

            "batters": [
                {
                    "name": "Virat Kohli",
                    "runs": 82,
                    "balls": 54
                },
                {
                    "name": "Rohit Sharma",
                    "runs": 45,
                    "balls": 30
                },
                {
                    "name": "Hardik Pandya",
                    "runs": 32,
                    "balls": 20
                }
            ],

            "bowlers": [
                {
                    "name": "Mitchell Starc",
                    "wickets": 3,
                    "runs_conceded": 38,
                    "overs": "4.0"
                },
                {
                    "name": "Pat Cummins",
                    "wickets": 2,
                    "runs_conceded": 41,
                    "overs": "4.0"
                }
            ],

            "recent_balls": [
                "1",
                "4",
                "0",
                "W",
                "2",
                "6"
            ]
        }

    }

    @staticmethod
    def get_summary(innings_id):

        innings = InningsSummaryService.innings.get(innings_id)

        if innings is None:
            return None

        run_rate = innings["total_runs"] / (innings["legal_balls"] / 6)

        overs = f'{innings["legal_balls"]//6}.{innings["legal_balls"]%6}'

        top_batter = max(
            innings["batters"],
            key=lambda x: x["runs"]
        )

        top_bowler = max(
            innings["bowlers"],
            key=lambda x: x["wickets"]
        )

        return {

            "innings_id": innings_id,

            "total_runs": innings["total_runs"],

            "wickets": innings["wickets"],

            "legal_balls": innings["legal_balls"],

            "overs": overs,

            "run_rate": round(run_rate,2),

            "batter_summaries": innings["batters"],

            "bowler_summaries": innings["bowlers"],

            "top_batter": top_batter,

            "top_bowler": top_bowler,

            "recent_balls": innings["recent_balls"]

        }