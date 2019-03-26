# Zeller's Rule f = k + [(13*m-1)/5 + D + [D/4] + [c/4] - 2*c]
# 26 mars 2019 >> f = 26 + [(13*1-1)/5 + 19 + (19/4) + (20/4) - 2*20]

def find_name_of_first_day_inYear(year):
    year = str(year)
    last_two_digits_of_yera = int(year[-2]+year[-1])
    first_two_digits_of_yera = int(year[0]+year[1])

    print(last_two_digits_of_yera)
    print(first_two_digits_of_yera)

    list_ = [1, (13*11-1)/5 , last_two_digits_of_yera , last_two_digits_of_yera/4 ,
            first_two_digits_of_yera/4 , -2*first_two_digits_of_yera]
    day_num = int((sum(list_))) // 1
    print(day_num)

    if day_num < 0 :
        first_day_num = day_num
        day_num = -1 * day_num

        while (day_num)%7 != 0:
            day_num += 1
        else :
            day_num = day_num + first_day_num
    return day_num % 7 

print(find_name_of_first_day_inYear(2019))