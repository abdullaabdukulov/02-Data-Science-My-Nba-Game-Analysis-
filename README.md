# Task
What is the problem? And where is the challenge?

The task is to create a function called analyse_nba_game that takes an array of play-by-play moves in an NBA game and returns a dictionary summarizing the game. 

The challenge is to parse the play-by-play data, extract relevant information, and organize it into a structured format.


# Description
How have you solved the problem?

To solve the problem, I have implemented the analyse_nba_game function. This function takes the play_by_play_moves array as input and processes each play in the array. It parses the play information, extracts relevant data such as team names, player names, field goals (FG), field goal attempts (FGA), three-pointers made (3P), three-point attempts (3PA), free throws made (FT), free throw attempts (FTA), offensive rebounds (ORB), defensive rebounds (DRB), total rebounds (TRB), assists (AST), steals (STL), blocks (BLK), turnovers (TOV), personal fouls (PF), and points (PTS).

The function organizes the extracted data into a dictionary with the following structure:
{
    "home_team": {"name": TEAM_NAME, "players_data": DATA},
    "away_team": {"name": TEAM_NAME, "players_data": DATA}
}
where TEAM_NAME represents the name of the team, and DATA is an array of hashes representing each player's data with the format:

{
    "player_name": XXX,
    "FG": XXX,
    "FGA": XXX,
    "FG%": XXX,
    "3P": XXX,
    "3PA": XXX,
    "3P%": XXX,
    "FT": XXX,
    "FTA": XXX,
    "FT%": XXX,
    "ORB": XXX,
    "DRB": XXX,
    "TRB": XXX,
    "AST": XXX,
    "STL": XXX,
    "BLK": XXX,
    "TOV": XXX,
    "PF": XXX,
    "PTS": XXX
}



# Installation
How to install your project? npm install? make? make re?

Nothing needs to be installed in the project


# Usage
Players	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
Player00	XX	XX	.XXX	X	XX	.XXX	XX	XX	.XXX	XX	XX	XX	XX	X	X	XX	XX	XX
Totals	XX	XX	.XXX	X	XX	.XXX	XX	XX	.XXX	XX	XX	XX	XX	X	X	XX	XX	XX

