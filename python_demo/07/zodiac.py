# import you birthday then export your zodiac

zodiac_name = ('Capricorn', 'Aquarius', 'Pisces', 'Arise', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius')
# print(zodiac_name.__len__())
# print(zodiac_name)
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# print(zodiac_days.__len__())
# print(zodiac_days)

birthday = input("Please input your birthday [Month][Day], e.g. 0812 :")
(month, day) = (int(birthday[0:2]), int(birthday[2:4]))
zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
num = list(zodiac_day).__len__()
print("Your Zodiac is: " + zodiac_name[num])
