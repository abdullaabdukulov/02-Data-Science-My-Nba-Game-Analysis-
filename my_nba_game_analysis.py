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

default_data = {"player_name": str(), "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

def analyse_nba_game(play_by_play_moves):
    global default_data
    global team
    result = {"home_team": {"name": str(), "players_data": list()}, "away_team": {"name": str(), "players_data": list()}}

    for play in play_by_play_moves:
        current_team = play[2]
        current_action = play[7]
        home_team = play[4]
        away_team = play[3]


        result['home_team']['name'] = home_team
        result['away_team']['name'] = away_team
        res =action(current_action)
        if current_team == result['home_team']['name']:
            team = 'home_team'
        else:
            team = 'away_team'
        for player in res:
            name = player[0][1]
            criteria = player[1]

            if name not in [i['player_name'] for i in result[team]['players_data']] or not result[team]['players_data']:
                default_data['player_name'] = name
                default_data[criteria] += 1
                result[team]['players_data'].append(default_data)
                default_data = dict.fromkeys(default_data.keys(), 0)

            elif name in [i['player_name'] for i in result[team]['players_data']]:
                for player_data in result[team]['players_data']:
                    if name == player_data['player_name']:
                        player_data[criteria] += 1


    print(result)





# def calculat


play = load_data('data2.txt')
analyse_nba_game(play)
