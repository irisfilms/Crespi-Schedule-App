import re


# parse agenda text file into list of dicts
def parseagendas(string: str):
    lines = string.split("\n")
    agendas = []
    agenda = {}

    for x in lines:
        line = x.strip()
        if line == "BEGIN":
            agenda = {}
        elif line == "END":
            agendas.append(agenda)
        else:
            if re.search("^.*:.+$", x):
                text_prop = re.split(":", x)
                agenda[text_prop[0]] = text_prop[1].strip()
            else:
                if "Body" in agenda:
                    agenda["Body"].append(x)
                else:
                    agenda["Body"] = []
    return agendas
