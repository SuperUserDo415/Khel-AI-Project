class MatchScoreboardService:

    matches = {

        1: {
            "match": "India vs Australia",
            "venue": "Wankhede Stadium",

            "innings_number": 2,

            "batting_team": "India",
            "bowling_team": "Australia",

            "runs": 152,
            "wickets": 3,

            "overs": 17,
            "balls": 2,

            "top_batter": {
                "name": "Virat Kohli",
                "runs": 68
            },

            "top_bowler": {
                "name": "Mitchell Starc",
                "wickets": 2
            },

            "recent_balls": [
                "1",
                "4",
                "W",
                "0",
                "6",
                "2"
            ]
        },

        2: {
            "match": "England vs Pakistan",
            "venue": "Lord's",

            "innings_number": 1,

            "batting_team": "England",
            "bowling_team": "Pakistan",

            "runs": 210,
            "wickets": 5,

            "overs": 25,
            "balls": 4,

            "top_batter": {
                "name": "Joe Root",
                "runs": 92
            },

            "top_bowler": {
                "name": "Shaheen Afridi",
                "wickets": 3
            },

            "recent_balls": [
                "0",
                "1",
                "4",
                "6",
                "2",
                "1"
            ]
        }

    }

    @staticmethod
    def get_scoreboard(match_id: int):

        match = MatchScoreboardService.matches.get(match_id)

        if match is None:
            return None

        total_balls = (match["overs"] * 6) + match["balls"]

        run_rate = round(
            match["runs"] / (total_balls / 6),
            2
        )

        return {

            "match": match["match"],

            "venue": match["venue"],

            "innings_number": match["innings_number"],

            "batting_team": match["batting_team"],

            "bowling_team": match["bowling_team"],

            "score": f'{match["runs"]}/{match["wickets"]}',

            "overs": f'{match["overs"]}.{match["balls"]}',

            "run_rate": run_rate,

            "top_batter": match["top_batter"],

            "top_bowler": match["top_bowler"],

            "recent_balls": match["recent_balls"]
        }