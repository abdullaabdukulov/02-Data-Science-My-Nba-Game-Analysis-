import csv
import re


def find_data(current_action):
    actions = [
        (re.compile(r'([\S]. [\S]*) makes (\d)-pt jump shot from'), "FG"),
        (re.compile(r'([\S]. [\S]*) makes (\d)-pt layup'), "FG"),
        (re.compile(r'([\S]. [\S]*) makes (\d)-pt dunk'), "FG"),
        (re.compile(r'([\S]. [\S]*) misses (\d)-pt jump shot from'), "FGA"),
        (re.compile(r'([\S]. [\S]*) misses (\d)-pt layup'), "FGA"),
        (re.compile(r'([\S]. [\S]*) makes clear path free throw (.*) of (.*)'), "FT"),
        (re.compile(r'([\S]. [\S]*) misses free throw (.*) of (.*)'), "FTA"),
        (re.compile(r'([\S]. [\S]*) makes (\d)-pt hook shot'), "FG"),
        (re.compile(r'([\S]. [\S]*) misses (\d)-pt hook shot'), "FGA"),
        (re.compile(r'Turnover by ([\S]. [\S]*[^) ])'), "TOV"),
        (re.compile(r'assist by ([\S]. [\S]*[^) ])'), "AST"),
        (re.compile(r'steal by ([\S]. [\S]*[^) ])'), "STL"),
        (re.compile(r'block by ([\S]. [\S]*)[^) ]'), "BLK"),
        (re.compile(r'([\S]. [\S]*) makes (\d)-pt (3-pt )?jump shot from'), "3P"),
        (re.compile(r'([\S]. [\S]*) misses (\d)-pt (3-pt )?jump shot from'), "3PA"),
        (re.compile(r'Offensive rebound by ([\S]+\. [\S]*)'), "ORB"),
        (re.compile(r'Defensive rebound by ([\S]+\. [\S]*)'), "DRB"),
        (re.compile(r'(Personal|Shooting|Offensive|Clear path|Louse ball) foul by ([\S]+\. [\S]*[^) ])'), "PF")
    ]

    re_data = [(action[0].search(current_action), action[1]) for action in actions]
    return [a for a in re_data if a[0] is not None]



def load_data(data):
    with open(data, 'r') as data_file:
        csv_reader = csv.reader(data_file, delimiter='|')
        return [row for row in csv_reader]


players_data = []


def analyse_nba_game(play_by_play_moves):
    for row in play_by_play_moves:
        actions = find_data(row[-1])
        if len(actions) > 0:
            for movement in actions:
                player_name = movement[0][1]
                point_field = movement[1]
                if player_name not in [i["player_name"] for i in players_data]:
                    players_data.append(
                        {"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0,
                         "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0,
                         "PF": 0, "PTS": 0, "is_home_team": row[2] == row[4]})
                index = next(i for i, player in enumerate(players_data) if player["player_name"] == player_name)
                players_data[index][point_field] += 1
                if point_field not in ("STL", "BLK", "PF"):
                    players_data[index]["is_home_team"] = row[2] == row[4]
                else:
                    players_data[index]["is_home_team"] = row[2] != row[4]


def calculate(players_data):
    for player in players_data:
        player["3PA"] += player["3P"]
        player["FGA"] += player["FG"] + player["3PA"]
        player["FG"] += player["3P"]
        player["FTA"] += player["FT"]
        player["TRB"] = player["ORB"] + player["DRB"]
        player["FG%"] = "{:.3f}".format(round(player["FG"] / player["FGA"], 3)) if player["FGA"] != 0 else 0
        player["FT%"] = "{:.3f}".format(round(player["FT"] / player["FTA"], 3)) if player["FTA"] != 0 else 0
        player["3P%"] = "{:.3f}".format(round(player["3P"] / player["3PA"], 3)) if player["3PA"] != 0 else 0
        player["PTS"] = 2 * (player["FG"] - player["3P"]) + 3 * player["3P"] + player["FT"]


def print_nba_game_stats(team_dict):
    for team in team_dict.values():
        fg, fga, fgp, p3, p3a, p3p, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tov, pf, pts = 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        print(
            f'{"Players name":<17}|{"FG":<5}|{"FGA":<5}|{"FG%":<6}|{"3P":<5}|{"3PA":<5}|{"3P%":<6}|{"FT":<5}|{"FTA":<5}|{"FT%":<6}|{"ORB":<5}|{"DRB":<5}|{"TRB":<5}|{"AST":<5}|{"STL":<5}|{"BLK":<5}|{"TOV":<5}|{"PF":<5}|{"PTS":<5}')
        for player in team["players_data"]:
            print(
                f'{player["player_name"]:<17}|{player["FG"]:<5}|{player["FGA"]:<5}|{player["FG%"]:<6}|{player["3P"]:<5}|{player["3PA"]:<5}|{player["3P%"]:<6}|{player["FT"]:<5}|{player["FTA"]:<5}|{player["FT%"]:<6}|{player["ORB"]:<5}|{player["DRB"]:<5}|{player["TRB"]:<5}|{player["AST"]:<5}|{player["STL"]:<5}|{player["BLK"]:<5}|{player["TOV"]:<5}|{player["PF"]:<5}|{player["PTS"]:<5}')
            fg += player["FG"]
            fga += player["FGA"]
            p3a += player["3PA"]
            fta += player["FTA"]
            drb += player["DRB"]
            stl += player["STL"]
            tov += player["TOV"]
            pts += player["PTS"]
            fgp = player["FG%"]
            p3p = player["3P%"]
            ftp = player["FT%"]
            trb = player["TRB"]
            p3 += player["3P"]
            ft += player["FT"]
            orb += player["ORB"]
            ast += player["AST"]
            blk += player["BLK"]
            pf += player["PF"]
        print(
            f'{"Team totals":<17}|{fg:<5}|{fga:<5}|{fgp:<6}|{p3:<5}|{p3a:<5}|{p3p:<6}|{ft:<5}|{fta:<5}|{ftp:<6}|{orb:<4} |{drb:<5}|{trb:<5}|{ast:<5}|{stl:<5}|{blk:<5}|{tov:<5}|{pf:<5}|{pts:<5}\n\n')


def main():
    play_by_play_moves = load_data("nba_game_warriors_thunder_20181016.txt")
    analyse_nba_game(play_by_play_moves)
    calculate(players_data)

    away_team = play_by_play_moves[0][3]
    home_team = play_by_play_moves[0][4]

    result = {"home_team": {"name": home_team, "players_data": []},
              "away_team": {"name": away_team, "players_data": []}}

    for player in players_data:
        if player["is_home_team"]:
            result["home_team"]["players_data"].append(player)
        else:
            result["away_team"]["players_data"].append(player)

    print_nba_game_stats(result)


if __name__ == "__main__":
    main()
