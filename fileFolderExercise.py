# Normal Read of File
fhand = open("mbox.txt")
print(fhand)
count = 0
for fline in fhand:
    count = count + 1
print("Number of lines::", count)

# This statement loop looks for a particular pattern. By Resetting the pointer back to start
fhand.seek(0)
# lhand = open("mbox.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line)

# This piece is printing a particular line change in Code
fhand.seek(0)
# lhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1:
        continue
    print(line)
