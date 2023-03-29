#Create an empty list
superlist = []
#This code reads the csv 
with open("Employee+Demographics.csv", 'r') as reader:
    for line in reader.readlines():
        superlist.append(line)
    #Another empty list for future use
    a = []
    for i in range(0,11):
        b = superlist[i]
        print(b)