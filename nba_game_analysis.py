from filter import get_info
import pandas as pd

data = {"home_team": {"name": str(), "players_data": list()}, "away_team": {"name": str(), "players_data": list()}}


def load_data():
    result = pd.read_csv('Blazers vs Lakers.txt', sep='|',
                         names=['Time', 'Second', 'Relevant Team', 'Away Team', 'Home team', 'Point1', 'Point2',
                                'Action'])

    return result


reverse_team = []


def extract(team):
    df = pd.DataFrame(team)
    all_act = df['Action'].tolist()
    result = []
    for i in all_act:
        a = get_info(i)
        if a:
            for j in a:
                if j[1] in ['STL', 'BLK', 'PF']:
                    reverse_team.append([j[0][1], j[1]])
                else:
                    result.append([j[0][1], j[1]])

    return result


def calculation(m, team):
    global data
    pl_name = []
    players_data = []

    for p in range(len(m)):
        player_name = m[p][0]

        if player_name not in pl_name:
            pl_name.append(player_name)
            players_data.append(
                {"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0,
                 "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0,
                 "PTS": 0, m[p][1]: 1})

        elif player_name in pl_name:
            indx = pl_name.index(player_name)
            players_data[indx][m[p][1]] += 1

    data[team]['players_data'] = players_data


def set_players(play_by):
    teams = play_by['Relevant Team'].unique()
    first_team = play_by[play_by['Relevant Team'] == teams[0]]
    second_team = play_by[play_by['Relevant Team'] == teams[-1]]

    data['home_team']['name'] = play_by['Home team'][0]
    data['away_team']['name'] = play_by['Away Team'][0]

    team_1 = extract(first_team)
    team_2 = extract(second_team)

    if teams[0] == data['home_team']['name']:
        calculation(team_1, 'home_team')

    if teams[0] == data['away_team']['name']:
        calculation(team_1, 'away_team')

    if teams[-1] == data['home_team']['name']:
        calculation(team_2, 'away_team')

    if teams[-1] == data['away_team']['name']:
        calculation(team_2, 'away_team')


def convert_to_table(team, team_name):
    global df
    """This function turns players data to table"""
    df = pd.DataFrame(
        data[team]['players_data'],
        index=[name['player_name'] for name in data[team]['players_data']]
    )
    df = df.iloc[0:, 1:]
    df = df.drop('Team')
    for i in reverse_team:
        if i[0] in df.index:
            df.loc[i[0], i[1]] += 1

    team_result = {"FG": df.FG.sum(), "FGA": df.FGA.sum(), "FG%": '%.3f' % df['FG%'].mean(), "3P": df['3P'].sum(),
                   "3PA": df['3PA'].sum(), "3P%": '%.3f' % df['3P%'].mean(), "FT": df.FT.sum(), "FTA": df.FTA.sum(),
                   "FT%": '%.3f' % df['FT%'].mean(), "ORB": df.ORB.sum(), "DRB": df.DRB.sum(), "TRB": df.TRB.sum(),
                   "AST": df.AST.sum(), "STL": df.STL.sum(), "BLK": df.BLK.sum(), "TOV": df.TOV.sum(),
                   "PF": df.PF.sum(),
                   "PTS": df.PTS.sum()}

    team_result = [float(val) for val in team_result.values()]
    df.loc['Team Totals', :] = team_result

    df.FGA += df.FG
    df['3PA'] += df['3P']
    df.FTA += df.FT
    df.TRB = df.ORB + df.DRB
    df.PTS = df.FG + df['3PA']

    df['FG%'] = (df['FG'] / df['FGA']) * 100
    df['3P%'] = (df['3P'] / df['3PA']) * 100
    df['FT%'] = (df.FT / df.FTA) * 100

    df = df.fillna(0)
    df = df.astype(int)

    print(
        ' ' * 20,
        f"This is the result of {team_name} team\n\n",
        df,
        '\n\n'
    )


def my_nba_analysis():
    k = load_data()
    set_players(k)
    convert_to_table('home_team', data['home_team']['name'])
    convert_to_table('away_team', data['away_team']['name'])


my_nba_analysis()
