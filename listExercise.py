# Normal Read of List
cheeses = ["Butter", "Jam", "Honey"]

for cheese in cheeses:
    print(cheese)

# Slicing of List
print(cheeses[:1])

# Appending a list
cheeses.append("Bread")
print(cheeses)

# Sorting a list
cheeses.sort()
print(cheeses)

# deleting an element from the list

element = cheeses.pop(1)
print(cheeses)
print(element)

# deleting more than one element from the list

del cheeses[0:1]
print(cheeses)

# difference between list and string
string_to_test = "Samrat"
t = list(string_to_test)
print(t)

