# print a simple dictionary Way 1
eng2sp = dict()
eng2sp["one"] = "uno"
print(eng2sp)
# print a simple dictionary Way 2
eng2sp = dict()
eng2sp = {"one": "uno"}
print(eng2sp)

# find the word counts from a file using dict

fopen = 1
try:
    fname = open("romeo.txt")
except:
    fopen = -1
    print("File Cannot be Opened")
if fopen < 0:
    print("Some issue with the files")
else:
    counts = dict()
    for fhand in fname:
        words = fhand.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    print(counts)

# print it out in a sorted manner

lst = list(counts.keys())
print(lst)
lst.sort()
print("## Printing the list in a sorted order ##")
for key in lst:
    print(key, counts[key])

# parsing the characters with punctuation removal and ignoring case sensitivity

import string
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
    dic = dict()
    for fhand in fname:
        # fhand = fhand.rsplit()
        fhand = fhand.lower()
        fhand = re.sub("[^\w\s]", "", fhand)
        words = fhand.split()
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

print("Printing ignoring Punctuation and case sensitivity and printing in sorted order")
lst1 = list(dic.keys())
lst1.sort()
lst2 = list()
for key in lst1:
    print(key, dic[key])

