def add_time(start, duration, day = ''):
    hours = int(start.split()[0].split(":")[0])
    minutes = int(start.split()[0].split(":")[1])
    timeInterval = start.split()[1]
    addHours = int(duration.split(":")[0])
    addMinutes = int(duration.split(":")[1])
    time = ''
    dayLeft = ''
    dayChange = False
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = {"monday": 0,
               "tuesday": 1,
               "wednesday": 2,
               "thursday": 3,
               "friday": 4,
               "saturday": 5,
               "sunday": 6
               }

    if timeInterval == 'PM':
        dayChange = True
    newHours = hours + addHours
    newMinutes = minutes + addMinutes

    if newMinutes >= 60:
        newHours += newMinutes // 60
        newMinutes = newMinutes - (newMinutes // 60) * 60

    daysCounter = round(newHours / 24)

    while newHours >= 13:
        newHours = newHours - 12
        if timeInterval == 'AM':
            timeInterval = 'PM'
        else:
            timeInterval = 'AM'

    if len(str(newMinutes)) == 1:
        newMinutes = '0' + str(newMinutes)

    time += str(newHours) + ":" + str(newMinutes) + " " + timeInterval

    if daysCounter == 1 and dayChange:
        dayLeft = '(next day)'
    elif daysCounter > 1:
        dayLeft = f'({daysCounter} days later)'

    if len(day) > 0 and day.lower() in weekday:
        if daysCounter > 0 and dayChange:
            index = (weekday[day.lower()] + daysCounter) % 7
            day = week[index]
            return(f'{time}, {day} {dayLeft}')
        else:
            return(f'{time}, {day} {dayLeft}')
    else:
        if len(dayLeft) > 0:
            return(f'{time} {dayLeft}')
        else:
            return(time)
