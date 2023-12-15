import re
import csv
from filters import action
def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            result.append(row)
    return result

def is_away_team(away_team, current_team):
    return away_team == current_team


def analyse_nba_game(play_by_play_moves):
    data_away = {"player_name": str(), "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
    data_home = {"player_name": str(), "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
    result = {"home_team": {"name": str(), "players_data": data_home}, "away_team": {"name": str(), "players_data": data_away}}

    for play in play_by_play_moves:
        current_team = play[2]
        current_action = play[7]
        home_team = play[4]
        away_team = play[3]


        result['home_team']['name'] = home_team
        result['away_team']['name'] = away_team
        res =action(current_action)
        # print(res)
        if res:
            if str(current_team) == result['home_team']['name']:
                data_home['player_name'] = res[0][0][1]
                data_home[res[0][1]] += 1


            elif current_team == result['away_team']['name']:
                data_away['player_name'] = res[0][0][1]
                data_away[res[0][1]] += 1
    print(result)

# def calculat


play = load_data('data.txt')
analyse_nba_game(play)



