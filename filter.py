import re
def action(current_action):
    _3P = (re.compile(r'(.*) makes 3-pt jump shot from').search(current_action), '3PT')

    MIS_3P = (re.compile(r'(.*) misses 3-pt jump shot from').search(current_action), '3PA')

    _2P = (re.compile(r'(.*) makes 2-pt jump shot from').search(current_action), 'FG')

    MIS_2P = (re.compile(r'(.*) misses 2-pt jump shot from').search(current_action), 'FGA')

    FT = (re.compile(r'(.*) makes free throw (.*) of (.*)').search(current_action), 'FT')

    FTA = (re.compile(r'(.*) misses free throw (.*) of (.*)').search(current_action), 'FTA')

    PF = (re.compile(r'Personal foul by (.*) \(').search(current_action), 'PF')

    ORB = (re.compile(r'Offensive rebound by (.*) \(').search(current_action), 'ORB')

    DRB = (re.compile(r'Defensive rebound by (.*) \(').search(current_action), 'DRB')

    TOV = (re.compile(r'Turnover by (.*) \(').search(current_action), 'TOV')

    BLK = (re.compile(r'block by (.*)').search(current_action), 'BLK')

    AST = (re.compile(r'assist by (.*)').search(current_action), 'AST')

    STL = (re.compile(r'steal by (.*)').search(current_action), 'STL')

    PF = (re.compile(r'Personal foul by (.*)').search(current_action), 'PF')

    SHF = (re.compile(r'Shooting foul by (.*)').search(current_action), 'SHF')

    OF = (re.compile(r'Offensive foul by (.*)').search(current_action), 'OF')

    CF = (re.compile(r'Clear path foul by (.*)').search(current_action), 'CF')

    LBF = (re.compile(r'Loose ball foul by (.*)').search(current_action), 'LBF')

    Dunk = (re.compile(r"(.*) makes 2-pt dunk").search(current_action), 'FG')

    TwoPLayup_missed = (re.compile(r'(.*) misses 2-pt layup').search(current_action), 'FGA')

    FTClear = (re.compile(r'(.*) makes clear path free throw (.*) of (.*)').search(current_action), 'FT')


    Hookshot_missed = (re.compile(r'(.*) misses 2-pt hook shot from').search(current_action), 'FGA')

    HookShot = (re.compile(r'(.*) makes 2-pt hook shot from').search(current_action), 'FG')

    case = [_3P, MIS_3P, _2P, MIS_2P, FT, FTA, PF, ORB, DRB, TOV, BLK, AST, STL, PF, SHF, OF, CF, LBF, Dunk, TwoPLayup_missed, FTClear, Hookshot_missed, HookShot]

    return [i for i in case if i[0] is not None]