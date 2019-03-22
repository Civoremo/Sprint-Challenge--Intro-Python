# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
a = []
for item in humans:
    if item.name[0] == 'D':
        a.append(item.name)
print("Starts with D:")
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
b = []
for item in humans:
    if item.name.endswith('e'):
        b.append(item.name)
print("Ends with e:")
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
c = []
for item in humans:
    if ord(item.name[0]) in range(ord('C'), ord('G')+1):
        c.append(item.name)
print("Starts between C and G, inclusive:")
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
d = []
for item in humans:
    d.append(item.age + 10)
print("Ages plus 10:")
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
e = []
for item in humans:
    e.append(item.name + '-' + str(item.age))
print("Name hyphen age:")
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
f = []
for item in humans:
    if item.age >= 27 and item.age <= 32:
        f.append((str(item.name), int(item.age)))
print("Names and ages between 27 and 32:")
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
g = []
for item in humans:
    newHuman = Human(item.name.upper(), item.age+5)
    g.append(newHuman)

print("All names capitalized:")
print(g)

# Write a list comprehension that contains the square root of all the ages.
h = []
for item in humans:
    h.append(math.sqrt(item.age))
print("Square root of ages:")
print(h)
