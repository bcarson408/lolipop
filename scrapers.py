import json
import os.path as path
from json.decoder import JSONDecodeError
import csv
import pandas as pd
import re


class CBSScapper():
    """main scrapper for fantasypros."""

    def __init__(self,csv_file):
        pass

    def cbs_sports_scraper(self):
        cbssports_url_passing="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
        cbssports_passing_data=pd.read_html(cbssports_url_passing)
        data = cbssports_passing_data
        context = {}
        context["source"] = "www.cbssports.com"
        df = pd.concat(data)
        cbs = cbs_sports_data_frame_cleaner(df)
        return cbs

    def cbs_sports_data_frame_cleaner(self,df):
        print("cbs_sports_data_frame_cleaner")
        new_columns = []
        for line in df.columns.values:
            line_list = line.split()
            new_columns.append("".join(line_list[:1]))
        df.columns = new_columns
        print(df["Player"].to_list())
        players = df["Player"].to_list()
        teams=[]
        pp=[]
        names = []
        for player in players:
            pline = player.split()
            if "RB" in pline[4:]:
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
        return df



    def csvScrap(self):
            dfs=pd.read_csv(csv_file)
            return dfs

    def open_csv(self):
        with open(self.csv_file, newline='') as csv_f:
            reader = csv.reader(csv_f)

            def cbs_sports_data_frame_cleaner(df):
                print("cbs_sports_data_frame_cleaner")
                # print(df)
                new_columns = []
                for line in df.columns.values:
                    # print(line)
                    line_list = line.split()
                    # print("list_list:",line_list)
                    # print("".join(line_list[:1]))
                    # print()
                    new_columns.append("".join(line_list[:1]))
                df.columns = new_columns
                # print(df.columns)
                print(df["Player"].to_list())
                players = df["Player"].to_list()
                # print(players)
                teams=[]
                pp=[]
                names = []
                for player in players:
                    pline = player.split()
                    if "RB" in pline[4:]:
                        # print(pline[4:])
                        print()
                    first_name = " ".join(pline[4:6])
                    # print(first_name)
                    names.append(first_name)
                    pp.append(first_name)
                    position = pline[6]
                    team = pline[7]
                    teams.append(team)
                    df["Player"] = df["Player"].replace(player,first_name)
                df.insert(1, "POS", "QB")
                df.insert(2,"Team",teams)
                # # context["Players"] = names
                # attempts = df["ATT"]
                # cmps = df["CMP"]
                return df

            def cbs_sports_scraper():
                cbssports_url_passing="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
                cbssports_passing_data=pd.read_html(cbssports_url_passing)
                data = cbssports_passing_data
                context = {}
                context["source"] = "www.cbssports.com"
                df = pd.concat(data)
                cbs = cbs_sports_data_frame_cleaner(df)
                return cbs

# csv_file1= "/Users/bcarson/Desktop/scraper/fantasy_football_projects_/2017/football_outsiders_stats_nfl_rb_2017.csv"
# csv_files = "*csv$"

class FantasyProsScrapper():
    pass



def csvScrap():
        dfs=pd.read_csv(csv_file1)
        # print(type(dfs))
        # print(dfs.columns)
        # print(dfs)
        # for col in dfs.columns.values:
        #     print(col )
        #     print()
        #     # print(dfs[col])
        return dfs

def open_csv():
    with open(csv_file1, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        # print(spamreader)
        # for row in spamreader:
        #     print(row)

def cbs_sports_data_frame_cleaner(df):
    print("cbs_sports_data_frame_cleaner")
    # print(df)
    new_columns = []
    for line in df.columns.values:
        # print(line)
        line_list = line.split()
        # print("list_list:",line_list)
        # print("".join(line_list[:1]))
        # print()
        new_columns.append("".join(line_list[:1]))
    df.columns = new_columns
    # print(df.columns)
    print(df["Player"].to_list())
    players = df["Player"].to_list()
    # print(players)
    teams=[]
    pp=[]
    names = []
    for player in players:
        pline = player.split()
        if "RB" in pline[4:]:
            # print(pline[4:])
            print()
        first_name = " ".join(pline[4:6])
        # print(first_name)
        names.append(first_name)
        pp.append(first_name)
        position = pline[6]
        team = pline[7]
        teams.append(team)
        df["Player"] = df["Player"].replace(player,first_name)
    df.insert(1, "POS", "QB")
    df.insert(2,"Team",teams)
    # # context["Players"] = names
    # attempts = df["ATT"]
    # cmps = df["CMP"]
    return df

def cbs_sports_scraper():
    cbssports_url_passing="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
    cbssports_passing_data=pd.read_html(cbssports_url_passing)
    data = cbssports_passing_data
    context = {}
    context["source"] = "www.cbssports.com"
    df = pd.concat(data)
    cbs = cbs_sports_data_frame_cleaner(df)
    return cbs

def tranform_colums(df,new_columns):
    df = df[[ "Rank","Player","Team","Bye","POS","ESPN","RTSports","Fantrax","FFC"]+new_columns+["FL"]]
    return df

def fantasypros_data():

        adp_url = "https://www.fantasypros.com/nfl/adp/ppr-overall.php"
        adp_data = pd.read_html(adp_url)
        df = pd.concat(adp_data)
        df.rename(columns = {'Player Team (Bye)':'Player'}, inplace=True)
        players = df['Player'].to_list()
        available_players = [x if type(x) is str else "" for x in players]
        players_info = [x.split() for x in available_players]
        first_names = [ " ".join(x[:2]) for x in players_info]
        teams = [ " ".join(x[2:3]) for x in players_info]
        bye_weeks = [x[3] if len(x) == 4  else x for x in players_info]

        df['Player'] = df['Player'].replace(players,first_names)
        df.insert(2,"Team", teams)

        df.insert(3,"Bye", bye_weeks)
        df.drop(['Unnamed: 0','AVG', 'Expert', 'Site', 'Date'],axis=1,
                inplace=True)

        df = df.set_index('Rank')
        position_dfs = []
        player_stats = {}
        player_stats['content'] = "Fantasy Pros"
        player_stats['rb_df'] = df[df['POS'].str.match('RB*')==True]
        player_stats['wr_df'] = df[df['POS'].str.match('WR*')==True]
        player_stats['te_df'] = df[df['POS'].str.match('TE*')==True]
        player_stats['qb_df'] = df[df['POS'].str.match('QB*')==True]

        return player_stats

def fantasypros():
    url ="/Users/bcarson/Projects/lollipop/flask/static/csv/"
    positions = ['rb','wr','te','qb']
    qb_csv_url="static/csv/"
    years = ["2017","2018","2019",]
    ext = ".csv"
    urls_dict = {}
    df_dicts = {}
    col = ['RUSHING', 'RUSHING', 'RUSHING', 'RUSHING', 'RUSHING', 'RUSHING']
    col2 = ['RECEIVING', 'RECEIVING', 'RECEIVING', 'RECEIVING', 'RECEIVING']
    col3 = ['MISC', 'MISC', 'MISC', 'MISC']
    files = ["fantasyPros_"+x+"_"+y+".csv" for x in positions for y in years]
    urls_dict["rb_urls"] = ("/Users/bcarson/Projects/lollipop/flask/static/csv/"+x for x in files if "rb" in x)
    urls_dict["wr_urls"] = ("/Users/bcarson/Projects/lollipop/flask/static/csv/"+x for x in files if "wr" in x)
    urls_dict["te_urls"] = ("/Users/bcarson/Projects/lollipop/flask/static/csv/"+x for x in files if "te" in x)
    urls_dict["qb_urls"] = ("/Users/bcarson/Projects/lollipop/flask/static/csv/"+x for x in files if "qb" in x)

    for x in urls_dict:
        for url in urls_dict[x]:
            for year in years:
                if year in  url:
                    season = year
                    df_key = x+"_"+season
                    df_dicts[df_key] = pd.read_csv(url)
    ff_df_dicts = fantasypros_data()
    updated = []
    player_dicts = []
    pos_url_years = [x+"_"+y for x in [*urls_dict] for y in years]
    for pos_df in [*ff_df_dicts][1:]:

        for player in ff_df_dicts[pos_df].values.tolist():
            player_dict = (dict(zip(ff_df_dicts[pos_df].keys().tolist(),player)))
            updated_player_dict ={}
            for stat_year in [*df_dicts]:
                for player_line in df_dicts[stat_year].values.tolist():
                    if type(player_line[0]) is int:
                        player_line = player_line[1:19]
                    if player[0] in   player_line[0]:

                        headers = [z for z in df_dicts[stat_year].keys().tolist()[3:-1]]
                        data = [z for z in player_line[3:-1]]
                        breakpoint()
                        players_stats_dict = dict(zip(headers,data))
                        player_dict = {**player_dict,**{stat_year:players_stats_dict}}


                        player_dicts.append(player_dict)


    players = [ player_d for player_d in player_dicts if len(player_d) == 13]

    return players







# def fantasypros_data(dfs):
#     adp_url = "https://www.fantasypros.com/nfl/adp/ppr-overall.php"
#     adp_data = pd.read_html(adp_url)
#     # qb_data = pd.read_csv('fantasypros_qb_2017')
#     df = pd.concat(adp_data)
#     players = df['Player Team (Bye)'].to_list()
#     teams=[]
#     bye_weeks=[]
#     for player in players:
#         check_for_str = isinstance(player,str)
#         if isinstance(player,str):
#             player_line = player.split()
#             # player_line = ",".join(player)
#             # print(player_line[0:2])
#             first_name = " ".join(player_line[:2])
#             team = " ".join(player_line[2:3])
#             teams.append(team)
#             bye_week = team = " ".join(player_line[3:])
#             bye_weeks.append(bye_week)
#             df['Player Team (Bye)'] = df['Player Team (Bye)'].replace(player,first_name)
#     df.rename(columns = {'Player Team (Bye)':'Player'}, inplace = True)
#     df.insert(2,"Team",pd.Series(teams))
#     df.insert(3,"Bye",pd.Series(bye_weeks))
#     df.drop(['Unnamed: 0','AVG', 'Expert', 'Site', 'Date'],axis =1 , inplace=True)
#     delete_list = ['Unnamed: 0','AVG', 'Expert', 'Site', 'Date']
#     # for x in delete_list:
#     #     del df[x]
#     # # print(df.head)
#     df = df.set_index('Rank')
#     # print(df)a
#     headers=[ 'Player', 'Team', 'Bye', 'POS', 'ESPN', 'RTSports','Fantrax',"Yahoo"]
#     Row_list=[]
#     player_list = []
#     running_back = {}
#     quarter_backs = []
#     qb_dict = {}
#     running_backs = []
#
#     rb_df = df[df['POS'].str.match('RB*')==True]
#     wr_df = df[df['POS'].str.match('WR*')==True]
#     te_df = df[df['POS'].str.match('TE*')==True]
#     qb_df = df[df['POS'].str.match('QB*')==True]
#
#     rushing_colums = ["Rushing_Att","Rushing_Yds","Rushoing_Y/A","Rushing_TD",]
#     receiving_colums = []
#     passing_colums = ["PASSING_CMP","PASSING_ATT","PASSING_PCT","PASSING_YDS","PASSING_Y/A","PASSING_TD","PASSING_INT","PASSING_SACKS"]
#     def_colums = []
#
#     headers = qb_df.columns.values
#
#     quarter_backs = []
#     someList=[]
#     count = 0
#     for stat_dict in qb_df.values:
#         temp = [dict(zip(headers,stat_dict))]
#         quarter_backs.append(temp[0])
#     return (quarter_backs)






# def fantasypros_qb_2017():
#     data = pd.read_csv("/Users/bcarson/Projects/lollipop/flask/static/csv/fantasyPros_qb_2017.csv",sep=', ')
#     player_dict = {}
#     headers = ["Rank","Player","Team","PASSING_CMP","PASSING_ATT","PASSING_PCT","PASSING_YDS","PASSING_Y/A","PASSING_TD","PASSING_INT","PASSING_SACKS","RUSHING_ATT","RUSHING_YDS","RUSHING_TD","MISC_FL","MISC_G","MISC_FPTS",",MISC_FPTS/G","MISC_OWN"]
#     player_dict_list = []
#     for stat in data.values:
#         df_asStr = str(stat.tolist())
#         df_asStrStrip = df_asStr.strip('['']')
#         stat_value = df_asStrStrip.split(',')
#         player_dict_list.append(dict(zip(headers,stat_value)))
#     return player_dict_list

# def fantasypros_qb_2018():
#     data = pd.read_csv("/Users/bcarson/Projects/lollipop/flask/static/csv/fantasyPros_qb_2018.csv",sep=', ')
#     player_dict = {}
#     headers = ["Rank","Player","Team","PASSING_CMP","PASSING_ATT","PASSING_PCT","PASSING_YDS","PASSING_Y/A","PASSING_TD","PASSING_INT","PASSING_SACKS","RUSHING_ATT","RUSHING_YDS","RUSHING_TD","MISC_FL","MISC_G","MISC_FPTS",",MISC_FPTS/G","MISC_OWN"]
#     player_dict_list = []
#     for stat in data.values:
#         df_asStr = str(stat.tolist())
#         df_asStrStrip = df_asStr.strip('['']')
#         stat_value = df_asStrStrip.split(',')
#         player_dict_list.append(dict(zip(headers,stat_value)))
#     return player_dict_list



# def fantasypros_qb_2019():
#     data = pd.read_csv("/Users/bcarson/Projects/lollipop/flask/static/csv/fantasyPros_qb_2019.csv",sep=', ')
#     player_dict = {}
#     headers = ["Rank","Player","Team","PASSING_CMP","PASSING_ATT","PASSING_PCT","PASSING_YDS","PASSING_Y/A","PASSING_TD","PASSING_INT","PASSING_SACKS","RUSHING_ATT","RUSHING_YDS","RUSHING_TD","MISC_FL","MISC_G","MISC_FPTS",",MISC_FPTS/G","MISC_OWN"]
#     player_dict_list = []
#     for stat in data.values:
#         df_asStr = str(stat.tolist())
#         df_asStrStrip = df_asStr.strip('['']')
#         stat_value = df_asStrStrip.split(',')
#         player_dict_list.append(dict(zip(headers,stat_value)))
#     return player_dict_list
#     # return dfsy
# -*- coding: utf-8 -*-
# def fantasypros_qb():
    url ="/Users/bcarson/Projects/lollipop/flask/static/csv/",
    positions = ['rb','wr','te','qb','dst']
    qb_csv_url="static/csv/"
    years = ["2017","2018","2019","2020"]
    ext = ".csv"
    # files = [fantasyPros_x_y.csv for x in positions for y in years]

def main():
    # open_csv()
    csvScrap()

if __name__ == "__main__":
    main()
