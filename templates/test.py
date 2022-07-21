l = input("Enter your list: ")
r = []
for i in l:
    if i not in r:
        r.append(i)
    else:
        print(i, end='')