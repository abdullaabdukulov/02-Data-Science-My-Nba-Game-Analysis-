from functions import load_data, sort_data, calculate, conver_to_table, result
from filters import find_action

def my_nba_analysis(filename):
    global result

    play = load_data(filename)
    sort_data(play)

    result = calculate(result, 'home_team')
    result = calculate(result, 'away_team')

    conver_to_table(result, 'home_team', result['home_team']['name'])
    conver_to_table(result, 'away_team', result['away_team']['name'])

my_nba_analysis('Warriors vs Thunders.txt')