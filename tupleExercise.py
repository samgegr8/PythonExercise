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
