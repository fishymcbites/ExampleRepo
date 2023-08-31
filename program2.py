#employees = {"cheddar":"therapist","blueberry":"bully","mango":"fat","pepperjack":"pepperjack"}
#A dictionary is simply a tool to bonk someone on the head with.
#
#for fish,role in employees.items():
#    print("-----")
#    print("Name: " + fish)
#    print("Job: " + role)

#===========================

rank = []
firstnames = []
lastnames = []

with open("/home/student/pie_time/girl_boy_names_2004.csv","r") as names_csv:
    lines = names_csv.readlines()
    for i in lines:
        new_list = i.split(",")
        rank.append(new_list[0])
        firstnames.append(new_list[1])
        lastnames.append(new_list[2])

    for i in range(len(firstnames)):
        print("-----")
        print("Rank: " + rank[i])
        print("Girl Name: " + firstnames[i])
        print("Boy Name: " + lastnames[i])


