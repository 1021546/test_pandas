# # pd.read_csv() 使用預設參數
# import pandas as pd

# csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
# csv_df = pd.read_csv(csv_url)
# print(csv_df)


# csv_url_1 = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
# csv_df_1 = pd.read_csv(csv_url_1, header=None, skiprows=1, names=['number', 'player', 'pos', 'ht', 'wt', 'birth_date', 'college'])
# print(csv_df_1)

# # pd.read_table() 指定 sep=";"
# import pandas as pd

# txt_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.txt"
# txt_df = pd.read_table(txt_url, sep=";")
# print(txt_df)

# # pd.read_excel() 使用預設參數
# import pandas as pd

# xlsx_url = "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
# chicsgo_bulls = pd.read_excel(xlsx_url)
# print(chicsgo_bulls)


# # pd.read_excel() 指定工作表與讀取範圍
# import pandas as pd

# xlsx_url_1 = "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
# boston_celtics = pd.read_excel(xlsx_url_1, sheet_name='boston_celtics_2007_2008', skiprows=6, header=None, names=['number', 'player', 'pos'], usecols=[0, 1, 2])
# print(boston_celtics)


# # JSON 檔案儲存在雲端
# from requests import get

# json_url = 'https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.json'
# chicago_bulls_dict = get(json_url).json()
# print(type(chicago_bulls_dict))
# print(chicago_bulls_dict)


#  JSON 檔案儲存在本機
from json import load

json_fp = "chicago_bulls_1995_1996.json"
with open(json_fp) as f:
    chicago_bulls_dict = load(f)
print(type(chicago_bulls_dict))
print(chicago_bulls_dict)

# 計算勝率或者從先發陣容中選出最喜歡的球員
winning_percentage = chicago_bulls_dict["records"]["wins"] / (chicago_bulls_dict["records"]["wins"] + chicago_bulls_dict["records"]["losses"])
fav_player = chicago_bulls_dict["starting_lineups"]["SG"]
print("勝率為 {:.2f}".format(winning_percentage))
print("最喜歡的球員是 {}".format(fav_player))