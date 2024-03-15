import re
import pandas as pd

data_path = "./data_2.txt"

with open(data_path, "r") as file:

    data_content = file.readlines()

all_data = {"home_team": {"name": str(), "players_data": {}},
            "away_team": {"name": str(), "players_data": {}}}


def analyse_nba_game(play_by_play_moves):
    for line in play_by_play_moves:
        global home_team, away_team, data
        data = {"player_name": str(), "FG": 0, "FGA": 0, "FG%": 0,
                "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0,
                "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0,
                "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

        line = line.split("|")
        relevant_team = line[2]
        away_team = line[3]
        home_team = line[4]
        action = line[-1]

        text = " ".join(action.split())
        find_name = re.compile(r'([A-Z]\.\s\w+)')
        search = find_name.search(text)

        if search:
            name = search.group(1)
            data["player_name"] = name

            # FG
            if "makes 2-pt" in action:
                data["FG"] += 1
                data['FGA'] += 1
                data["PTS"] += 2
            # FG
            if "makes 3-pt" in action:
                data["FG"] += 1
                data['FGA'] += 1
                data["3P"] += 1
                data["3PA"] += 1
                data["PTS"] += 3
            # FGA
            if "misses 2-pt" in action:
                data["FGA"] += 1
            if "misses 3-pt" in action:
                data["FGA"] += 1
            # FT
            if "makes free throw" in action:
                data["FT"] += 1
                data["FTA"] += 1
                data["PTS"] += 2
            # FTA
            if "misses free throw" in action:
                data["FTA"] += 1
            # ORB
            if "Offensive rebound" in action:
                data["ORB"] += 1
                data["TRB"] += 1
            # DRB
            if "Defensive rebound" in action:
                data["DRB"] += 1
                data["TRB"] += 1
            # AST
            if "assist" in action:
                # print(name)
                data["AST"] += 1
            # STL
            if "steal" in action:
                data["STL"] += 1
            # BLK
            if 'block' in action:
                data["BLK"] += 1
            # TOV
            if "Turnover" in action:
                data["TOV"] += 1

            if "Personal foul by" in action:
                data["PF"] += 1
                if relevant_team == away_team:
                    relevant_team = home_team
                else:
                    relevant_team = away_team

            if "Shooting foul by" in action:
                if relevant_team == home_team:
                    relevant_team = away_team
                else:
                    relevant_team = home_team

            if relevant_team == home_team:
                all_data["home_team"]["name"] = home_team
                if name in all_data["home_team"]["players_data"]:
                    player_stats = all_data["home_team"]["players_data"][name]
                    update(player_stats)
                else:
                    all_data["home_team"]["players_data"][name] = data.copy()
            else:
                all_data["away_team"]["name"] = away_team
                if name in all_data["away_team"]["players_data"]:
                    player_stats = all_data["away_team"]["players_data"][name]
                    update(player_stats)
                else:
                    all_data["away_team"]["players_data"][name] = data.copy()

            for k1, v1 in all_data["home_team"]["players_data"].items():
                for k, v in v1.items():
                    if k == "FG":
                        fg = v
                    if k == "FGA":
                        fga = v
                        if fg or fga > 0:
                            fg_p = round((fg/fga) * 100, 2)
                            data["FG%"] = fg_p

    return all_data

def percent(data):
    if data["FGA"] != 0:
        data["FG%"] = round((data["FG"] / data["FGA"]) * 100)
    else:
        data["FG%"] = 0

    if data["3PA"] != 0:
        data["3P%"] = round((data["3P"] / data["3PA"]) * 100)
    else:
        data["3P%"] = 0

    if data["FTA"] != 0:
        data["FT%"] = round((data["FT"] / data["FTA"]) * 100)
    else:
        data["FT%"] = 0

    return data

def update(player_stats):
    player_stats["3P"] += data["3P"]
    player_stats["FG"] += data["FG"]
    player_stats["FGA"] += data["FGA"]
    player_stats["3P"] += data["3P"]
    player_stats["3PA"] += data["3PA"]
    player_stats["FT"] += data["FT"]
    player_stats["FTA"] += data["FTA"]
    player_stats["ORB"] += data["ORB"]
    player_stats["DRB"] += data["DRB"]
    player_stats["TRB"] += data["TRB"]
    player_stats["AST"] += data["AST"]
    player_stats["STL"] += data["STL"]
    player_stats["BLK"] += data["BLK"]
    player_stats["TOV"] += data["TOV"]
    player_stats["PF"] += data["PF"]
    player_stats["PTS"] += data["PTS"]
    player_stats = percent(player_stats)

    return player_stats

analyse_nba_game(data_content)

home_df = pd.DataFrame(all_data["home_team"]["players_data"]).T.reset_index(drop=True)
away_df = pd.DataFrame(all_data["away_team"]["players_data"]).T.reset_index(drop=True)

home_team_totals = home_df.sum(axis=0)
away_team_totals = away_df.sum(axis=0)

home_team_totals["player_name"] = "Team Total"
away_team_totals["player_name"] = "Team Total"

home_df = pd.concat([home_df, pd.DataFrame(home_team_totals).T], ignore_index=True)
away_df = pd.concat([away_df, pd.DataFrame(away_team_totals).T], ignore_index=True)

print("\n")
print(f"{home_team}: HOME TEAM")
print(home_df)
print("\n")
print(f"{away_team}: AWAY_TEAM")
print(away_df)