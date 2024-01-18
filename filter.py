import re


def get_info(current_action):
    P3 = [re.compile(r'(.*) makes 3-pt jump shot from').search(current_action), '3P']

    P2 = [re.compile(r'(.*) makes 2-pt jump shot from').search(current_action), 'FG']

    TOV = [re.compile(r'Turnover by (.*) \(').search(current_action), 'TOV']

    ORB = [re.compile(r'Offensive rebound by (.*)').search(current_action), 'ORB']

    DRB = [re.compile(r'Defensive rebound by (.*)').search(current_action), 'DRB']

    AST = [re.compile(r'assist by (.*)\)').search(current_action), 'AST']

    Miss3P = [re.compile(r'(.*) misses 3-pt jump shot from').search(current_action), '3PA']

    Miss2P = [re.compile(r'(.*) misses 2-pt jump shot from').search(current_action),'FGA']

    STL = [re.compile(r'steal by (.*)\)').search(current_action),'STL']

    FreeThrow = [re.compile(r'(.*) makes free throw ').search(current_action), 'FT']

    MisFreeThrow = [re.compile(r'(.*) misses free throw ').search(current_action), 'FTA']

    PF = [re.compile(r'Personal foul by (.*) \(').search(current_action), 'PF']

    ShoutingFoul = [re.compile(r'Shouting foul by (.*) \(').search(current_action), 'PF']

    BLK = [re.compile(r'block by (.*)\)').search(current_action), 'BLK']

    OffFoul = [re.compile(r'Offensive foul by (.*) \(').search(current_action), 'PF']

    LayUp = [re.compile(r'(.*) makes 2-pt layup').search(current_action),'FG']

    Dunk = [re.compile(r'(.*) makes 2-pt dunk').search(current_action), 'FG']

    MisLayUp = [re.compile(r'(.*) misses 2-pt layup').search(current_action), 'FGA']

    LooseBallFoul = [re.compile(r'Loose ball foul by (.*) \(').search(current_action), 'PF']

    FTClear = [re.compile(r'(.*) makes clear path free throw (.*) of (.*)').search(current_action), 'FT']

    Hookshot_missed = [re.compile(r'(.*) misses 2-pt hook shot from').search(current_action), 'FGA']

    HookShot = [re.compile(r'(.*) makes 2-pt hook shot from').search(current_action), 'FG']

    re_data = [P3, P2, TOV, ORB, DRB, AST, Miss3P,  Miss2P, STL, FreeThrow, MisFreeThrow, PF, ShoutingFoul, BLK, OffFoul, LayUp, Dunk, MisLayUp, LooseBallFoul, FTClear, Hookshot_missed, HookShot]
    d = [i for i in re_data if i[0]]
    if d:
        if d[0][0]:
            return d

