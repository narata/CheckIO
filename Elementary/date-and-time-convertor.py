def date_time(time):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
    buf_1 = time.split(' ')
    time_list = buf_1[0].split('.') + buf_1[1].split(':')
    print(time_list)
    hour = "hour" if int(time_list[3]) == 1 else "hours"
    minute = "minute" if int(time_list[4]) == 1 else "minutes"
    return "{} {} {} year {} {} {} {}".\
        format(
            int(time_list[0]),
            months[int(time_list[1])-1],
            int(time_list[2]),
            int(time_list[3]),
            hour,
            int(time_list[4]),
            minute
        )


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
