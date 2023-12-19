import re

{"player_name": str(),  "FG%": 0,"3P%": 0,  "FT%": 0,  "TRB": 0,  "PF": 0, "PTS": 0}
def find_action(current_action):
    _3P = [re.compile(r'(.*) makes 3-pt jump shot from').search(current_action), '3P', 3]

    MIS_3P = [re.compile(r'(.*) misses 3-pt jump shot from').search(current_action), '3PA', 0]

    _2P = [re.compile(r'(.*) makes 2-pt jump shot from').search(current_action), 'FG', 2]

    MIS_2P = [re.compile(r'(.*) misses 2-pt jump shot from').search(current_action), 'FGA', 0]

    FT = [re.compile(r'(.*) makes free throw (.*) of (.*)').search(current_action), 'FT', 0]

    FTA = [re.compile(r'(.*) misses free throw (.*) of (.*)').search(current_action), 'FTA', 0]

    PF = [re.compile(r'Personal foul by (.*) \(').search(current_action), 'PF', 0]

    ORB = [re.compile(r'Offensive rebound by (.*)').search(current_action), 'ORB', 0]

    DRB = [re.compile(r'Defensive rebound by (.*)').search(current_action), 'DRB', 0]

    TOV = [re.compile(r'Turnover by (.*) \(').search(current_action), 'TOV', 0]

    BLK = [re.compile(r'block by (.*)\)').search(current_action), 'BLK', 0]

    AST = [re.compile(r'assist by (.*)\)').search(current_action), 'AST', 0]

    STL = [re.compile(r'steal by (.*)\)').search(current_action), 'STL', 0]

    PF = [re.compile(r'Personal foul by (.*) \(').search(current_action), 'FFF', 0]

    SHF = [re.compile(r'Shooting foul by (.*) \(').search(current_action), 'FFF', 0]

    OF = [re.compile(r'Offensive foul by (.*) \(').search(current_action), 'PF', 0]

    CF = [re.compile(r'Clear path foul by (.*)').search(current_action), 'FFF', 0]

    LBF = [re.compile(r'Loose ball foul by (.*) \(').search(current_action), 'PF', 0]

    Dunk = [re.compile(r"(.*) makes 2-pt dunk").search(current_action), 'FG', 2]

    TwoPLayup_missed = [re.compile(r'(.*) misses 2-pt layup').search(current_action), 'FGA', 0]

    FTClear = [re.compile(r'(.*) makes clear path free throw (.*) of (.*)').search(current_action), 'FT', 0]


    Hookshot_missed = [re.compile(r'(.*) misses 2-pt hook shot from').search(current_action), 'FGA', 0]

    HookShot = [re.compile(r'(.*) makes 2-pt hook shot from').search(current_action), 'FG', 2]

    case = [_3P, MIS_3P, _2P, MIS_2P, FT, FTA, PF, ORB, DRB, TOV, BLK, AST, STL, PF, SHF, OF, CF, LBF, Dunk, TwoPLayup_missed, FTClear, Hookshot_missed, HookShot]

    return [i for i in case if i[0]]
