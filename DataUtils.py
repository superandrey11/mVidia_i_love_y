import pandas as pd

print("LOAD DATA...")
characteristicts_data = pd.read_csv('C:\javaTest/dataset2.csv', encoding='utf-8', na_filter=False)
comments_data = pd.read_csv('C:\javaTest/dataset1.csv', encoding='utf-8', na_filter=False)

categories = comments_data.CATEGORY_ID.unique()
testing_categories = [
    2050101, #smartphones
    1070907, #tv
    2030201, #notebook
    4030101, #washing mashines
    #todo холодильники пылесосы посудомойки
]

subcat_characteristic_map = {}
for i, v in characteristicts_data.groupby("GROUP_ID"):
    subcat_characteristic_map[i] = v['CODE'].unique()

def get_category_comments_data(id):
    return comments_data[comments_data['CATEGORY_ID'] == id]

def get_category_characteristicts_data(id):
    return characteristicts_data[characteristicts_data['CATEGORY_ID'] == id]

def get_unique_characteristics(data):
    return data["CODE"].unique()



