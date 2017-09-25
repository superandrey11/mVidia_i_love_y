import DataUtils

data = DataUtils.get_category_characteristicts_data(2050101)
#for id, data in data.groupby("GROUP_ID"):
#    print(str(id) +": ,[]")

#for n, c in dict(zip(data['NAME'], data['CODE'])).items():
#    print(str(c) +":[],")
for id, data in data.groupby("GROUP_ID"):
    print("-"*50)
    print(id)
    print(data["GROUP_NAME"].iloc[0])
    for n, c in dict(zip(data['NAME'], data['CODE'])).items():
        print(n + " " + str(c))