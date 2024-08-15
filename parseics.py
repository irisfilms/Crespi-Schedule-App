# parse ICS data to list of dicts
def parseics(string):
    lines = string.split("\n")
    events = []
    event = {}

    for x in lines:
        x = x.strip()
        if x == "BEGIN:VEVENT":
            event = {}
        elif x == "END:VEVENT":
            events.append(event)
        elif (
            "DTSTART;TZID=America/Los_Angeles" in x
            or "DTEND;TZID=America/Los_Angeles" in x
        ):
            split_date = x.split(":")
            event[split_date[0]] = split_date[1]
        elif "SUMMARY" in x:
            split_summary = x.split(":")[1]
            event["Class"] = split_summary.split("P -")[0][:-2].strip()
            event["Period"] = split_summary[(len(split_summary) - 2) : -1]

    def filter_events(dic):
        if "DTSTART;TZID=America/Los_Angeles" in dic.keys():
            return True
        else:
            return False

    return list(filter(filter_events, events))
