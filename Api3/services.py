class MatchStateService:

    matches = {

        1: {
            "match": "India vs Australia",

            "innings_number": 2,

            "batting_team": "India",
            "bowling_team": "Australia",

            "runs": 152,
            "wickets": 3,

            "overs": 17,
            "balls": 2,

            "target": 181
        },

        2: {
            "match": "England vs Pakistan",

            "innings_number": 1,

            "batting_team": "England",
            "bowling_team": "Pakistan",

            "runs": 198,
            "wickets": 4,

            "overs": 18,
            "balls": 5,

            "target": None
        }

    }

    @staticmethod
    def get_match_state(match_id):

        match = MatchStateService.matches.get(match_id)

        if match is None:
            return None

        return {

            "match": match["match"],

            "innings_number": match["innings_number"],

            "batting_team": match["batting_team"],

            "bowling_team": match["bowling_team"],

            "score": f'{match["runs"]}/{match["wickets"]}',

            "overs": f'{match["overs"]}.{match["balls"]}',

            "wickets": match["wickets"],

            "target": match["target"]

        }