import re
import csv
from filters import find_action


def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            result.append(row)
    return result


def is_away_team(away_team, current_team):
    return away_team == current_team


default_data = {"player_name": str(), "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0,
                "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

result = {"home_team": {"name": str(), "players_data": list()}, "away_team": {"name": str(), "players_data": list()}}


def update_data(name, team, action):
    """This function updates the main data with players data"""
    global default_data
    players_data = result[team]['players_data']

    if name not in [i['player_name'] for i in players_data] or not players_data:
        """This condition is adding new dict to  main data when player data not in main data"""

        default_data['player_name'] = name
        default_data[action] += 1
        players_data.append(default_data)

        """After adding data the values of default data will be equal to 0"""
        default_data = dict.fromkeys(default_data.keys(), 0)

    elif name in [i['player_name'] for i in players_data]:
        """This condition updates the player data in main data"""
        for player_data in players_data:
            if name == player_data['player_name']:
                player_data[action] += 1







def analyse_nba_game(data):
    global team

    for action in data:
        current_team = action[2]
        current_action = action[7]
        result['home_team']['name'] = action[4]
        result['away_team']['name'] = action[3]

        response = find_action(current_action)

        if current_team == result['home_team']['name']:
            team = 'home_team'
        else:
            team = 'away_team'

        for player in response:
            name = player[0][1]
            criteria = player[1]

            update_data(name, team, criteria)

    print(result)


play = load_data('data2.txt')
analyse_nba_game(play)
