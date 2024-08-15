from parseicaldate import parseicaldate
import datetime


# extract ICS dict with class at current time
def getcurrentclass(ics):
    def findcurrentclass(item):
        offset = datetime.timedelta(minutes=3)
        start_time = parseicaldate(item["DTSTART;TZID=America/Los_Angeles"]) - offset
        end_time = parseicaldate(item["DTEND;TZID=America/Los_Angeles"]) + offset
        current_time = datetime.datetime.now()

        if start_time < current_time and end_time > current_time:
            return True
        else:
            return False

    return list(filter(findcurrentclass, ics))
