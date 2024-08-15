import datetime


def getcurrentagenda(ics: list, parsed_text: list):
    def findtext(variable):
        current_date = datetime.date.today()
        agenda_date = datetime.datetime.strptime(variable["Date"], "%m/%d/%Y").date()

        if (
            int(variable["Period"]) == int(ics[0]["Period"])
            and current_date == agenda_date
        ):
            return True
        else:
            return False

    return list(filter(findtext, parsed_text))
