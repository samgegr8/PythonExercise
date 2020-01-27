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

# playing with lines from a text file and printing only emails

fileopen = 1
try:
    fhand = open("mbox-short.txt")
except:
    fileopen = -1
if fileopen < 1:
    print("Problem in Accessing the file")
else:
    for fline in fhand:
        # fline = fline.rsplit()
        if not fline.startswith("From:"):
            continue
        words = fline.split()
        print(words[1])

# Delete head from the list
def delete_head(p):
    del p[0]

t = ["a", "b", "c"]
delete_head(t)
print(t)
