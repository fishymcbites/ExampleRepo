countryNames = []
countryCodes = []


def read_csv(x):
    with open("/home/student/pie_time/data.csv","r") as country:
        lines = country.readlines()
        return lines

def parse_csv(y):
    for i in read_csv(lines):
        newlist = i.split(",")
        countryNames.append(newlist[0])
        countryCodes.append(newlist[1])
