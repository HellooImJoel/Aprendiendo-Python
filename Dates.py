# Dates

from datetime import datetime

# la libreria "datetime" utiliza codigo python combinado con objetos de tipo basico.

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


timestamp = now.timestamp()    # es la representacion unica de un tiempo espesfico, en el justo momento en el que se ejecuta, en base a un "timestamp" se puede inferir una fecha.
print(timestamp)               # un timestamp tiene formato estandar POSIX. 






