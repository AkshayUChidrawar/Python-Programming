def problem2_8(temp_list):
    temp_list.sort()
    n = len(temp_list)
    sum = 0
    for each in range(0,n):
        sum = sum + temp_list[each]
    avg = sum/n
    print ("Average:", avg)
    print ("High:", temp_list[-1])
    print ("Low:", temp_list[0])