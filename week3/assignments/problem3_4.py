m = ("January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December")
def problem3_4(mon, day, year):
    mont = str (m.index(mon) + 1)
    d = str(day)
    y = str(year)
    date = mont + '/' + d + '/' + y
    print (date)
