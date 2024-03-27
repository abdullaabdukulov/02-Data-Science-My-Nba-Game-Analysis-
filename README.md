# Description
{"home_team": {"name": TEAM_NAME, "players_data": DATA}, "away_team": {"name": TEAM_NAME, "players_data": DATA}}
DATA will be an array of hashes with this format:
{"player_name": XXX, "FG": XXX, "FGA": XXX, "FG%": XXX, "3P": XXX, "3PA": XXX, "3P%": XXX, "FT": XXX, "FTA": XXX, 
"FT%": XXX, "ORB": XXX, "DRB": XXX, "TRB": XXX, "AST": XXX, "STL": XXX, "BLK": XXX, "TOV": XXX, "PF": XXX, "PTS": XXX}


# Task
We have caught all the play_by_play happening during a NBA game so we have a flow of data and we want to create a nice 
array of hash which will sum everything.
Create a print_nba_game_stats(team_dict) function which will a dictionary with name and players_data will print it 
with the following format (each column is separated by a tabulation (' ')):


# Installation
git clone "link"
pip freeze > requirements.txt

# Usage
pip install -r requirements.txt
We have to run nba_game_analysis.py file in order to check this project is working very well or not

