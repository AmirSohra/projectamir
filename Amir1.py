# ********* In The Nmae Of God ***********
#  Student ID: 401130433
#  Student Name: Amir Ali Sohrabi
#  Fundamental of Computers and Programming (python)
#  Hamedan University of Technology, Hamedan, Iran.

from AmirC import *

def menu_Handle():
    print('-----------------menu Handle----------------- ')
    print('1.Append / Update / Delete  pack')
    print('2.Append / Update / Delete  continer')
    print('3.Append / Update / Delete  car')
    print('4.loading')
    print('5.Send and Receive Cargo')
    print('6.display packs')
    print('7.display packs')
    print('8.display packs')
    print('9.Exit')
    
    print()
    print()
    choose = eval(input("Please Enter number : "))
    return choose

f = open('LTS.txt','w')

def login():
    global f
    print("-----------------------Local Transportation System-----------------------")
    print("1.Login System")
    print("2.Make Account")

    print()
    item = int(input("Enter your a item: "))
   
    if item == 2:
        
        User_Name = input("Enter your User name : ")
        password = input("Enter your Password : ")

        f= open('LTS.txt','w')
        f.write(password)

    else :

        User_Name = input("Enter your User name : ")
        print(f"Hello {User_Name}, you already made account")

        f = open('LTS.txt', 'r')
        print(f.read())

def menu_Loading():
    print('-----------------menu Loading----------------- ')
    print('1.Diplay Packs')
    print('2.Display Continers')
    print('3.Display Cars')
    print('4.loading pack to continer')
    print('5.Join continer to car_carry_continer')
    print('6.loding Ordinary pack to room_car')
    print('7.Exit')
    
    print()
    choose = eval(input(" Please Enter number: "))
    return choose

def menu_Send_Receive_Cargo():
    print('-----------------menu_Send_Receive_Cargo----------------- ')
    print('1.Display cargo ')
    print('2.Send Letter load and Cargo')

    print()
    choose = eval(input("Please Enter number: "))
    return choose

# -------------------------------------------Packs-----------------------------------------------
list_packs = []
count_pack = 0 

def getType_pack():
    print('-----------------------Packs------------------------------')
    print('1.Ordinary pack')
    print('2.Pack_breakable')
    print('3.Cold Pack')
    choose = eval(input(" Please Enter your type of pack: "))
    return choose

def menu_CRUD_pack():
    print('-----------------menu CURD Pack----------------- ')
    print('1.Append new pack')
    print('2.Update pack')
    print('3.Delete pack')

    choose = eval(input("Please Enter number: "))
    return choose

def display_packs():
    for i in list_packs:

        if i.get_type_pack() == "Pack" :
            line = "Pack ordinary" + str(i.packNumber) + ': ' +  "weight: " + str(i.weight) + " , " +"destination: " + i.destination + " , " + "start: " + i.start + " , " + "history: " + i.history +'\n'
            print(line)   

        elif i.get_type_pack() == "Pack_breakable" :
            line = "Pack breakable" + str(i.packNumber) + ': ' +  "weight: " + str(i.weight) + " , " +"destination: " + i.destination + " , " + "start: " + i.start + " , " + "history: " + i.history +'\n'
            print(line) 

        elif i.get_type_pack() == "Pack_cold" :
            line = "Pack cold" + str(i.packNumber) + ': ' +  "weight: " + str(i.weight) + " , " +"destination: " + i.destination + " , " + "start: " + i.start + " , " + "history: " + i.history + " , " + "temperature: " + i.temperature +'\n'
            print(line) 

def insert_pack():

    choose_Type_pack = getType_pack()

    global count_pack

    count_pack = count_pack + 1

    if choose_Type_pack ==1 :

        weight = int(input('Enter weight: '))
        destination = input('Enter destination: ')
        start = input('Enter start: ')
        history = input('Enter history: ')
        p = Pack(count_pack, weight, destination, start, history)
        
        list_packs.append(p)

    elif choose_Type_pack == 2:

        weight = int(input('Enter weight: '))
        destination = input('Enter destination: ')
        start = input('Enter start: ')
        history = input('Enter history: ')

        p = Pack_breakable(count_pack, weight, destination, start, history)

        list_packs.append(p)

    elif choose_Type_pack == 3:

        weight = int(input('Enter weight: '))
        destination = input('Enter destination: ')
        start = input('Enter start: ')
        temperature = input('Enter temperature: ')
        history = input('Enter history: ')
        
        p = Pack_cold(count_pack, weight, destination, start, history ,temperature)

        list_packs.append(p)

def update_pack():

    display_packs()

    Number_pack = int(input("Enter packNumber: "))

    change_property = input("Which property do you want to change: ")

    new_value = input(f"Enter new value {change_property} :")

    # How to Update object of list_packs ? 

    if change_property == "weight":
        list_packs[Number_pack-1].weight = new_value

    elif change_property == "destination":
        list_packs[Number_pack-1].destination = new_value

    elif change_property == "start":
        list_packs[Number_pack-1].start = new_value

    elif change_property == "temperature":
        list_packs[Number_pack-1].temperature = new_value

    elif change_property == "history":
        list_packs[Number_pack-1].history = new_value

def delete_pack():

    global count_pack

    display_packs()

    Number_pack = int(input("Enter packNumber which you want to delete it :"))

    # How to delete object of list_packs ?

    list_packs.pop(Number_pack -1 )

    count_pack -=1

    for i in list_packs:        # Sort index
        if i.packNumber > Number_pack :
            i.packNumber = i.packNumber -1 

# -------------------------------------------Continers-----------------------------------------------
list_continers = []
count_continer = 0 

def menu_CRUD_continer():
    print('-----------------menu CURD Continer----------------- ')
    print('1.Append new Continer')
    print('2.Update Continer')
    print('3.Delete Continer')

    print()
    choose = eval(input("Please Enter number: "))
    return choose

def getType_continer():
    print('--------Continer-------')
    print('1.breakable_Container')
    print('2.Freezer_Container')
    print()

    choose = eval(input("Enter your type of Continer: "))
    return choose

def display_continer():
    for i in list_continers:

        if i.get_type_continer() == "breakable_Container" :
            line = "Continer breakable" + str(i.continerNumber) + ' : ' +  "weight: " + str(i.weight) + " , " +"countMax_pack: " + str(i.countMax_pack) + " , "  + 'speed: ' + i.speed +'\n'
            print(line)   

        elif i.get_type_continer() == "Freezer_Container" :
            line = "Continer Freezer" + str(i.continerNumber) + ' : ' +  "weight: " + str(i.weight) +  " , " +"countMax_pack: " + str(i.countMax_pack) +  " , "  + 'Car_refrigerator_temperature: ' + i.Car_refrigerator_temperature +'\n'
            print(line) 

def insert_continer():

    choose_Type_continer = getType_continer()

    global count_continer
    global flag_continer

    if choose_Type_continer ==1 :

        count_continer = count_continer + 1

        weight = int(input('Enter weight: '))
        countMax_pack = int(input('Enter countMax_pack: '))
        speed = input('Enter speed: ')
        
        c = breakable_Container(count_continer, weight, countMax_pack, speed )

        list_continers.append(c)

    elif choose_Type_continer ==2 :

        count_continer = count_continer + 1

        
        weight = int(input('Enter weight: '))
        countMax_pack =int( input('Enter countMax_pack: '))
        Car_refrigerator_temperature = input('Enter Car_refrigerator_temperature: ')
        
        c = Freezer_Container(count_continer, weight, countMax_pack, Car_refrigerator_temperature )

        list_continers.append(c)
        
def update_continer():

    display_continer()

    print()
    Number_continer = int(input("Enter continerNumber: "))

    change_property = input("Which property do you want to change: ")

    new_value = input(f"Enter new value {change_property} :")

    # How to Update object of list_Continers ? 

    if change_property == "weight":
        list_continers[Number_continer-1].weight = new_value

    elif change_property == "countMax_pack":
        list_continers[Number_continer-1].countMax_pack = new_value

    elif change_property == "speed":
        list_continers[Number_continer-1].speed = new_value

    elif change_property == "Car_refrigerator_temperature":
        list_continers[Number_continer-1].Car_refrigerator_temperature = new_value

def delete_continer():

    global count_continer

    display_continer() 

    print()

    Number_continer = int(input("Please Enter continerNumber which you want to delete it :"))

    # How to delete object of list_continers ?

    list_continers.pop(Number_continer -1 )

    count_continer -=1

    for i in list_continers:
        if i.continerNumber > Number_continer :
            i.continerNumber = i.continerNumber -1 

# -------------------------------------------Cars-----------------------------------------------
list_cars = []
count_car = 0 

def menu_CRUD_cars():
    print('-----------------menu CURD Cars----------------- ')
    print('1.Append new Cars')
    print('2.Update Cars')
    print('3.Delete Cars')

    print()
    choose = eval(input("Please Enter number: "))
    return choose

def getType_cars():
    print('-----------------Cars-----------------')
    print('1.room_car ( For ordinary Pack )')
    print('2.car_carry_continer')

    print()
    choose = eval(input("Please Enter your type of Cars: "))
    return choose

def display_cars():
    for i in list_cars:

        if i.get_type_car() == "Room_Car" :
            line = "room car" + str(i.carNumber) + ' : ' +  "weight: " +str(i.weight)+ " , " +"countMax_pack: " + str(i.countMax_pack) + '\n'
            print(line)   

        elif i.get_type_car() == "Car_Carry_Continer" :
            line = "car carry continer" + str(i.carNumber) + ' : ' +  "weight: " + str(i.weight) + " , " +"countMax_continer: " + str(i.countMax_continer) + '\n'
            print(line)

def insert_car():

    choose_Type_car = getType_cars()

    global count_car

    if choose_Type_car ==1 :

        count_car = count_car + 1

        print()
        weight = int(input('Please Enter weight: '))
        countMax_pack = int(input('Please Enter countMax_pack: '))

        car = Room_Car(count_car, weight, countMax_pack)
        
        list_cars.append(car)

    elif choose_Type_car ==2 :

        count_car = count_car + 1

        print()
        weight = int(input('Please Enter weight: '))
        countMax_continer =int( input('Please Enter countMax_continer: '))
        
        car = Car_Carry_Continer(count_car, weight, countMax_continer )

        list_cars.append(car)

def update_car():

    display_cars()

    Number_car = int(input("Enter carNumber: "))

    change_property = input("Which property do you want to change: ")

    new_value = input(f"Enter new value {change_property} :")

    # How to Update object of list_cars ? 

    if change_property == "weight":
        list_cars[Number_car-1].weight = new_value

    elif change_property == "countMax_pack":
        list_cars[Number_car-1].countMax_pack = new_value

    elif change_property == "countMax_continer":
        list_cars[Number_car-1].countMax_continer = new_value

def delete_car():

    global count_car

    display_cars()

    Number_car = int(input("Enter carNumber which you want to delete it :"))

    # How to delete object of list_cars ?

    list_cars.pop(Number_car -1 )

    count_car -=1

    for i in list_cars:
        if i.carNumber > Number_car :
            i.carNumber = i.carNumber -1 

# -------------------------------------------Cargo-----------------------------------------------
list_warehous = []

def Display_cargo():

    for i in list_cars:

        if i.get_type_car() == "Room_Car":

            print(f'-------------Ordinary Packs of Room Car{i.carNumber}------------------')

            for j in i.list_packs_ordinary:
                
                line = "Pack ordinary" + str(j.packNumber) + ': ' +  "weight: " + str(j.weight) + " , " +"destination: " + j.destination + " , " + "start: " + j.start + " , " + "history: " + j.history +'\n'
                print(line)

            print(50*'-')


        elif i.get_type_car() == "Car_Carry_Continer":

            print(f'-------------Continers of CarryCar {i.carNumber}------------------')

            for j in i.list_continers_To_car:

                if j.get_type_continer() == "breakable_Container" :
                    line = "Continer breakable" + str(j.continerNumber) + ' : ' +  "weight: " + str(j.weight) + " , " +"countMax_pack: " + str(j.countMax_pack) + " , "  + 'speed: ' + j.speed +'\n'
                    print(line) 

                    for k in j.list_packs_To_breakable_Container:
                            
                        line = "Pack breakable" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history +'\n'
                        print(line)

            
                elif j.get_type_continer() == "Freezer_Container" :
                    line = "Continer Freezer" + str(j.continerNumber) + ' : ' +  "weight: " + str(j.weight) +  " , " +"countMax_pack: " + str(j.countMax_pack) +  " , "  + 'Car_refrigerator_temperature: ' + j.Car_refrigerator_temperature +'\n'
                    print(line)


                    for k in j.list_packs_To_Freezer_Container:

                        line = "Pack cold" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history + " , " + "temperature: " + k.temperature +'\n'
                        print(line)

            print(50*'-')

       # Get car as Cargo to add Werhous 

        while 1 :

            answer = input('Do you want to Append Cargo to warehous? : (y/n)') # Howmany AAAAAAAAAmir

            if answer == 'y':

                choose = int(input('Enter your Cargo :'))

                if choose == i.carNumber :
                    list_warehous.append(i)

            else :
                break

def Send_Letter_load_Cargo ():

    global f

    f = open('LTS.txt', 'a')

    for i in list_warehous:

        if i.get_type_car() == "Room_Car":

            f.write(f'Ordinary Packs of Room Car{i.carNumber} :\n')
            f.write('\n')
            for j in i.list_packs_ordinary:
                
                line = "Pack ordinary" + str(j.packNumber) + ': ' +  "weight: " + str(j.weight) + " , " +"destination: " + j.destination + " , " + "start: " + j.start + " , " + "history: " + j.history +'\n'
                f.write(line)
            f.write('\n')    
                 
        elif i.get_type_car() == "Car_Carry_Continer":

            f.write(f'Continers of CarryCar {i.carNumber} :')
            f.write('\n')

            for j in i.list_continers_To_car:

                if j.get_type_continer() == "breakable_Container" :
                    line = "Continer breakable" + str(j.continerNumber) + ' : ' +  "weight: " + str(j.weight) + " , " +"countMax_pack: " + str(j.countMax_pack) + " , "  + 'speed: ' + j.speed +'\n'
                    f.write(line) 

                    for k in j.list_packs_To_breakable_Container:
                            
                        line = "Pack breakable" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history +'\n'
                        f.write(line)


                elif j.get_type_continer() == "Freezer_Container" :
                    line = "Continer Freezer" + str(j.continerNumber) + ' : ' +  "weight: " + str(j.weight) +  " , " +"countMax_pack: " + str(j.countMax_pack) +  " , "  + 'Car_refrigerator_temperature: ' + j.Car_refrigerator_temperature +'\n'
                    f.write(line)


                    for k in j.list_packs_To_Freezer_Container:

                        line = "Pack cold" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history + " , " + "temperature: " + k.temperature +'\n'
                        f.write(line)    

# -------------------------------------------main-----------------------------------------------

def main():

    login()

    while 1:
        choose = menu_Handle()

        if choose == 1:
            choose_CRUD_Pack = menu_CRUD_pack()

            if choose_CRUD_Pack == 1:      # Append Pack
                insert_pack()
            elif choose_CRUD_Pack == 2:
                update_pack()
            elif choose_CRUD_Pack == 3:
                delete_pack()

        elif choose == 2:
            choose_CRUD_Continer = menu_CRUD_continer()
            if choose_CRUD_Continer == 1:      # Append Pack
                insert_continer()
            elif choose_CRUD_Continer == 2:
                update_continer()
            elif choose_CRUD_Continer == 3:
                delete_continer()

        elif choose == 3:
            choose_CRUD_Car = menu_CRUD_cars()

            if choose_CRUD_Car == 1:      # Append  car
                insert_car()
            elif choose_CRUD_Car == 2:
                update_car()
            elif choose_CRUD_Car == 3:
                delete_car()

        elif choose == 4:

            while 1:

                choose_menu_Loading = menu_Loading()

                if choose_menu_Loading == 1 :
                    display_packs()

                elif choose_menu_Loading == 2 :
                    display_continer()
            
                elif choose_menu_Loading == 3 :
                    display_cars()

                elif choose_menu_Loading == 4 :

                    sum_packW = 0     # for Check max weight package

                    display_continer()

                    choose_continer_to_Load = input('Which continer to Loading ? (Please write fullname of continer like :> breakable1 or Freezer1) :')

                    if len(choose_continer_to_Load) == 10:  # meaning: To Realize breakable (type of Continer) for line 443

                        for k in list_packs:  # فرآیند نشان دادن بار اول بسته های سازگار 

                            if k.get_type_pack() == "Pack_breakable" :

                                line = "Pack breakable" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history +'\n'
                                print(line)

                        for i in list_continers:

                            if i.continerNumber == int(choose_continer_to_Load[9]):     # meaning: (breakable1) number of continer   

                                countMax_pack = i.countMax_pack

                                howMany = int(input(f"How many 'Pack breakable' do you want to load continer breakable {i.continerNumber} ?")) 
                                if howMany > countMax_pack :
                                    print(f"Space of your continer is {countMax_pack} ! Please enter again") 
                                    
                                else:   

                                    j = 1
                                    while j<= howMany: 
                                        
                                        if sum_packW <= i.weight:
                                            for k in list_packs:  # فرآیند نشان دادن بسته های سازگار 

                                                if k.get_type_pack() == "Pack_breakable" :

                                                    line = "Pack breakable" + str(k.packNumber) + ' : ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history +'\n'
                                                    print(line)
                                            
                                            print()

                                            Number_pack_loading = int(input("Which Pack do you want to load continer? :")) 

                                            i.list_packs_To_breakable_Container.append(list_packs[Number_pack_loading-1])       

                                            sum_packW += list_packs[Number_pack_loading-1].weight

                                            list_packs.pop(Number_pack_loading-1)

                                            for q in list_packs:
                                                if q.packNumber > Number_pack_loading :
                                                    q.packNumber = q.packNumber -1 

                                        else:
                                            print('Oh! Sum of weight packs are greater than weight Continer ')
                                            break
                                        j+=1

                    elif len(choose_continer_to_Load) == 8:  # meaning: To Realize Freezer (type of Continer) for line 443

                        for k in list_packs:

                            if k.get_type_pack() == "Pack_cold" :        # فرایند نشان دادن بسته های سازگار

                                line = "Pack cold" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history + " , " + "temperature: " + k.temperature +'\n'
                                print(line)


                        for i in list_continers:

                            if i.continerNumber == int(choose_continer_to_Load[7]):     # meaning: (breakable1) number of continer  

                                countMax_pack = i.countMax_pack

                                howMany = int(input(f"How many 'Pack Cold' do you want to load continer Freezer {i.continerNumber} ?")) 
                                if howMany > countMax_pack :
                                    print(f"Space of your continer is {countMax_pack} ! Please enter again")

                                else:

                                    j = 1
                                    while j<= howMany:
                                    
                                        if sum_packW <= i.weight:

                                            for k in list_packs:

                                                if k.get_type_pack() == "Pack_cold" :        # فرایند نشان دادن بسته های سازگار

                                                    line = "Pack cold" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history + " , " + "temperature: " + k.temperature +'\n'
                                                    print(line)

                                            print()

                                            Number_pack_loading = int(input("Which Pack do you want to load continer? :")) 

                                            i.list_packs_To_Freezer_Container.append(list_packs[Number_pack_loading-1]) 

                                            sum_packW += list_packs[Number_pack_loading-1].weight

                                            list_packs.pop(Number_pack_loading-1)      

                                            for q in list_packs:
                                                if q.packNumber > Number_pack_loading :
                                                    q.packNumber = q.packNumber -1

                                        else:
                                            print('Oh! Sum of weight packs are greater than weight Continer ')
                                            break

                                        j+=1

                elif choose_menu_Loading == 5 :

                    sum_continerkW = 0
                      
                    for i in list_cars:

                        if i.get_type_car() == "Car_Carry_Continer" :
                            line = "car carry continer" + str(i.carNumber) + ' : ' +  "weight: " + str(i.weight) + " , " +"countMax_continer: " + str(i.countMax_continer) + '\n'
                            print(line)

                    choose_car_to_carry =  input('Which car to Carry ? (Please write fullname of car like :> carry1 ) :')


                    for k in list_continers:  #    برای how many

                        if k.get_type_continer() == "breakable_Container" :

                            line = "Continer breakable" + str(k.continerNumber) + ' : ' +  "weight: " + str(k.weight) + " , " +"countMax_pack: " + str(k.countMax_pack) + " , "  + 'speed: ' + k.speed +'\n'
                            print(line)    

                        elif k.get_type_continer() == "Freezer_Container" :

                            line = "Continer Freezer" + str(k.continerNumber) + ' : ' +  "weight: " + str(k.weight) + " , " +"countMax_pack: " + str(k.countMax_pack) + " , "  + 'Car_refrigerator_temperature: ' + k.Car_refrigerator_temperature +'\n'
                            print(line)


                    for i in list_cars:

                        if i.carNumber == int(choose_car_to_carry[5]):

                            countMax_continer = i.countMax_continer

                            howMany = int(input(f"How many 'continer' do you want to load car {i.carNumber} ?")) 
                            if howMany > countMax_continer :
                                print(f"Space of your car is {countMax_continer} ! Please enter again") 

                            else:

                                j = 1
                                while j<= howMany:

                                    if sum_continerkW <= i.weight:

                                        for k in list_continers:  # فرآیند نشان دادن کانتینر های سازگار 

                                            if k.get_type_continer() == "breakable_Container" :

                                                line = "Continer breakable" + str(k.continerNumber) + ' : ' +  "weight: " + str(k.weight) + " , " +"countMax_pack: " + str(k.countMax_pack) + " , "  + 'speed: ' + k.speed +'\n'
                                                print(line)    

                                            elif k.get_type_continer() == "Freezer_Container" :

                                                line = "Continer Freezer" + str(k.continerNumber) + ' : ' +  "weight: " + str(k.weight) + " , " +"countMax_pack: " + str(k.countMax_pack) + " , "  + 'Car_refrigerator_temperature: ' + k.Car_refrigerator_temperature +'\n'
                                                print(line)
                                
                                        print()
                                        
                                        Number_continer_carry = int(input("Which continer do you want to carry by car ? :")) 

                                        i.list_continers_To_car.append(list_continers[Number_continer_carry-1]) 

                                        sum_continerkW += list_packs[Number_continer_carry-1].weight

                                        list_continers.pop(Number_continer_carry-1)

                                        for q in list_continers:
                                            if q.continerNumber > Number_continer_carry :
                                                q.continerNumber = q.continerNumber -1 

                                    else:
                                        print('Oh! Sum of weight continers are greater than weight Car ')
                                        break

                                    j+=1

                elif choose_menu_Loading ==  6:

                    sum_packordinary = 0

                    for i in list_cars:

                        if i.get_type_car() == "Room_Car" :
                            line = "room car" + str(i.carNumber) + ' : ' +  "weight: " + str(i.weight) + " , " +"countMax_pack: " + str(i.countMax_pack) + '\n'
                            print(line)

                    choose_room_car =  input('Which Room Car ? (Please write fullname of car like :> room1 ) :')

                    for k in list_packs: 

                        if k.get_type_pack()== "Pack":

                            line = "Pack ordinary" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history +'\n'
                            print(line)

                    for i in list_cars:

                        if i.carNumber == int(choose_room_car[4]):

                            countMax_pack = i.countMax_pack

                            howMany = int(input(f"How many 'pack ordinary' do you want to load car {i.carNumber} ?")) 
                            if howMany > countMax_pack :
                                print(f"Space of your car is {countMax_pack} ! Please enter again")

                            else:

                                j = 1
                                while j <= howMany:

                                    if sum_packordinary <= i.weight:

                                        for k in list_packs: 

                                            if k.get_type_pack()== "Pack":

                                                line = "Pack ordinary" + str(k.packNumber) + ': ' +  "weight: " + str(k.weight) + " , " +"destination: " + k.destination + " , " + "start: " + k.start + " , " + "history: " + k.history +'\n'
                                                print(line) 

                                        print()

                                        Number_pack_loading = int(input("Which Pack do you want to load Car? :")) 

                                        i.list_packs_ordinary.append(list_packs[Number_pack_loading-1])       

                                        sum_packordinary += list_packs[Number_pack_loading-1].weight

                                        list_packs.pop(Number_pack_loading-1)

                                        for q in list_packs:
                                            if q.packNumber > Number_pack_loading :
                                                q.packNumber = q.packNumber -1 

                                    else:
                                        print('Oh! Sum of weight packs are greater than weight Car room ')
                                        break

                                    j+=1 

                elif choose_menu_Loading == 7 :
                    break
        
        elif choose == 5:

            choose_send_Receive = menu_Send_Receive_Cargo()

            if choose_send_Receive == 1:
                Display_cargo()

            elif choose_send_Receive == 2:
                Send_Letter_load_Cargo ()

        elif choose == 6 :
            display_packs()
        
        elif choose == 7:
            display_continer()

        elif choose == 8 :
            display_cars()

        elif choose == 9 :
            break



main()
input()
