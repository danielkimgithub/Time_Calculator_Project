def add_time(start, duration, start_date=''):

    ampm = start.split(' ')[1]

    time = start.split(' ')[0]
    # type string
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    # type string
    houradd = duration.split(':')[0]
    minadd = duration.split(':')[1]

    # type int for start
    hourint = int(hour)
    minuteint = int(minute)
    # type int for duration
    houraddint = int(houradd)
    minaddint = int(minadd)

    new_hour = hourint + houraddint
    new_minute = minuteint + minaddint

    # change hour if new_minute exceeds 60
    while new_minute % 60 != 0 and new_minute >= 60:
        count = 1
        new_minute -= (60*count)
        new_hour += (1*count)
        # switch am/pm if minute exceeds 60 minutes
        if count % 2 == 1:
            if ampm == 'PM':
                ampm = 'AM'
            else:
                ampm = 'PM'
        count += 1

    whole_days = (new_hour // 24) + 1
    print(whole_days)

    hcount = 1
    while new_hour % 12 != 0 and new_hour >= 12:
        new_hour = new_hour % 12
        # switch am/pm if minute exceeds 60 minutes
        if hcount % 2 == 1:
            if ampm == 'PM':
                ampm = 'AM'
            else:
                ampm = 'PM'
        hcount += 1
    

    # restrict to AM/PM time
    if new_hour % 12 == 0:
        new_hour = 12
    if new_hour % 24 == 0:
        ampm = 'AM'


    if new_minute < 10:
        new_minute = (f'0{new_minute}')
    new_time = (f"{new_hour}:{new_minute} {ampm}")
    print(new_time)


    #return new_time

add_time('11:43 PM', '24:20')
