import os
import csv

phones = []
phone_header = [ 'Name', 'Phone Number']

def save_phone_list():
    f = open("E:\\coursera\\week4\\myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()
    
def load_phone_list():
    if os.access("E:\\coursera\\week4\\myphones.csv",os.F_OK):
        f = open("E:\\coursera\\week4\\myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()

def disp():
    show_phone(phone_header, "")
    index = 1
    for ph in phones:
        show_phone(ph, index)
        index = index + 1
    return 0
def show_phone(ph, index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index, ph[0], ph[1]))
    
def reorder_phones():
    global phones       # this insures that we use the one at the top
    phones.sort()
    return 0
def create_phone():
    newname = input("Enter name for a new phone record: ")
    newnum = input("Enter phone number: ")
    new_rec = [newname,newnum]
    phones.append(new_rec)
    return 0

def proper_menu_choice(ind):
    if ((ind.isdigit()== False) or (int(ind)< 1) or (int(ind) > len(phones))):
        return False
    else:
        return True
    
def delete_phone(drec):
    drec = int(drec)
    del phones[drec-1]
    print( "Deleted phone #", drec)
    return 0

def edit_phone(erec):
    erec = int(erec)
    phrec = phones[erec-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    print(phrec)
    newname = input("Write a new name: ")
    if newname == "":
        newname = phrec[0]
    newnum = input("Enter new phone number: ")
    if newnum == "":
        newnum = phrec[1]
    phrec = [newname, newnum]
    phones[erec-1] = phrec
    return 0

def menu_choice():
    print("\ns) Show")
    print("r) Reorder")
    print("n) New")
    print("d) Delete")
    print("e) Edit")
    print("q) Quit")
    ch = input("Enter your Choice from above: ")    
    return ch
    
def main_func():
    load_phone_list()
    
    while True:
        choice = menu_choice()
        mych = choice.lower()
        if mych not in ['s','r','n','d', 'e', 'q']:
            print(choice, " is an Invalid choice.")
        else:
            if mych == 's':
                disp()
            elif mych == 'r':
                reorder_phones()
            elif mych == 'n':
                create_phone()
            elif mych == 'd':
                drec = input("Which item do you want to delete? ")
                if (proper_menu_choice(drec)):
                    delete_phone(drec)
                else:
                    print ("'" + drec + "' needs to be integer index of phone record within boundaries!")
            elif mych == 'e':
                erec = input("Which item do you want to edit? ")
                if (proper_menu_choice(erec)):
                    edit_phone(erec)
                else:
                    print ("'" + erec + "' needs to be integer index of phone record within boundaries!")                
            else:
                print( "Exiting...")
                break     # jump out of while loop
    
    save_phone_list()

# The following makes this program start running at main_loop() when executed as a stand-alone program.    
if __name__ == '__main__':
    main_func()