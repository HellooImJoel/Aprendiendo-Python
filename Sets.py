# Sets 

"""
Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered 
and un-indexed distinct elements. In Python set is used to store unique items, and it is possible 
to find the union, intersection, difference, symmetric difference, subset, super set and disjoint 
set among sets.
"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Joel", "Stadelman", 23}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("GrayScallet")
print(my_other_set)

################################# 

my_other_set.add("GrayScallet")  
print(my_other_set)             # un 'set' no admite elementos repetidos.

print("GrayScallet" in my_other_set)
print("GrayScalet" in my_other_set)

my_other_set.remove("Stadelman")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

print(len(my_other_set))

del my_other_set

my_set = {"Joel", "Stadelman", 23}
my_other_set = {"C#", "MongoDB", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))











