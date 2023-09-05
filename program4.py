#argument is the file??
x = "/home/student/pie_time/data.csv"
countryNames = []
countryCodes = []

#opens and reads lines into a variable
def read_csv(file1):
    with open(file1,"r") as country:
        lines = country.readlines()
        return lines



def parse_csv(y):
    for i in read_csv(x):
        newlist = i.split(",")
        countryNames.append(newlist[0])
        countryCodes.append(newlist[1])
        

def print_data():
    for i in range(len(countryNames)):
        print("-------")
        print("Country Name: " + countryNames[i])
        print("Country Code: " + countryCodes[i])



a = read_csv(x)
parse_csv(a)
print_data()




