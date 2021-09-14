import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url1='https://sports.yahoo.com/nfl/stats/'
url2="https://www.footballoutsiders.com/stats/nfl/team-defense/2019"
url3="https://www.cbssports.com/nfl/stats/player/passing/nfl/postseason/qualifiers/?sortdir=descending&sortcol=yds"
csv1 ="data.csv"
csv21 ="nba.csv"

# cbssports_url_passing="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
# cbssports_passing_data=pd.read_html(cbssports_url_passing)
# team_dvoa_def_dfs  = pd.read_html(url3)
# dfs=data.csv
def csvScrap():
        dfs=pd.read_csv(csv21)
        # print(type(dfs))
        # print(dfs.columns)
        for col in dfs.columns.values:
            print(col )
            print()
            # print(dfs[col])






# print(team_dvoa_def_dfs)
# print(type(team_dvoa_def_dfs[0]))
# print(f'Total tables: {len(team_dvoa_def_dfs)}')
# len(team_dvoa_def_dfs)

# for table in  team_dvoa_def_dfs:
#         print("type {}: ".format(type(table)))
#
#         print(table.iloc[0])
#

def main():
    # csvScrap()
    cbssports_url_passing="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
    cbssports_passing_data=pd.read_html(cbssports_url_passing)
    data = cbssports_passing_data
    context = {}
    context["source"] = "www.cbssports.com"

    df = pd.concat(data)
    new_columns = []
    for line in df.columns.values:
        line_list = line.split()
        new_columns.append("".join(line_list[:1]))

    df.columns = new_columns
    players = df["Player"].to_list()
    teams=[]
    pp=[]
    names = []
    for player in players:
        pline = player.split()

        if "RB" in pline[4:]:
            # print(pline[4:])
            print()

        first_name = " ".join(pline[4:6])
        names.append(first_name)
        pp.append(first_name)
        position = pline[6]
        team = pline[7]
        teams.append(team)
        df["Player"] = df["Player"].replace(player,first_name)
    df.insert(1, "POS", "QB")
    df.insert(2,"Team",teams)
    context["Players"] = names
    attempts = df["ATT"]
    cmps = df["CMP"]
    # plt.plot(pp[:6],cmps[:6])
    # plt.show()
    # x = np.median(cmps)
    # std=np.std(cmps)
    # var=np.var(cmps)
    # print(x,std,var)
    print(context)






main()
