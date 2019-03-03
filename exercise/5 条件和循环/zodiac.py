# import you birthday then export your zodiac

zodiac_name = ('Capricorn', 'Aquarius', 'Pisces', 'Arise', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius')
chinese_zodiac =('猴鸡狗猪鼠牛虎兔龙蛇马羊')
# print(zodiac_name.__len__())
# print(zodiac_name)
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# print(zodiac_days.__len__())
# print(zodiac_days)

birthday = input("Please input your birthday [Year][Month][Day], e.g. 19850812 :")
(year, month, day) = (int(birthday[0:4]), int(birthday[4:6]), int(birthday[6:8]))

year_count = year % 12
print("Your Chinese Zodiac: " + chinese_zodiac[year_count], end='  ')
zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
num = list(zodiac_day).__len__()
print("Zodiac: " + zodiac_name[num])
