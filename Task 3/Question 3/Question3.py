with open("about.txt", "r") as read_object:
    content = read_object.read()
    
lst = content.split()
lst1 = []
d = {}

for i in range(len(lst)):
    word = lst[i]
    if word[-1] == ",":
        lst[i] = word[:-1]

for word in lst:
    if len(word)>=6:
        lst1.append(word)
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1


maximum = max(list(d.values()))

for i in d:
    if d[i] == maximum:
        print(i, "is the most frequently used word and it occurs ", d[i], "times")
        break



