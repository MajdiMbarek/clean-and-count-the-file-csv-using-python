import csv


titles  = set()

dic = {}
with open("Favorite TV Shows - Form Responses 1.csv") as file:
    reader  = csv.reader(file)
    next(reader)
    for i in reader:
        titles.add(i[1].upper().strip())
    
    for i in sorted(titles):
        dic[i] = 0
with open("Favorite TV Shows - Form Responses 1.csv") as file:  
    reader = csv.reader(file)
    for row in reader:
        title = row[1].upper().strip()
        if title in dic:
            dic[title] += 1
for row in dic:
    print(f"{row} : {dic[row]}")
    
 