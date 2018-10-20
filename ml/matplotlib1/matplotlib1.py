import pandas as pd
import matplotlib.pyplot as plt

f = open(
    'E:\\baiduyundownload\\机器学习\\01.python数据分析与机器学习实战\\课程资料\\唐宇迪-机器学习课程资料\\Python库代码（4个）\\3-可视化库matpltlib\\UNRATE.csv')

unrate = pd.read_csv(f)

unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))

first_wetwelve = unrate[0:12]
plt.plot(first_wetwelve['DATE'], first_wetwelve['VALUE'])
plt.xticks(rotation=45)
plt.show()
