import pandas

f = open(
    'E:\\baiduyundownload\\机器学习\\01.python数据分析与机器学习实战\\课程资料\\唐宇迪-机器学习课程资料\\Python库代码（4个）\\2-数据分析处理库pandas\\food_info.csv')

food_info = pandas.read_csv(f)

print(type(food_info))
print(food_info.dtypes)

print(food_info.head(3))

print(food_info.tail(4))

print(food_info.columns)

print(food_info.shape)

print(food_info.loc[3:6])

print(food_info["NDB_No"])

columns = ["Zinc_(mg)", "NDB_No"]
print(food_info[columns])

col_names = food_info.columns.tolist()
print(col_names)
gram_colmns = []
for c in col_names:
    if c.endswith("g"):
        gram_colmns.append(c)
gram_df = food_info[gram_colmns]
print(gram_df)

print(food_info["Iron_(mg)"])
div_1000 = food_info["Iron_(mg)"] / 1000
print(div_1000)

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]

iron_grams = food_info["Iron_(mg)"] / 1000

max_calories = food_info["Energ_Kcal"].max
print(max_calories)

food_info.sort_values("Sodium_(mg)", inplace=True)
print(food_info["Sodium_(mg)"])

food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)



