import csv


titles  = set()

dic = {}
with open("Favorite TV Shows - Form Responses 1.csv") as file:
    # declared the file inside reader variable
    reader  = csv.reader(file)
    # your a choice if you want to work with (list) or (dict)
    # my work using list
    next(reader) # if you using (dict) don't should be use this line

    for i in reader:
        # add the column of title from file to titles variable , his type is (set)
        # using the set means don't repeat any words twice
        titles.add(i[1].upper().strip())
    
    for i in sorted(titles):
        # declare the words from titles variable in dic anf give the value of key "0"
        dic[i] = 0
with open("Favorite TV Shows - Form Responses 1.csv") as file:  
    reader = csv.reader(file)
    # here well be count the words inside the dictionary (dic)
    for row in reader:
        title = row[1].upper().strip()
        if title in dic:
            dic[title] += 1

# print (dic)
for row in dic:
    print(f"{row} : {dic[row]}")
    
 