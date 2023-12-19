import pandas as pd
import csv
from filters import find_action

def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        for row in csvreader:
            result.append(row)
    return result


default_data = {"player_name": str(), "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0,
                "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

result = {"home_team": {"name": str(), "players_data": list()}, "away_team": {"name": str(), "players_data": list()}}


def update_data(name, team, action, point):
    """This function updates the main data with players data"""
    global default_data
    players_data = result[team]['players_data']

    if name not in [i['player_name'] for i in players_data] or not players_data:
        """This condition is adding new dict to  main data when player data not in main data"""
        default_data['player_name'] = name
        default_data[action] += 1
        default_data['PTS'] += point
        players_data.append(default_data)
        # print(result[team]['players_data'])

        """After adding data the values of default data will be equal to 0"""
        default_data = dict.fromkeys(default_data.keys(), 0)

    elif name in [i['player_name'] for i in players_data]:
        """This condition updates the player data in main data"""
        for player_data in players_data:
            if name == player_data['player_name']:
                player_data[action] += 1
                player_data['PTS'] += point
    return


def calculate(filtered_data, status):
    """This function calculates some avarage of critiries in data and replaces it with original"""
    adding = {
        'FGA': ['FG', 'FGA'],
        '3PA': ['3P', '3PA'],
        'FTA': ['FT', 'FTA'],
        'TRB': ['ORB', 'DRB']
    }
    divition = {
        'FG%': ['FG', 'FGA'],
        '3P%': ['3P', '3PA'],
        'FT%': ['FT', 'FTA']
    }

    lenght = len(filtered_data[status]['players_data'])
    option = filtered_data[status]['players_data']
    for index in range(lenght):
        for key in option[index]:

            if key in adding.keys():
                option[index][key] = option[index][adding[key][0]] + option[index][adding[key][1]]

            elif key in divition.keys():
                try:
                    option[index][key] = float('%.3f' % (option[index][divition[key][0]] / option[index][divition[key][1]]))
                except ZeroDivisionError:
                    continue

    return result


def sort_data(data):
    """this function filters and sorts some criteries in players data"""

    for action in data:
        current_team = action[2]
        current_action = action[7]
        result['home_team']['name'] = action[4]
        result['away_team']['name'] = action[3]

        response = find_action(current_action)


        for player in response:
            name = player[0][1]
            criteria = player[1]
            point = player[-1]

            if current_team == result['home_team']['name']:
                if criteria != 'STL' and criteria != 'FFF' and criteria != 'BLK':
                    update_data(name, 'home_team', criteria, point)

                elif criteria == 'STL' or criteria == 'BLK':
                    update_data(name, 'away_team', criteria, point)

                elif criteria == 'FFF':
                    update_data(name, 'away_team', 'PF', point)


            else:
                if criteria != 'STL' and criteria != 'FFF' and criteria != 'BLK':
                    update_data(name, 'away_team', criteria, point)

                elif criteria == 'STL' or criteria == 'BLK':
                    update_data(name, 'home_team', criteria, point)

                elif criteria == 'FFF':
                    update_data(name, 'home_team', 'PF', point)


def conver_to_table(data, team, team_name):
    """This function turns players data to table"""
    df = pd.DataFrame(
        data[team]['players_data'],
        index=[name['player_name'] for name in result[team]['players_data']]
    )
    df = df.iloc[0:, 1:]
    df = df.drop('Team')

    team_result = {"FG": df.FG.sum(), "FGA": df.FGA.sum(), "FG%": '%.3f' % df['FG%'].mean(), "3P": df['3P'].sum(),
                "3PA": df['3PA'].sum(), "3P%": '%.3f' % df['3P%'].mean(), "FT": df.FT.sum(), "FTA": df.FTA.sum(),
                "FT%": '%.3f' % df['FT%'].mean(), "ORB": df.ORB.sum(), "DRB": df.DRB.sum(), "TRB": df.TRB.sum(),
                "AST": df.AST.sum(), "STL": df.STL.sum(), "BLK": df.BLK.sum(), "TOV": df.TOV.sum(), "PF": df.PF.sum(),
                "PTS": df.PTS.sum()}

    team_result = [float(val) for val in team_result.values()]
    df.loc['Team Totals', :] = team_result

    print(
        ' '*20,
        f"This is the result of {team_name} team\n\n",
        df,
        '\n\n'
    )

