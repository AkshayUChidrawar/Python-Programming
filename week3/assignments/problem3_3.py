m = ("January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December")
def problem3_3(month, day, year):
    mon = m[month-1]
    d = str(day)
    com = ','
    y = str(year)
    date = mon + ' '+ d+ com + ' '+ y
    print  (date)