"""Energy_level = ["Groggy Morning", "Mid Morning Energy Peak", "Afternoon Skump", "Early Evenings second wind", "Winding down for sleep"]
User_name = ['John', 'Mary', 'Phil', 'Tyler' 'kate' ' Mosh']
Step_count  = [1200, 2300, 2398, 3000, 4500, 4585, 6000]
All = (Energy_level, User_name, Step_count)
print(Energy_level)
print(User_name)
print(Step_count)
Energy_level.append('Mid afternoon')
User_name.append('Sandy')
Step_count.append('700')
print(All)"""




def Ts2():
    screen_times = [120, 95, 140, 160, 80, 100, 200]
    print(f'screen time for day 3:{screen_times[2]}')
    avg = screen_times[0] + screen_times[1] + screen_times[2] /3
    print(f'average : {avg}')
    screen_times[-1] = 500
    print(screen_times)
    print(max(screen_times))
    print(min(screen_times))
#Ts2()




def Ts3():
    listA = [1 , 2, 3]
    listB = [1, "2", 3.0]




def Ts4():
    notification = [34, 28, 55, 40, 60, 22, 18]
    print(notification [0:6])
    print(f'Highest day: {max(notification)}')
    print(f'Lowest day: {min(notification)}')
    print(f'Total notification : {sum(notification)}')
    avg = sum(notification) / 7
    print(f'Average : {avg}')
    value = int(input("What new value woukd you love to add?   "))
    notification.append(value)
    print(notification)


Ts4()
