with open("words5.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if len(i) != 5:
            f.write(i)
    f.truncate()