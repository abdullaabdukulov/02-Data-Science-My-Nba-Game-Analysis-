# 02-Data Science My Nba Game Analysis



<hr>
<p>We have caught all the <code>play_by_play</code> happening during a <code>NBA</code> game so we have a flow of data and we want to create a nice array of hash which will sum everything.</p>
<h1>Part I</h1>
<p>Create a function <code>analyse_nba_game(play_by_play_moves)</code> which receives an array of play and will return a dictionary summary of the game.</p>
<p>Each play follow this format:</p>
<pre class=" language-plain"><code class=" language-plain">PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
</code></pre>
<p>They are ordered by time.</p>
<p>The return dictionary (hash) will have this format:</p>
<pre class=" language-plain"><code class=" language-plain">{"home_team": {"name": TEAM_NAME, "players_data": DATA}, "away_team": {"name": TEAM_NAME, "players_data": DATA}}
DATA will be an array of hashes with this format:
{"player_name": XXX, "FG": XXX, "FGA": XXX, "FG%": XXX, "3P": XXX, "3PA": XXX, "3P%": XXX, "FT": XXX, "FTA": XXX, "FT%": XXX, "ORB": XXX, "DRB": XXX, "TRB": XXX, "AST": XXX, "STL": XXX, "BLK": XXX, "TOV": XXX, "PF": XXX, "PTS": XXX}
</code></pre>
<p>Percent are on 100.
Player is a string everything else are integers.</p>
<p><strong>Example00</strong></p>
<pre class=" language-plain"><code class=" language-plain">1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)
1|703.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by P. George (bad pass)
1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)
1|673.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Adams misses 2-pt jump shot from 12 ft
1|671.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Offensive rebound by D. Schröder
1|667.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|P. George misses 3-pt jump shot from 26 ft
1|665.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Defensive rebound by K. Durant
1|657.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|K. Durant makes 2-pt layup from 2 ft
1|638.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|D. Schröder misses 2-pt jump shot from 14 ft
1|636.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Offensive rebound by D. Schröder
1|623.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|S. Adams misses 2-pt layup from 3 ft (block by K. Durant)
1|621.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Defensive rebound by D. Green
1|618.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|Turnover by D. Green (out of bounds lost ball)
1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|2|5|P. Patterson makes 2-pt layup from 2 ft (assist by S. Adams)
1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|2|5|Shooting foul by D. Green (drawn by P. Patterson)
1|608.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|5|P. Patterson makes free throw 1 of 1
1|598.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|D. Jones makes 2-pt dunk from 1 ft (assist by D. Green)
1|581.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|P. Patterson misses 2-pt hook shot from 8 ft
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|Offensive rebound by P. Patterson
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|3|7|Shooting foul by K. Thompson (drawn by P. Patterson)
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson makes free throw 1 of 2
1|580.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson misses free throw 2 of 2
1|580.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by D. Green
1|569.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|D. Green misses 3-pt jump shot from 28 ft
1|567.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by D. Schröder
1|552.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|P. Patterson misses 2-pt jump shot from 16 ft
1|551.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Defensive rebound by S. Curry
1|547.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Turnover by S. Curry (bad pass; steal by P. George)
1|542.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|7|Turnover by S. Adams (bad pass; steal by K. Durant)
1|533.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|10|K. Thompson makes 3-pt jump shot from 26 ft (assist by D. Green)
</code></pre>
<h1>Part II</h1>
<p>Create a <code>print_nba_game_stats(team_dict)</code> function which will a dictionary with <code>name</code> and <code>players_data</code> will print it with the following format (each column is separated by a tabulation (' ')):</p>
<pre class=" language-plain"><code class=" language-plain">HEADER
FOR PLAYER IN PLAYERS
PLAYER
TOTAL
</code></pre>
<p><strong>Example 00</strong></p>
<pre class=" language-plain"><code class=" language-plain">Players	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
Player00	XX	XX	.XXX	X	XX	.XXX	XX	XX	.XXX	XX	XX	XX	XX	X	X	XX	XX	XX
Totals	XX	XX	.XXX	X	XX	.XXX	XX	XX	.XXX	XX	XX	XX	XX	X	X	XX	XX	XX
</code></pre>
<p><strong>Example 01</strong></p>
<pre class=" language-plain"><code class=" language-plain">Players	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
Kevin Durant	9	21	.429	0	5	.000	9	10	.900	1	7	8	6	1	1	3	4	27
Stephen Curry	11	20	.550	5	9	.556	5	5	1.000	0	8	8	9	1	0	3	4	32
Klay Thompson	5	20	.250	1	8	.125	3	3	1.000	1	3	4	0	0	0	2	3	14
Draymond Green	1	6	.167	0	1	.000	0	0		1	12	13	5	3	0	6	3	2
Damian Jones	6	7	.857	0	0		0	0		2	1	3	2	0	3	2	4	12
Kevon Looney	5	11	.455	0	0		0	0		8	2	10	2	1	2	1	4	10
Shaun Livingston	3	5	.600	0	0		0	0		2	1	3	1	1	0	1	2	6
Quinn Cook	1	2	.500	1	1	1.000	0	0		1	1	2	1	0	0	2	2	3
Andre Iguodala	1	2	.500	0	1	.000	0	0		0	2	2	2	0	0	0	0	2
Jordan Bell	0	0		0	0		0	0		1	1	2	0	0	1	0	1	0
Jonas Jerebko	0	0		0	0		0	0		0	3	3	0	0	0	1	2	0	0
Alfonzo McKinnie	0	1	.000	0	1	.000	0	0		0	0	0	0	0	0	0	0	0
Team Totals	42	95	.442	7	26	.269	17	18	.944	17	41	58	28	7	7	21	29	108
</code></pre>
<p><strong>Tips</strong>
What abbreviations like <code>TRB</code> means?
As data scientist, immersion inside your dataset is key and I think you can easily google it :-)
(Google: trb meaning nba)</p>
<p>Example data files:</p>
<ul>
<li>
<p><a href="https://storage.googleapis.com/qwasar-public/nba_game_warriors_thunder_20181016.txt" target="_blank">Warriors vs Thunders (16/10/2018)</a></p>
</li>
<li>
<p><a href="https://storage.googleapis.com/qwasar-public/nba_game_blazers_lakers_20181018.txt" target="_blank">Blazers vs Lakers (18/10/2018)</a></p>
</li>
</ul>


## Instalation
**For using this project you need to install required packages below using this command on your terminal**

```bash
    pip install -r requirements.txt
```

## Usage
First of all you need to clone this repo

```bash
    # use this command on your terminal
    https://github.com/ahrorhaidarov/02-Data-Science-My-Nba-Game-Analysis-.git
```

Then run `the_my_nba_game_analysis.py` file

```bash
    # use this command on your terminal
    python the_my_nba_game_analysis.py
```

