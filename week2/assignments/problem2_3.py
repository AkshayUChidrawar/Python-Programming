def problem2_3(my_list):
    size =[]
    for each in my_list:
        size.append(len(each))
    for element in range(0, len(my_list)):
        print(my_list[element], "has", size[element], "letters.")