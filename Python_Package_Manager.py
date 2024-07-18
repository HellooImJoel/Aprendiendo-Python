### Python Package Manager ###

"""
PIP(https://pypi.org/) stands for Preferred installer program. We use pip to install different Python packages. 
Package is a Python module that can contain one or more modules or other packages. 
A module or modules that we can install to our application is a package. In programming, 
we do not have to write every utility program, instead we install packages and import them to our 
applications.
"""

import numpy

import mypackage.arithmetics # pip install numpy


print(numpy.version.version)

numpy_array = numpy.array([23, 35, 52, 30, 30, 24, 67])
print(type(numpy_array))

print(numpy_array * 2)


import pandas  # pip install pandas


## pip list
## pip uninstall pandas
## pip show numpy

## pip install requests
import requests

#response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
#print(response)
#print(response.status_code)
#print(response.json())


## Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))


