# Make a report of email address and the count of their emails
fopen = 1
try:
    fname = open("mbox-short.txt")
except:
    fopen = -1
    print("File Cannot be Opened")
if fopen < 0:
    print("Some issue with the files")
else:
    emailAddress = dict()
    for fhand in fname:
        # fhand = fhand.rsplit()
        if fhand.startswith("From:") != True:
            continue
        lineSplit = fhand.split()
        if lineSplit[1] not in emailAddress:
            emailAddress[lineSplit[1]] = 1
        else:
            emailAddress[lineSplit[1]] += 1


print("Printing report in Sorted Orders")
lst1 = list(emailAddress.keys())
lst1.sort()
for key in lst1:
    print(key, emailAddress[key])
