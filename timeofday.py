fileopen = 1
try:
    fhand = open("mbox-short.txt")
except:
    fileopen = -1
if fileopen < 1:
    print("Problem in Accessing the file")
else:
    dic = dict()
    for fline in fhand:
        # fline = fline.rsplit()
        if not fline.startswith("From "):
            continue
        words = fline.split(":")
        time = words[0]
        hours = int(time[-2:])
        if hours not in dic:
            dic[hours] = 1
        else:
            dic[hours] += 1
    lst = list(dic.keys())
    lst.sort()
    for key in lst:
        print(key, dic[key])
