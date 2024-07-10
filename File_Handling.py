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

#print(txt_file.read())
#print(txt_file.read(10))

#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())   # esta funcion itera el fichero y lo convierte en una lista.

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta C#")
print(txt_file.readline())

txt_file.close()

#os.remove("D:\Programas\VS Code\VS Code Projects\Python-Projects\my_file.txt")




















