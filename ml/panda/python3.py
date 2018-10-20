import pandas as pd
import numpy as np

f = open(
    'E:\\baiduyundownload\\机器学习\\01.python数据分析与机器学习实战\\课程资料\\唐宇迪-机器学习课程资料\\Python库代码（4个）\\2-数据分析处理库pandas\\titanic_train.csv')

titanic_survival = pd.read_csv(f)
# print(titanic_survival.head())

age = titanic_survival["Age"]
# print(age.loc[0:10])
age_is_null = pd.isnull(age)
# print(age_is_null)
age_null_true = age[age_is_null]
# print(age_null_true)

age_null_count= len(age_null_true)
# print(age_null_count)


mean_age = sum(titanic_survival["Age"]) / len(titanic_survival["Age"])
# print(mean_age)

good_ages = titanic_survival["Age"][age_is_null == False]
# print(good_ages)

correct_mean_age = sum(good_ages)/len(good_ages)
# print(correct_mean_age)

correct_mean_age = titanic_survival["Age"].mean()
# print(correct_mean_age)

passenger_classes = [1,2,3]

# fares_by_class = {}
# for this_class in passenger_classes:
#     pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
#     pclass_fares = pclass_rows["Fares"]
#     fare_for_class = pclass_fares.mean()
