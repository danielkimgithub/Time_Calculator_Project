def add_time(start, duration, day_of_week=False):

    days_of_week_index = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
    
    days_of_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # split start time into hours, minutes, AM/PM
    start_tuple=start.partition(':')
    start_minute_tuple= start_tuple[2].partition(' ')
    start_hours = int(start_tuple[0])
    start_minute = int(start_minute_tuple[0])
    am_pm = start_minute_tuple[2]
    am_pm_flip = {"PM": "AM", "AM": "PM"}

    # split duration into hours and minutes
    duration_tuple=duration.partition(':')
    durationhr = int(duration_tuple[0])
    durationmin = int(duration_tuple[2])

    # number of days from durationhr
    number_of_days = int(durationhr / 24)

    # print total minutes with variable end_minutes
    end_minutes = start_minute + durationmin
    # limit minutes to less than 60
    while end_minutes >= 60:
        start_hours += 1
        end_minutes = end_minutes - 60

    # new final hour mark, limit to 12 and set to 12 if modulo equals 0
    end_hours = (start_hours + durationhr) % 12
    end_hours = end_hours = 12 if end_hours == 0 else end_hours

    # if final minute is less than 10, add '0' before digit
    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)

    # if meridiem is set to 'PM' and start_hours + the remainder of durationhr/24 is less than or equal to 12, add another day to number of days
    if am_pm == "PM" and start_hours + (durationhr % 24) >= 12:
        number_of_days += 1 
        
    # number of meridiem flips 
    number_of_ampm_flips = int((start_hours + durationhr) / 12)
    # keep meridiem if number_of_ampm_flips is even, switch if odd
    am_pm = am_pm_flip[am_pm] if (number_of_ampm_flips % 2 == 1) else am_pm
    
    return_time = str(end_hours) + ":" + str(end_minutes) + ' ' + am_pm

    # if day_of_week is True
    if day_of_week:
        day_of_week = day_of_week.lower()
        index = int((days_of_week_index[day_of_week]) + number_of_days) % 7
        new_day = days_of_week_array[index]
        return_time = f"{return_time}, {new_day}"
        #return_time += ", " + new_day

    if number_of_days == 1:
        return_time = f"{return_time} (next day)"
        #return_time = return_time + ' ' + "(next day)"
    elif number_of_days > 1:
        return_time = f"{return_time} ({number_of_days} days later)"
        #return_time = return_time + " (" + str(number_of_days) + " days later)"
    
    return return_time

add_time('3:00 PM', '3:10')
add_time('11:30 AM', '2:32', 'Monday')
add_time('11:43 AM', '00:20')
add_time('10:10 PM', '3:10')
add_time('11:43 PM', '24:20', 'tueSday')
add_time('6:30 PM', '205:12')
