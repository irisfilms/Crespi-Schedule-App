from datetime import datetime


def parseicaldate(date):
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    hour = int(date[9:11])
    minute = int(date[11:13])
    second = int(date[13:15])

    time = datetime(year, month, day, hour, minute, second)

    return time
