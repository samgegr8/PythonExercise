# Tuple Assignments  and it types
t1 = ("a",)  # Always One element represent like this else it becomes a string
print(type(t1))

t = tuple("samrat")
print(t)

t1 = ("s", "b")
print(t1)

print(t[1:4])

print((9, 1, 8) < (2, 4, 6))  # it evaluates the first element and ignores the rest

# Sorting of word in the string from longest to shortest

txt = "but soft what light in yonder window breaks"
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)
for res, word in t:
    print(word)

# Dictionary to Tuples
d = {"a": 10, "b": 1, "c": 22}
l = list()
for key, val in d.items():
    l.append((val, key))
print(l)
# sorting the list
l.sort(reverse=True)
print(l)

# Sorting most common words in the text
import re

fopen = 1
try:
    fname = open("romeopunctuation.txt")
except:
    fopen = -1
    print("File Cannot be Opened")
if fopen < 0:
    print("Some issue with the files")
else:
    counts = dict()
    for fhand in fname:
        fhand = fhand.lower()
        fhand = re.sub("[^\w\s]", "", fhand)
        words = fhand.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    lst = list()
    for key, val in counts.items():
        lst.append((val, key))

    lst.sort(reverse=True)

    print("Printing 10 most popular words")
    for key, val in lst[:10]:
        print(key, val)

