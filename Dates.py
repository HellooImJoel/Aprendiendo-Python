### Dates ###

# Date time
# la libreria "datetime" utiliza codigo python combinado con objetos de tipo basico.

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime


now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())   # es la representacion unica de un tiempo espesfico, en el justo momento en el que se ejecuta, en base a un "timestamp" se puede inferir una fecha. un timestamp tiene formato estandar POSIX. 


print_date(now)

year_2024 = datetime(2024, 4, 28)

print_date(year_2024)


# Time

current_time = time(17,2,23) # es un objeto que nos sirve para encapsular tiempo, pero no es capaz de rellenar los valores de sus atributos por si mismos.

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 5, 1)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


# Operaciones con fechas

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date # si los objetos son del mismo tipo si es posible realizar una diferencia.
print(diff)


# Timedelta
# sirve para operar con diferencias de fechas.

start_timedelta = timedelta(200, 100, 100, weeks = 10)  
end_timedelta = timedelta(300, 100, 100, weeks = 13) 

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
















