# File Handling

import os

# .txt file

"""
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

txt_file = open("D:/Programas/VS Code/VS Code Projects/Python-Projects/my_file.txt", "w+")
txt_file.write("Mi nombre es Joel\nMi apellido es Stadelman\nTengo 23 años\nMi lenguaje preferido es Python")

print(txt_file.read())
print(txt_file.read(10))

print(txt_file.readline())
print(txt_file.readline())
#print(txt_file.readlines())   # esta funcion itera el fichero y lo convierte en una lista.

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta C#")
print(txt_file.readline())

txt_file.close()

#os.remove("D:\Programas\VS Code\VS Code Projects\Python-Projects\my_file.txt")


# .json file

import json

json_file = open("D:/Programas/VS Code/VS Code Projects/Python-Projects/my_file.json", "w+")

json_test = {
    "name":"Joel", 
    "surname":"Stadelman", 
    "age":23, 
    "languages":["Python", "MongoDB", "Kotlin"],
    "website":"https://joelst.dev"}            

json.dump(json_test, json_file, indent=2)  

json_file.close()


with open("D:/Programas/VS Code/VS Code Projects/Python-Projects/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("D:/Programas/VS Code/VS Code Projects/Python-Projects/my_file.json"))
print(json_dict)
print(type(json_dict))



# .csv file

import csv

csv_file = open("D:/Programas/VS Code/VS Code Projects/Python-Projects/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname","age" ,"language","website"])
csv_writer.writerow(["Joel", "Stadelman", 23, "Python","https://joelst.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL",""])

csv_file.close()

with open("D:/Programas/VS Code/VS Code Projects/Python-Projects/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx
# import xlrd # debe instalarse el modulo

# .xml file

import xml
