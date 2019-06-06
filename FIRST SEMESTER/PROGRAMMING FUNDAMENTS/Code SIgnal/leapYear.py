def is_leap(year):

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap = True
    else:
        leap = False

    return leap


print(is_leap(2000))