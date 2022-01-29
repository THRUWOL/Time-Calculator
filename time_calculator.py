def add_time(start, duration):
    hours = int(start.split()[0].split(":")[0])
    minutes = int(start.split()[0].split(":")[1])
    timeInterval = start.split()[1]
    addHours = int(duration.split(":")[0])
    addMinutes = int(duration.split(":")[1])

    days = 0

    newHours = hours + addHours
    newMinutes = minutes + addMinutes
    if newMinutes >= 60:
        newHours += newMinutes // 60
        newMinutes = newMinutes - (newMinutes // 60)*60

    days = round(newHours / 24)
    while newHours >= 13:
        newHours = newHours - 12
        if timeInterval == 'AM':
            timeInterval = 'PM'
        else:
            timeInterval = 'AM'

    print(newHours, timeInterval, newMinutes, days)




# print("11:06 PM", "2:02")
# 1:08 AM (next day)
print(add_time("6:30 PM", "205:12"))
print(add_time("11:43 PM", "24:20"))
