import pandas as pd
import re

def loading(file_name):
    result = pd.read_csv(file_name, sep="|", names=["PERIOD", "REMAINING SEC", "RELEVANT TEAM", "AWAY TEAM", "HOME TEAM", "AWAY SCORE", "HOME SCORE", "DESCRIPTION"])
    result.rename(columns={"AWAY TEAM": "AWAY_TEAM", "HOME TEAM": "HOME_TEAM"}, inplace=True)
    return result


def analyse_nba_game(play_by_play_moves):
    actions = {
        'FG': r'(.*) makes 2-pt ',
        'FGA': r'(.*) misses 2-pt ',
        '3P': r'(.*) makes 3-pt ',
        '3PA': r'(.*) misses 3-pt ',
        'FT': r'(.*) makes free throw ',
        'FTA': r'(.*) misses free throw ',
        'ORB': r'Offensive rebound by (.*)',
        'DRB': r'Defensive rebound by (.*)',
        'AST': r'assist by (.*)\)',
        'STL': r'steal by (.*)\)',
        'PF': r' foul by (.*) \(',  
        'BLK': r'block by (.*)\)',
        'TOV': r'Turnover by (.*) \(',
    }

    player_data_home = {}
    player_data_away = {}

    for index, row in play_by_play_moves.iterrows():
        desc = row['DESCRIPTION']
        relevant_team = row['RELEVANT TEAM']
        home_team_name = row['HOME_TEAM']
        away_team_name = row['AWAY_TEAM']
        
        for action, pattern in actions.items():
            match = re.compile(pattern).search(desc)
            if match:
                player_name = match.group(1)
                if relevant_team == home_team_name:
                    player_data = player_data_home
                elif relevant_team == away_team_name:
                    player_data = player_data_away
                else:
                    continue
                
                if player_name not in player_data:
                    player_data[player_name] = {
                        'player_name': player_name,
                        'FG': 0, 'FGA': 0, '3P': 0, '3PA': 0, 'FT': 0, 'FTA': 0,
                        'ORB': 0, 'DRB': 0, 'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0,
                        'PF': 0, 'PTS': 0,  
                    }
                
                player_data[player_name][action] += 1
                
                if action in ['FG', '3P', 'FT', 'AST']:  
                    player_data[player_name]['PTS'] += 2 if action == 'FG' else 3 if action == '3P' else 1

    for player_stats in player_data_home.values():
        player_stats['FG%'] = player_stats['FG'] / player_stats['FGA'] * 100 if player_stats['FGA'] != 0 else 0
        player_stats['3P%'] = player_stats['3P'] / player_stats['3PA'] * 100 if player_stats['3PA'] != 0 else 0
        player_stats['FT%'] = player_stats['FT'] / player_stats['FTA'] * 100 if player_stats['FTA'] != 0 else 0
        player_stats['TRB'] = player_stats['ORB'] + player_stats['DRB']

    for player_stats in player_data_away.values():
        player_stats['FG%'] = player_stats['FG'] / player_stats['FGA'] * 100 if player_stats['FGA'] != 0 else 0
        player_stats['3P%'] = player_stats['3P'] / player_stats['3PA'] * 100 if player_stats['3PA'] != 0 else 0
        player_stats['FT%'] = player_stats['FT'] / player_stats['FTA'] * 100 if player_stats['FTA'] != 0 else 0
        player_stats['TRB'] = player_stats['ORB'] + player_stats['DRB']

    home_team_data = {"name": play_by_play_moves.iloc[0]['HOME_TEAM'], "players_data": list(player_data_home.values())}
    away_team_data = {"name": play_by_play_moves.iloc[0]['AWAY_TEAM'], "players_data": list(player_data_away.values())}

    return {"home_team": home_team_data, "away_team": away_team_data}


def print_nba_game_stats(team_dict):
    players_data = team_dict["players_data"]
    stats_keys = ['FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

    print("Players\t\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tORB\tDRB\tTRB\tAST\tSTL\tBLK\tTOV\tPF\tPTS")

    for player in players_data:
        print("{}\t{}\t{}\t{:.1f}\t{}\t{}\t{:.1f}\t{}\t{}\t{:.1f}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            player["player_name"], player["FG"], player["FGA"], player["FG%"], player["3P"], player["3PA"],
            player["3P%"], player["FT"], player["FTA"], player["FT%"], player["ORB"], player["DRB"],
            player["TRB"], player["AST"], player["STL"], player["BLK"], player["TOV"], player["PF"],
            player["PTS"]
        ))

    total_stats = {stat: sum(player[stat] for player in players_data) for stat in stats_keys}
    print("Team Totals\t{}\t{}\t{:.1f}\t{}\t{}\t{:.1f}\t{}\t{}\t{:.1f}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
        total_stats["FG"], total_stats["FGA"], total_stats["FG%"], total_stats["3P"], total_stats["3PA"],
        total_stats["3P%"], total_stats["FT"], total_stats["FTA"], total_stats["FT%"], total_stats["ORB"],
        total_stats["DRB"], total_stats["TRB"], total_stats["AST"], total_stats["STL"], total_stats["BLK"],
        total_stats["TOV"], total_stats["PF"], total_stats["PTS"]
    ))

lists = loading("nba_game_blazers_lakers_20181018.txt")
game_summary = analyse_nba_game(lists)

print("Home Team:")
print_nba_game_stats(game_summary["home_team"])
print("\nAway Team:")
print_nba_game_stats(game_summary["away_team"])

