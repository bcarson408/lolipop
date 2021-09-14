import json
import os.path as path
from json.decoder import JSONDecodeError
import csv
import pandas as pd
import re


# class FantasyProsScrapper():
#     # dict_qb = fantasypros_qb_2018()

    def fantasypros_data(self):

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

    def fantasypros(self):
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
        # urls_dict["te_urls"] = ("/Users/bcarson/Projects/lollipop/flask/static/csv/"+x for x in files if "te" in x)
        # urls_dict["qb_urls"] = ("/Users/bcarson/Projects/lollipop/flask/static/csv/"+x for x in files if "qb" in x)
        for x in urls_dict:
            for url in urls_dict[x]:
                for year in years:
                    if year in  url:
                        season = year
                        df_key = x+"_"+season
                        df_dicts[df_key] = pd.read_csv(url)
        ff_df_dicts = self.fantasypros_data()
        updated = []
        player_dicts = []
        pos_url_years = [x+"_"+y for x in [*urls_dict] for y in years]
        for pos_df in [*ff_df_dicts][1:-1]:
            for player in ff_df_dicts[pos_df].values.tolist():
                player_dict = (dict(zip(ff_df_dicts["rb_df"].keys().tolist(),player)))
                updated_player_dict ={}
                for stat_year in [*df_dicts]:
                    for player_line in df_dicts[stat_year].values.tolist():
                        if player[0] in  player_line[1]:
                            headers = [z for z in df_dicts[stat_year].keys().tolist()[3:-1]]
                            data = [z for z in player_line[3:-1]]
                            players_stats_dict = dict(zip(headers,data))
                            player_dict = {**player_dict,**{stat_year:players_stats_dict}}
                player_dicts.append(player_dict)
                            # updated_player_dict = {**player_dict,**players_stats_dict}
                            # updated_player_dict = {**player_dict,**{stat_year:updated_player_dict}}
                            # current_player = ff_df_dicts["rb_df"].loc[(ff_df_dicts["rb_df"].Player) == player[0]]
                            # idx = len(current_player.keys())+1
                            # breakpoint()
        players = [ player_d for player_d in player_dicts if len(player_d) == 13]
        breakpoint()
        return players
        # for x in players:
        #     if len(x) > 10 :
        #         print(x['Player'])
        #         print()
        # breakpoint()


                    # if player in player_dict:
                    #     print(player_dict,player_dict,df_dicts[stat_year]["Player"])


        # #                 x["year"].append({"2017":player_dict})






        # [ for x in df_positions]


    #     for x in fantasypros:
    #
    #         x["year"] = []
    #
    #         for player_dict in fp_qb_df :
    #             if x['Player'] in player_dict['Player']:
    #                 # print(player_dict['Player'],player_dict)
    #                 x["year"].append({"2017":player_dict})
    #
    #         for player_dict1 in dict_qb :
    #             if x['Player'] in player_dict1['Player']:
    #                 # x["year"] = []
    #                 x["year"].append({"2018":player_dict1})
    #
    #         for player_dict2 in dict_qb_2019 :
    #             if x['Player'] in player_dict2['Player']:
    #                 # x["year"] = []
    #                 x["year"].append({"2019":player_dict2})
    #                 # print(x)
    #         # print(x["year"])
    #         player_dict_list.append(x)
    #         # df_years = pd.DataFrame(x)
    #         # qb_df = df_years[df_years['POS'] == 'QB']
    #
    #         # indx = 0
    #         # for year in df_years.keys():
    #         #     year_dict = df_years[year]
    #         #     indx += 1
    #     player_stats = pd.DataFrame(player_dict_list)
    #     headers = ['Player', 'Team', 'PASSING_CMP', 'PASSING_ATT', 'PASSING_PCT', 'PASSING_YDS', 'PASSING_Y/A', 'PASSING_TD', 'PASSING_INT', 'PASSING_SACKS', 'RUSHING_ATT', 'RUSHING_YDS', 'RUSHING_TD', 'MISC_FL', 'MISC_G', 'MISC_FPTS', ',MISC_FPTS/G', 'MISC_OWN']
    #     for i in range(len(player_stats)):
    #         yearly_status = player_stats.loc[i]['year']
    #         for idx in range(len(yearly_status)):
    #                 if idx== 0:
    #                     year='2017'
    #                 if idx== 1:
    #                     year='2018'
    #                 if idx== 2:
    #                     year='2019'
    #                 stats = yearly_status[idx][year]
    #                 print(year,stats['Team'],stats['PASSING_CMP'])
    #         print()
    #
    #         # print()
    #
    #     player_stats_dict = player_stats.to_dict()['year']
    #     for player in range(len(player_stats_dict)):
    #         player_stats_dict[player]
    #         for y in range(len(player_stats_dict[player])):
    #             player_stat_year = player_stats_dict[player][y]
    #             if y == 0:
    #                 key = '2017'
    #             if y == 1:
    #                 key = '2018'
    #             if y == 2:
    #                 key = '2019'
    #             for k in player_stat_year[key].keys():
    #                 print(f"{k} {player_stat_year[key][k]}", end=" ")
    #             # breakpoint()
    #           # player_stat = year_dict
    #             # qb_stats.append(player_stat)
    #         # rb_df = df[df['FantPos'] == 'RB']
    #
    #
    # # wr_df = df[df['FantPos'] == 'WR']
    # # te_df = df[df['FantPos'] == 'TE']
    #
    #
    #     #####################################################################################
    #
    #
    #
    #     return df_positions


    # def tranform_colums(df,new_columns):
    #     df = df[[ "Rank","Player","Team","Bye","POS","ESPN","RTSports","Fantrax","FFC"]+new_columns+["FL"]]
    #     return df

def main():
    fantasypros()


if __name__ == "__main__":
    main()
