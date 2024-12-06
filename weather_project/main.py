import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
#
# temp_max = data["temp"].max()
# print(temp_max)
#
#
# print(data["condition"])
# print(data.condition)

data[data.day == "Monday"["day"]]