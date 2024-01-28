# 02-Data Science My Nba Game Analysis

## Task

The project aims to perform analysis on NBA game data, extracting player statistics and team totals from play-by-play moves.

## Description

The provided script processes a CSV file containing play-by-play moves in an NBA game. It uses regular expressions to identify different actions (e.g., shots, rebounds, fouls) performed by players and accumulates statistics for each player and team. The calculated statistics include field goals (FG), field goal attempts (FGA), three-pointers (3P), three-point attempts (3PA), free throws (FT), free throw attempts (FTA), offensive rebounds (ORB), defensive rebounds (DRB), assists (AST), steals (STL), blocks (BLK), turnovers (TOV), personal fouls (PF), and total points (PTS). The script then prints out the analyzed statistics for each player and team.

## Installation

The script does not have explicit installation requirements. It assumes the presence of a CSV file containing NBA play-by-play data named "nba_game_warriors_thunder_20181016.txt" in the same directory. The script can be run using the command:

```
./python my_nba_game_analysis.py
```

Ensure that you have Python installed on your system.

## Usage

1. Place the CSV file with NBA play-by-play data in the same directory as the script.
2. Run the script using the provided command.
3. The script will process the data, calculate player and team statistics, and print the results.