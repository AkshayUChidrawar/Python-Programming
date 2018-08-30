alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):
    print (my_list)
    print (my_list[0])
    print (my_list[-1])
    end= len(my_list)
    print(my_list[3:5])
    print(my_list[0:3])
    print(my_list[3:end])
    print (end)
    my_list.append('z')
    print (my_list)
     