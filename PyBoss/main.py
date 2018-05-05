
import os
import csv

new_employee = []

Data1 = os.path.join("PyBoss", "employee_data1.csv")
with open(Data1, 'r') as csvfile1:
    readerdic1 = csv.DictReader(csvfile1)

#dict1 = {row[0]: row[4] for row in readerdic1}

#Data2 = os.path.join("PyBoss", "employee_data2.csv")
#with open(Data2, 'r') as csvfile2:
    #readerdic2 = csv.reader(csvfile2, delimiter=',')
#dict2 = {row[0]: row[4] for row in readerdic2}
for row in readerdic1:
    employ_ID = row["Emp ID"]
    Fullname = row.split(["name"], ' ')
    BirthDate = row["DOB"]
    SS = row["SSN"]
    States = row["State"]
print(["State"])
